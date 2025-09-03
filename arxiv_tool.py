# step1: Access arXiv using URL
import requests


def search_arxiv_papers(topic: str, max_results: int = 5) -> dict:
    query = "+".join(topic.lower().split())
    for char in list('()" '):
        if char in query:
            print(f"Invalid character '{char}' in query: {query}")
            raise ValueError(
                f"Cannot have character: '{char}' in query: {query}")

    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{query}"
        f"&max_results={max_results}"
        "&sortBy=submittedDate"
        "&sortOrder=descending"
    )

    print(f"Making request to arxiv API: {url}")
    resp = requests.get(url)

    if not resp.ok:
        print(f"ArXiv Api request failed: {resp.status_code} - {resp.text}")
        raise ValueError(f"Bad response from arXiv Api: {resp}\n{resp.text}")

    # data = parse_arxiv_xml(resp.text)
    # return data
    return resp.text


print(search_arxiv_papers(topic="Prompt engineering", max_results=2))

# step2: parse XML
# step3: convert the functionality into a tool
