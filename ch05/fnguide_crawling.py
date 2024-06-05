import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

## 배당 수익 가져오기
#dividend_rate = soup.find(attrs = {'id':'svdMainGrid10D'})
#print(dividend_rate)

print(">>>>> find 이용")
dividend_rate = soup.find(attrs = {'id':'svdMainGrid10D'}).find_all("td", attrs = {'class':'r'})
print(dividend_rate)
print(dividend_rate[-6])
print(dividend_rate[-6].string)
print()

print(">>>>> select 이용")
#dividend_rate = soup.select('#svdMainGrid10D > table > tbody > tr:nth-child(8) > td:nth-child(2)')
dividend_rate = soup.select('#svdMainGrid10D > table > tbody > tr:nth-of-type(5) > tr:nth-of-type(3) > td.r')
print(dividend_rate)
print(dividend_rate[0])
print(dividend_rate[0].string)