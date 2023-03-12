# Scrapes tweets from a Twitter handle. It takes in a Twitter handle as an input and outputs 
# the text content of the tweets in that handle. Also uses proxy servers to bypass rate 
# limits and timeouts.
# 
# Not complete atm, as it only prints the number of tweets found and does not actually save them 
# to a database or a file. Also, it does not handle errors in the scraping process.

# Import the necessary libraries
from celery_main.celery import app
import proxy
from bs4 import BeautifulSoup

# Define a Celery task function with the input parameter 'handle'
@app.task(bind=True,default_retry_delay=10)
def do_work(self, handle):
    # Print the received handle for debugging purposes
    print('handle received ' + handle)
    # Construct the Twitter URL for the given handle
    url = "https://twitter.com/" + handle
    # Use the 'proxy' library to get a session with a proxy server
    session = proxy.get_session()
    # Send a GET request to the Twitter URL using the proxy server
    response = session.get(url, timeout=5)
    # Print the HTTP status code and the URL for debugging purposes
    print("-- STATUS " + str(response.status_code) + " -- " + url)
    # If the HTTP status code is 200 (OK), parse the tweets in the response
    if response.status_code == 200:
        parse_tweets(response, handle)

# Define a function to parse the tweets in the response and extract their text content
def parse_tweets(response, handle):
    # Use BeautifulSoup to parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'lxml')
    # Find all the tweet elements in the parsed HTML using their data-item-type attribute
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})
    # For each tweet element, extract its text content and add it to the 'tweets_list'
    for tweet in tweets:
        tweets_list.append(get_tweet_text(tweet))

    # Print the number of tweets found for debugging purposes
    print(str(len(tweets_list)) + " tweets found.")
    # TODO: Save the 'tweets_list' to a database or a file

# Define a function to extract the text content of a tweet element
def get_tweet_text(tweet):
    try:
        # Find the tweet text element in the tweet element using its CSS class
        tweet_text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        # Find any image links in the tweet text element and remove them from the text content
        images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
        tweet_text = tweet_text_box.text
        for image_in_tweet_tag in images_in_tweet_tag:
            tweet_text = tweet_text.replace(image_in_tweet_tag.text, '')
        # Return the cleaned up tweet text content
        return tweet_text
    except Exception as e:
        # Return None if there was an error in extracting the tweet text content
        return None
