#!/usr/bin/python3
"""This returns a list containing the titles of all hot articles for a given
subreddit. It returns none when and if no result is found.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """This returns a list containing the titles of all hot articles for a given
    subreddit. It returns none when and if no result is found..
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
