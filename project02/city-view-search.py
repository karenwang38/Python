import requests
from bs4 import BeautifulSoup

'''
#example
# Google 搜尋 URL
google_url = 'https://www.google.com.tw/search'
# 查詢參數
my_params = {'q': '新竹景點'}
# 下載 Google 搜尋結果
# 'https://www.google.com.tw/search?q=%E6%96%B0%E7%AB%B9%E6%99%AF%E9%BB%9E&btnG=%E6%90%9C%E5%B0%8B&rlz=1C5CHFA_enTW812TW812'
r = requests.get(google_url, params = my_params)
'''



#新竹 front page
#新竹景點 urlencoding => %e6%96%b0%e7%ab%b9%e6%99%af%e9%bb%9e
google_url = 'https://www.google.com.tw/search?q=%E6%96%B0%E7%AB%B9%E6%99%AF%E9%BB%9E&btnG=%E6%90%9C%E5%B0%8B&rlz=1C5CHFA_enTW812TW812'
google_url = 'https://www.google.com.tw/search?q=新竹景點&btnG=搜尋&rlz=1C5CHFA_enTW812TW812'

google_url = 'https://www.google.com.tw/search?sa=G&rlz=1C5CHFA_enTW812TW812&q=%E6%96%B0%E7%AB%B9%E6%99%AF%E9%BB%9E&npsic=0&rlst=f&rlha=0&rllag=24823371,121103423,18977&ved=0ahUKEwihlpD8oPLeAhXGf7wKHbsLA6cQjGoIMQ'

# url Disc
# sample
# https://www.google.com.tw/search?q=%E6%96%B0%E7%AB%B9%E6%99%AF%E9%BB%9E&rlz=1C5CHFA_enTW812TW812&prmd=ivnsm&ei=LAn8W_KGGYL88gWC6pIo&start=0&sa=N&rlst=f
url_encoding = {'台北市景點':'%e5%8f%b0%e5%8c%97%e5%b8%82%e6%99%af%e9%bb%9e',
                '新北市景點':'%e6%96%b0%e5%8c%97%e5%b8%82%e6%99%af%e9%bb%9e',
                '桃園市景點':'%e6%a1%83%e5%9c%92%e5%b8%82%e6%99%af%e9%bb%9e',
                '台中市景點':'%e5%8f%b0%e4%b8%ad%e5%b8%82%e6%99%af%e9%bb%9e',
                '台南市景點':'%e5%8f%b0%e5%8d%97%e5%b8%82%e6%99%af%e9%bb%9e',
                '高雄市景點':'%e9%ab%98%e9%9b%84%e5%b8%82%e6%99%af%e9%bb%9e',
                '基隆市景點':'%e5%9f%ba%e9%9a%86%e5%b8%82%e6%99%af%e9%bb%9e',
                '新竹市景點':'%e6%96%b0%e7%ab%b9%e5%b8%82%e6%99%af%e9%bb%9e',
                '嘉義市景點':'%e5%98%89%e7%be%a9%e5%b8%82%e6%99%af%e9%bb%9e'}
search_page = 10
fp=open('view_list.txt', 'w')
if fp !=None:
    for view in url_encoding:
        print('\n========',view,'=========')
        fp.write('\n========')
        fp.write(view)
        fp.write('========')
        for p in range(search_page):
            if p == 0:
                google_url = 'https://www.google.com.tw/search?q='+url_encoding[view]+'&rlz=1C5CHFA_enTW812TW812&prmd=ivnsm&ei=sAn8W-6kO8WE8wWjlozYBw&start=0&sa=N&rlst=f'
            else:
                google_url = 'https://www.google.com.tw/search?q='+url_encoding[view]+'&rlz=1C5CHFA_enTW812TW812&prmd=ivnsm&ei=LAn8W_KGGYL88gWC6pIo&start='+str(p)+'0&sa=N&rlst=f'

            r = requests.get(google_url)
            # 確認是否下載成功
            if r.status_code == requests.codes.ok:
              # 以 BeautifulSoup 解析 HTML 原始碼
              soup = BeautifulSoup(r.text, 'html.parser')

              # 觀察 HTML 原始碼
            #print(soup.prettify())

            # 以 CSS 的選擇器來抓取 Google 的搜尋結果
            #items = soup.select('div.g > h3.r > a[href^="/url"]')
            items = soup.find_all('div', class_='kR1eme gsrt rllt__wrapped')
            for i in items:
                # 標題
                print(i.text)
                fp.write('\n')
                fp.write(i.text)

                # 網址
                #print("網址：" + i.get('href'))
fp.close()
