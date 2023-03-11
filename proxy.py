# source: https://github.com/mattes/rotating-proxy
# docker-rotating-proxy
# 
#                Docker Container
#                -------------------------------------
#                         <-> Polipo 1 <-> Tor Proxy 1
# Client <---->  HAproxy  <-> Polipo 2 <-> Tor Proxy 2
#                         <-> Polipo n <-> Tor Proxy n
# 
# Why: Lots of IP addresses. 
# One single endpoint for your client. 
# Load-balancing by HAproxy.

import requests
import user_agents
import random

def get_session():
    # Create a session and set the proxy
    session = requests.session()
    session.proxies = {'http': 'rproxy:5566',
                       'https': 'rproxy:5566'}
    session.headers = get_headers()
    return session


def get_headers():
    # Set the headers for the session
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": random.choice(user_agents.useragents)
    }

    return headers