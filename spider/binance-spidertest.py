import urllib
#因为python3.X有时候不会将子模块自动导入进去，所以改成import url.request问题就解决了
import urllib.request
import requests
from bs4 import BeautifulSoup

# 賦值網站鏈接
quote_page='https://www.binance.com/tw'

## 使用假header (防止被偵測為爬蟲程式)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
page = requests.get(quote_page, headers=headers)


'''
[UA example: for a simple web-page]
User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53

原文網址：https://kknews.cc/zh-tw/tech/mjqmg.html
'''

# 檢索網站並獲取 html 代碼，存入變量”page”中
#page = urllib.request.urlopen(quote_page)
#html_context = page.read()

#page = requests.get(quote_page)
#print(page.url)
'''
此網站有防機器人功能
https://www.bloomberg.com/tosv2.html?vid=&uuid=be2eec20-e0c7-11e8-9dcc-7dce14f9fcbb&url=L3F1b3RlL1NQWDpJTkQ=
'''


# 用 beautifulSoup 解析 HTML 代碼並存入變量“soup”中`
#soup = BeautifulSoup(html_context, 'html.parser')
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
#print(soup.prettify())

# 獲取“名稱”類的<div> 代碼段落並提取相應值
#name_box = soup.find('h1', attrs={'class': 'logo'})
#p=soup.find('ul', id="producers")
name_box = soup.find_all('div', class_="ReactVirtualized__Table__rowColumn")
#print(name_box)

fp=open('Binance_raw_data.txt', 'w')
if fp !=None:
    i=0
    for m in name_box:
        fp.write(m.text)
        fp.write(",")
        print(m.text)
        if i%8==0:
            fp.write("\n")
        i=i+1



fp.close()


market=[]
Coin=[]
NerPrice=[]
_24Hour=[]
_24Hour_heightest=[]
_24Hour_lowest=[]
_24Hour_total=[]
number=[]

list_num = len(name_box)

for n in range(0,list_num):
    if n%8==1:
        market.append(name_box[n].text)
        #number.append(n)
    if n%8==2:
        Coin.append(name_box[n].text)
    if n%8==3:
        NerPrice.append(name_box[n].text)
    if n%8==4:
        _24Hour.append(name_box[n].text)
    if n%8==5:
        _24Hour_heightest.append(name_box[n].text)
    if n%8==6:
        _24Hour_lowest.append(name_box[n].text)
    if n%8==7:
        _24Hour_total.append(name_box[n].text)

'''
print("market: ", market)
print("Coin: ", Coin)
print("NerPrice: ", NerPrice)
print("_24Hour: ", _24Hour)
print("_24Hour_heightest: ", _24Hour_heightest)
print("_24Hour_lowest: ", _24Hour_lowest)
print("_24Hour_total: ", _24Hour_total)
'''






'''
GRS/BTC
Groestlcoin
0.00007762–
-1.62%
0.00008008
0.00007734
23.43958480

XZC/BTC
ZCoin
0.001561–
-1.08%
0.001580
0.001532
22.69728373

....

'''


'''
print(len(name_box))
#print(name_box[1])
print("0:",name_box[0].text)
print("1:",name_box[1].text)
#print(name_box[2])
print("2:",name_box[2].text)
#print(name_box[3])
print("3:",name_box[3].text)
print("4:",name_box[4].text)
print("5:",name_box[5].text)
print("6:",name_box[6].text)
print("7:",name_box[7].text)
print("8:",name_box[8].text)
print("9:",name_box[9].text)
print("10:",name_box[10].text)
print("11:",name_box[11].text)
print("12:",name_box[12].text)
print("13:",name_box[13].text)
print("14:",name_box[14].text)
print("15:",name_box[15].text)
print("16:",name_box[16].text)
'''

# <h1 class="logo">Bloomberg</h1>

#在我們得到標籤之後，我們可以用 name_box 的 text 屬性獲取相應值
# strip() 函數用於去除前後空格


#name = name_box.text.strip()
#print(name)
# Bloomberg
