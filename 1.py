import bs4
import requests
url = f"https://maplestory.nexon.com/Ranking/World/Total?page={1}&j=3&d=12"

result = requests.get(url).text
print(result)