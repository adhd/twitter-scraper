# twitter-scraper
A tweet scraper that doesn't use the Twitter API.

## Description

Twitter in 2023 is a treasure trove of unstructured natural language data. Many hobby programmers, researchers, and traders (among others) have written up simple scripts using libraries like `requests` and `bs4` in Python to scrape Twitter data (or alternatively using the suite of Twitter APIs -- an expensive choice better suited towards smaller hobby projects). Oftentimes, the speed at which tweets (and user data) can be scraped presents a barrier to tinkerers.

Why scrape Twitter? Ingesting data en masse (orders of magnitude larger than what the Twitter API can provide you) can allow you to gain insights about:

* Discussions related to a brand, products, country or city
* Competitors and their popularity, to gain some kind of competitive edge
* Emerging trends and attitudes about a topic
* Sentiments towards a brand or company, to protect investments
* Discussions related to services and community-based knowledge
* Consumer habits to develop new products or target underdeveloped niches

Data collected can be used:

* To train machine learning models
* Conduct academic research
* Combat fake news by understanding the pattern of how misinformation spreads.

## Getting Started

### Install Docker

Download and install [Docker Community Edition](https://www.docker.com/community-edition). If you're on macOS and have `Homebrew-Cask`, you can use `brew install --cask docker` to install Docker. Alternatively, download and install Docker Toolbox. Note that Docker For macOS is not quite as feature complete as its VirtualBox install counterpart. 

> **NOTE**: Docker Toolbox is legacy. You should use the Docker Community Edition.

### Installing

The `requirements.txt` file lists all Python libraries required, and can be installed using:

```bash
$ pip install -r requirements.txt
```

As an aside: `pip-compile` is a tool that can streamline combining loosely specified dependencies with a fully frozen environment. 

### Executing program

Start a Docker cluster. `sudo docker-compose up`. You should see something like the following output:

```
worker_1  | [2023-02-15 11:32:11,013: INFO/MainProcess] celery@6f03c7d4a1b8 ready.
```


* Step-by-step bullets
```
code blocks for commands
```

### Setting-up a rotating proxy
Taken from the [docker-rotating-proxy](https://github.com/mattes/rotating-proxy) repo. Usage as follows:

```
# build docker container
docker build -t mattes/rotating-proxy:latest .

# ... or pull docker container
docker pull mattes/rotating-proxy:latest

# start docker container
docker run -d -p 5566:5566 -p 4444:4444 --env tors=25 mattes/rotating-proxy

# test with ...
curl --proxy 127.0.0.1:5566 https://api.my-ip.io/ip

# monitor
http://127.0.0.1:4444/haproxy?stats
```

## Help

Any advice for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. might be dave 
ex. [@mightBeDave](https://github.com/adhd)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
