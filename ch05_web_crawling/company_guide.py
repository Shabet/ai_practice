import urllib.request as req
from bs4 import BeautifulSoup


url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='
res = req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")


## 배당 수익률 가져오기

dividend_rate_find_all = soup.find(attrs = {'id': 'svdMainGrid10D'}).find_all("td",attrs = {'class':'r'})
dividend_rate = soup.select("#svdMainGrid10D > table > tbody > tr:nth-of-type(5) > tr:nth-of-type(3) > td.r ")


print("종목 배당 수익률: ",dividend_rate[0].string)
print("종목 배당 수익률: ",dividend_rate_find_all[-6].string)


