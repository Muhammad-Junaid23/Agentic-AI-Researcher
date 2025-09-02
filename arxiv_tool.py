# step1: Access arXiv using URL
import requests

query = "Prompt Engineering"
max_results = 1

url = (
    "http://export.arxiv.org/api/query"
    f"?search_query=all:{query}"
    f"&max_results={max_results}"
    # "&sortBy=submittedtDate"
    "&sortOrder=descending"
)

resp = requests.get(url)
print("response: ", resp.status_code)
print("response: ", resp.text)

# step2: parse XML
# step3: convert the functionality into a tool
