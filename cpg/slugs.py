from curl_cffi import requests

def get_slug(title: str) -> str | None:
    query = {
        "query": """
        query problemsetQuestionList($searchKeyword: String) {
            problemsetQuestionList: questionList(
                categorySlug: ""
                filters: { searchKeywords: $searchKeyword }
                limit: 1
                skip: 0
            ) {
                questions: data {
                    title
                    titleSlug
                }
            }
        }
        """,
        "variables": {"searchKeyword": title},
    }
    resp = requests.post(
        "https://leetcode.com/graphql",
        json=query,
        impersonate="chrome",
    )
    resp.raise_for_status()
    questions = resp.json()["data"]["problemsetQuestionList"]["questions"]
    for q in questions:
        if q["title"].casefold() == title.casefold():
            return q["titleSlug"]
    return None