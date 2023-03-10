import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_apikey = os.environ.get("STOCK_API_KEY")
news_apikey = os.environ.get("NEWS_API_KEY")

account_sid = "ACae6761704379db12e2a381a5842375a9"
auth_token = os.environ.get("TWI_AUTH_TOKEN")

symbol = ""

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_apikey,
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()


date = datetime.now()
yesterday_date = date - timedelta(1)
yesterday = str(yesterday_date.date())

two_days_date = date - timedelta(2)
two_days = str(two_days_date.date())

yesterday_data_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
two_days_close = float(stock_data["Time Series (Daily)"][two_days]["4. close"])
percentage = round(((yesterday_data_close - two_days_close) / yesterday_data_close) * 100)

if percentage <= -5 or percentage >= 5:

    if percentage <= -5:
        symbol = "🔻"
    elif percentage >= 5:
        symbol = "🔺"

    parameters = {
        "q": COMPANY_NAME,
        "from": two_days,
        "yesterday": yesterday,
        "language": "en",
        "apiKey": news_apikey,
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    top_3_news = news_data["articles"][:3]

    client = Client(account_sid, auth_token)
    for article in top_3_news:
        headline = article["title"]
        brief = article["description"]
        news_link = article["url"]

        message = client.messages.create(
            body=f"{STOCK}: {symbol}{abs(percentage)}%\n\nHeadline: {headline}\n\nBrief: {brief}\n\nRead More: {news_link}",
            from_="+13159035188",
            to="+2348068925885"
        )
        print(message.status)

