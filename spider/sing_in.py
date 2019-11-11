import requests
#from lxml import html
from bs4 import BeautifulSoup


'''
STEP
1. Get login url
2. Get infomaiton for login : useremail, password, csrfmiddlewaretoken
3. request.post to send login infomation for login
4. Check login success: check userID is our ID: karenwang
'''

USEREMAIL = 'karen.wang38@gmail.com'
PASSWORD = 'ji31su31'
LOGIN_URL = 'https://anewstip.com/accounts/login/'
USERID = 'karenwang'

'''
撰寫在登入頁面先拿取token的部分
requests.session()是幫助我們把這一次的request都算在同一個session裡，
這樣我們第二次對登入頁面發request時，csrfmiddlewaretoken value才不會又重新產生。
'''
def main():
    session_requests = requests.session()
    #print(session_requests)

            # 1. enter login url
            # 2. get infomaiton for login : useremail, password, csrfmiddlewaretoken
    result = session_requests.get(LOGIN_URL)
    if result.status_code == requests.codes.ok:
        print("Get Login URL Success!")
    #tree = result.text
    # print("result =", result)
    tree = BeautifulSoup(result.text, 'html.parser')
    #authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]
    authenticity_token = tree.find('input', {'name':'csrfmiddlewaretoken'})['value']


    #print("result = ",result)
    #print("tree =", tree)
    #print("authenticity_token =", authenticity_token)

    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '101',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://anewstip.com',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': LOGIN_URL,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'GA1.2.795940461.1542293378; _gid=GA1.2.1686174136.1542293378; messagesUtk=a947d04c5685437596c62843671fc042; hs-messages-is-open=false; __hstc=107920349.a947d04c5685437596c62843671fc042.1542293384425.1542293384425.1542293384425.1; __hssrc=1; hubspotutk=a947d04c5685437596c62843671fc042; csrftoken='+authenticity_token+'; sessionid=zjyvxivheaja0xqroowg6awaoa71zdyo; __hssc=107920349.26.1542293384425'
    }

    payload = {
        'email': 'karen.wang38@gmail.com',
        'password': 'ji31su31',
        'csrfmiddlewaretoken': authenticity_token
    }
    '''
    7. 以POST method登入
    以剛剛啟動的session實例來發post request，才會在同一個session裡。後面記得帶上登入資訊及標頭參數
    '''

            # 3. request.post to send login infomation for login

    result = session_requests.post(LOGIN_URL, data = payload, headers = headers)
    #print("result= ", result)

            # 4. cehck login success: check userID is our ID: karenwang
    URL = "https://anewstip.com/"
    result = session_requests.get(URL, headers = dict(referer = URL))
    soup = BeautifulSoup(result.text, 'html.parser')
    #print(soup)
    id = soup.find_all('script')

    '''
    print("id =",id)
    print(len(id))
    print('-------')
    print("0 :",id[0])
    print("1 :",id[1])
    print("2 :",id[2])
    print("3 :",id[3])
    print("4 :",id[4])
    #<script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','//www.google-analytics.com/analytics.js','ga');ga('create', 'UA-57474640-1', { 'userId': 'karenwang-17354' }); ga('set', 'dimension1', 'karenwang-17354'); ga('send', 'pageview');</script>
    print("5 :",id[5])
    print("6 :",id[6])
    '''

    id_find = id[4].text
    #print(id_find)
    #print(len(id_find))


    #print(type(id_find))
    #print(USERID in id_find)
    if USERID in id_find:
        print("Login success!!!")
    else:
        print("Login fail!!!")

    # 跑起來之後output你會得到每個記者的profile url
    for i in range(1,11):
        URL = 'https://anewstip.com/search/journalists/?q=privacy&page=' + str(i)
        result = session_requests.get(URL, headers = dict(referer = URL))
        soup = BeautifulSoup(result.text, 'html.parser')

        # <span class="info-name"><a href="/journalist/profile/dv2-15637e7a/" target="_blank">Donald Aplin</a></span>
        for link in soup.select('.info-name a'):
            print('https://anewstip.com/'+link.get('href'))


if __name__ == '__main__':
    main()


'''
for i in id_find:
    print(i)
'''





'''
#karen's MacOS
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 101
Content-Type: application/x-www-form-urlencoded
Cookie: _ga=GA1.2.795940461.1542293378; _gid=GA1.2.1686174136.1542293378; messagesUtk=a947d04c5685437596c62843671fc042; hs-messages-is-open=false; __hstc=107920349.a947d04c5685437596c62843671fc042.1542293384425.1542293384425.1542293384425.1; __hssrc=1; hubspotutk=a947d04c5685437596c62843671fc042; csrftoken='+authenticity_token+'; sessionid=zjyvxivheaja0xqroowg6awaoa71zdyo; __hssc=107920349.26.1542293384425
Host: anewstip.com
Origin: https://anewstip.com
Referer: https://anewstip.com/accounts/login/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
'''


'''
HTML

<html>

<form action="process">
<input type="hidden" name="_AntiCsrfToken" value="5435434354353453545">

</form>
</html>
Python:

from bs4 import BeautifulSoup as bs4
import requests

r = requests.get('http://maffaz.com/so.html')
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')
token = soup.find('input', {'name':'_AntiCsrfToken'})['value']
print(token)
returns:

5435434354353453545
Also you do not need

{'name':'_AntiCsrfToken'}
so:

token = soup.find('input')['value']
Will work
'''
