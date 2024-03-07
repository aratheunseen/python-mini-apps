import requests
import mailer
from datetime import datetime,date,timedelta

topic = "apple"
start_date = str((date.today()-timedelta(days=3)).strftime("%Y-%m-%d"))
end_date = str(datetime.now().strftime("%Y-%m-%d"))
language = "en"

# Change NewsAPI.org key (Its a sample key)
api_key = "06f80f048654d7f74d5f41252eb5c4b319c"
url = f"https://newsapi.org/v2/everything?q={topic}&from={start_date}&to={end_date}&language={language}&sortBy=popularity&apiKey={api_key}"

# Make request
response = requests.get(url)

# Convert to json
content = response.json()

# Access content
name = "The Newsletter"
message = ""
for article in content["articles"][:20]:
    if article['title'] is not None:
        message = f"{message}\n{article['title']}\n{article['description']}\n{article['url']}\n\n"

mail_body = f"""Subject: Latest update of {topic} from {name}"\

{message}
"""
body = mail_body.encode('utf-8')

mailer.send_mail(body)