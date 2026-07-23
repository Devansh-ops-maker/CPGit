from cpg.cffi_backend import query,get_headers
from curl_cffi import requests
from cpg.slugs import get_slug
import sys


def details():
    file_name=str(sys.argv[1])

    title_slug=get_slug(file_name)

    if title_slug is None:
        print("Problem not found")
        return 

    payload={
        "query":query,
        "variables":{
            "titleSlug":title_slug
        }
    }

    response = requests.post(
    "https://leetcode.com/graphql",
    json=payload,
    headers=get_headers(title_slug),
    impersonate="chrome"
    )

    response.raise_for_status()

    problem=response.json()["data"]["question"]

    if problem is None:
        print("Problem not found")
        return

    topics=set()

    for topic in problem['topicTags']:
        topics.add(topic['name'])

    print(f"Title: {problem['title']}")
    print(f"TitleSlug: {problem['titleSlug']}")
    print(f"Difficulty: {problem['difficulty']}")
    print(f"Acceptance Rate: {problem['acRate']:.2f}")
    print("Topics: ",end=" ")
    
    for topic in topics:
        print(topic,end=" ")
    print()
    
