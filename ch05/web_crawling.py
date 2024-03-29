from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div>
 <p>AI</p>
 <p>개발</p>
 <p href="a.html">실무</p>
 <p id="yoon">실무AI_Id</p>
 <p class="yoon">실무AI_Class</p>

</div>
</body>
</html>
'''

print(">>>> 1")
soup = BeautifulSoup(html, 'html.parser')
print(soup.html.body.div)                   # DOM 구조를 파악하여 접근
print()
print(soup.find("p"))                       # 태그로 접근
print()
print(soup.find("p").string)                # 태그로 접근
print()
print(soup.find_all("p"))                   # 태그로 접근
print()
print(soup.find(href = "a.html"))           # 태그 속성으로 접근
print()
print(soup.find(attrs = {'href':"a.html"})) # 태그 속성으로 접근
print()
print(soup.find(string = "개발"))           # 특정 문자열로 검색
print()

print(">>>> 2")
beautifulSoup = BeautifulSoup(html, 'html.parser')
beautifulSoup.find(attrs = {'href':"a.html"})
print(beautifulSoup.select("p"))
print()
print(beautifulSoup.select(".yoon"))
print()
print(beautifulSoup.select("#yoon"))
print()
print(beautifulSoup.select("p#yoon"))
print()
print(beautifulSoup.select("p.yoon"))
print()
print(beautifulSoup.select("html > body > div > p"))
print()
print(beautifulSoup.select("html > body > div > p.yoon"))
print()
