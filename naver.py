import requests
# import urllib.request
# 위와 기능 똑같음 둘중 편한 것 쓰면 됌
import pandas as pd
from bs4 import BeautifulSoup

# requsts 모듈은 status 안 써도 상태코드 출력 가능
url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# soup.find_all("li", "on")
exchangeList = soup.select("#exchangeList > li") 
# class면 .을 사용하고 id면 #을 사용
# > 는 바로 밑에. 하위를 의미. exchangeList 밑에 li태그를 가리킴

# 4개 데이터 수집
exchange_datas = []
baseUrl = "https://finance.naver.com"

for item in exchangeList: #excgangeList 안에는 미국, 일본, EU, 중국 총 4개나라 데이터가 담겨있음 #exchangeList[n]이 item으로 대체됨
    data ={
        "title" : item.select_one(".h_lst").text,
        "exchange" : item.select_one(".value").text,
        "change" : item.select_one(".change").text,
        "updown" : item.select_one(".head_info.head_info > .blind").text, 
        "link" : baseUrl + item.select_one("a").get("href")
    
    }
    exchange_datas.append(data)

df = pd.DataFrame(exchange_datas)

df.to_excel("./naverfinance.xlsx", encoding="utf-8")