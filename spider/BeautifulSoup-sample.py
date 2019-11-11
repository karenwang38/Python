from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)

'''
# 另外，我們還可以用本地HTML 文件來創建對象，例如
soup = BeautifulSoup(open('index.html'))
'''

# 下面我們來打印一下soup 對象的內容，格式化輸出
#print (soup.prettify())

'''
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
'''

# tag : title, head, body, p, a...
print("soup.head =", soup.head)
# <head><title>The Dormouse's story</title></head>
print("soup.a =", soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print("soup.head.name =", soup.head.name)
# soup.head.name = head
print("soup.a.name =", soup.a.name)
# soup.a.name = a
print("soup.a.attrs =", soup.a.attrs)
# soup.a.attrs = {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
print("soup.a['class'] =", soup.a['class'])
# soup.a['class'] = ['sister']
print("soup.head.string =", soup.head.string)
# soup.head.string = The Dormouse's story

print (soup.a.string)
#  Elsie
print (type(soup.a.string))
# <class 'bs4.element.Comment'>

'''
a 標籤裡的內容實際上是註釋，但是如果我們利用.string 來輸出它的內容，我們發現它已經把註釋符號去掉了，所以這可能會給我們帶來不必要的麻煩。

另外我們打印輸出下它的類型，發現它是一個Comment 類型，所以，我們在使用前最好做一下判斷，判斷代碼如下
if type(soup.a.string)==bs4.element.Comment:
    print (soup.a.string )
'''
a_tag = soup.find_all('a')
print("a_tag : \n", a_tag)
'''
a_tag :
 [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''
print("-------------")
print(a_tag[0].text)
#
print(a_tag[1].text)
# Lacie
print(a_tag[2].text)
# Tillie

for context in a_tag:
    print(context)
'''
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
'''

for context in a_tag:
    print("context: ", context.text)
    print("link: ", context.get('href'))
'''
context:
link:  http://example.com/elsie
context:  Lacie
link:  http://example.com/lacie
context:  Tillie
link:  http://example.com/tillie
'''
