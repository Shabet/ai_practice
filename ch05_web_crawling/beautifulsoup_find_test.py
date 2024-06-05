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