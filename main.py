import requests
from send_email import send_email

body=""

api_key = "d8bc696b0f3540ffacd8f9f3ced26f21"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-05-19&sortBy=" \
"publishedAt&apiKey=d8bc696b0f3540ffacd8f9f3ced26f21"


# make request

req = requests.get(url)

#Get Dictionary 
content = req.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("ascii", "ignore").decode("ascii")
send_email(body)   