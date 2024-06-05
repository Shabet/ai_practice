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





