import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "988857c3897541eeb4afafcafeff82bb"
STOCK_API_KEY = "56G7T1CYS4BIWXJS"
PARAMETER_STOCK = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
res = requests.get(url=STOCK_ENDPOINT, params=PARAMETER_STOCK)
res.raise_for_status()
data = res.json()["Time Series (Daily)"]
new_list = [value for (key, value) in data.items()]

#TODO 2. - Get the day before yesterday's closing stock price
yes_close = float(new_list[0]["4. close"])
prev_close = float(new_list[1]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
result = abs(round(yes_close - prev_close, 2))
if yes_close > prev_close:
    print(f"yesterday close is increase{result} points")
elif yes_close < prev_close:
    print(f"yesterday close is decrease {result} points")
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_point = round(result / yes_close * 100, 2)
print(f"different is {diff_point} percent")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if diff_point < 2 or diff_point > 2:
    print("get news")
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
NEWS_PARAMETER = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
}
if diff_point < 2 or diff_point > 2:
    news_res = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETER)
    news_res.raise_for_status()
    articles = news_res.json()["articles"]


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_arc = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 
    for news in formatted_arc:
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
            connect.starttls()
            connect.login(user="", password="")
            connect.sendmail(from_addr="", to_addrs="",
                             msg=f"There news on your {COMPANY_NAME} stocks\n\n{news}")



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

