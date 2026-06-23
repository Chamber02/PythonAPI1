import requests
from send_email import send_email

topic = "tesla"
body=""

api_key = "d8bc696b0f3540ffacd8f9f3ced26f21"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
"from=2026-06-19&sortBy=" \
"publishedAt&" \
"apiKey=d8bc696b0f3540ffacd8f9f3ced26f21&language=en"


# make request

req = requests.get(url)

#Get Dictionary 
content = req.json()

#Access the article titles and description
for article in content["articles"][0:20]:
    print(article["title"])
    print(article["description"])
    body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] +2*"\n"

body = "Subject: Today's news"+ "\n" + body
body = body.encode("utf-8")
send_email(body)   