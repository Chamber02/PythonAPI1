import requests

api_key = "d8bc696b0f3540ffacd8f9f3ced26f21"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-05-19&sortBy=" \
"publishedAt&apiKey=d8bc696b0f3540ffacd8f9f3ced26f21"



req = requests.get(url)
content = req.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])