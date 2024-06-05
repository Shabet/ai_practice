# 웹 크롤링

## robots.txt 열어보기

- 크롤링 하고자 하는 웹 사이트의 robots.txt를 확인해 본다.
  * robots.txt 예시
    + [www.naver.com/robots.txt ](https://www.naver.com/robots.txt )
    + [www.cuk.edu/robots.txt ](https://www.cuk.edu/robots.txt )
    + [www.daum.net/robots.txt ](https://www.daum.net/robots.txt )


## beautifulsoup을 활용한 HTML 파싱

- beautifulsoup 설치

```
pip install beautifulsoup4
```

- beautifulsoup을 이용한 파싱 테스트
  + find() 함수

```
from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div>
 <p>AI</p>
 <p>개발</p>
 <p href="a.html">실무</p>

</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.html.body.div)  # DOM 구조를 파악하여 접근
print(soup.find("p"))  # 태그로 접근
print(soup.find("p").string)  # 태그로 접근
print(soup.find(href = "a.html"))  # 태그 속성으로 접근
print(soup.find(attrs = {'href':"a.html"}))  # 태그 속성으로 접근
print(soup.find(string = "개발"))  # 특정 문자열로 검색
'''

beautifulSoup = BeautifulSoup(html, 'html.parser')
beautifulSoup.find(attrs = {'href':"a.html"})
```

  + find_all() 함수

```
from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div>
 <p>AI</p>
 <p>개발</p>
 <p href="a.html">실무</p>

</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all("p"))

for i in soup.find_all("p"):  # 태그로 접근
    print(i)
```

## 웹에서 증권정보 가져오기

- [fnguide ](https://comp.fnguide.com/ ) 에서 증권정보 수집하기

```
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

```


