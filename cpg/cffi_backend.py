from curl_cffi import requests

query = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    difficulty
    acRate
    topicTags {
      name
      slug
    }
  }
}
"""

def get_headers(slug):
    return {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "Origin": "https://leetcode.com"
    }