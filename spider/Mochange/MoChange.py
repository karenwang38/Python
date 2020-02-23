import requests
from bs4 import BeautifulSoup
from lxml import html
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

# # 下載 Yahoo 首頁內容
# r = requests.get('https://www.mochange.co/products/shop_info.php?product_sernum=720')
#
# # 確認是否下載成功
# if r.status_code == requests.codes.ok:
#   # 以 BeautifulSoup 解析 HTML 程式碼
#   soup = BeautifulSoup(r.text, 'html.parser')
#   print(soup)
#
# # 以 CSS 的 class 抓出各類頭條新聞
# stories = soup.find_all('span', class_='fl')
# print(stories)
# for s in stories:
#     # 新聞標題
#     print("list：" + s.text)
URL = 'https://www.mochange.co/products/shop_info.php?product_sernum=530'
account_data = [{'email' : 'karen.wang38@gmail.com', 'id' : 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=', 'length' : '61'},
                {'email' : 'llibs38@gmail.com',      'id' : 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=', 'length' : '57'},
                {'email' : 'chctrader@gmail.com',    'id' : 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=', 'length' : '61'},
                {'email' : 'chctrader001@gmail.com', 'id' : '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=', 'length' : '63'}]
itmeList = ['527', '509', '624', '626', '628', '531']
# print('account data: ', account_data)
# llibs38_id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
# karenwang38_id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
# chctrader_id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
# 大柱_id = 'McHvxIefazHIGc8aJ+Qr/MO9kTIZ0c86tcT/EO5pdW0='


session_requests = requests.session()
# result = session_requests.get(URL)
# if result.status_code == requests.codes.ok:
#     print("Get URL Success!")
# else:
#     print("Get URL Fail!")

# 登入
def Login(email, computer):
    loginResult = False




    #karen mac
    login_url = 'https://www.mochange.co/member_login/member_login.php'

    # # llibs windows
    # login_url = 'https://www.mochanji.com/member_login/member_login.php'


    if computer == 'mac':
        login_headers = {
            # # karen mac
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '59',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.1080974198.1570156735; _gat_gtag_UA_139121893_1=1',
            # 'Host': 'www.mochange.co',
            # 'Origin': 'https://mochange.mohist.com.tw',
            # 'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochange.co',
            # 'Sec-Fetch-Mode': 'navigate',
            # 'Sec-Fetch-Site': 'cross-site',
            # 'Sec-Fetch-User': '?1',
            # 'Upgrade-Insecure-Requests': '1',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '59',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.1040713635.1582003150',
            'Host': 'www.mochange.co',
            'Origin': 'https://mochange.mohist.com.tw',
            'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochange.co',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',


        }

    elif computer == 'windows':
        login_headers = {
            # # llibs windows
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '54',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=ft987iase39p75g278r50eb7q6; _gid=GA1.2.749101058.1571282254; _gat_gtag_UA_139121893_1=1',
            # 'Host': 'www.mochange.co',
            # 'Origin': 'https://mochange.mohist.com.tw',
            # 'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochanji.com',
            # 'Upgrade-Insecure-Requests': '1',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '54',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://mochange.mohist.com.tw',
            'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochanji.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',

        }

    elif computer == 'debbieS':
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.813832450.1563535954; PHPSESSID=5ds1iobsb93pki8deb6r1d0j01; _gid=GA1.2.1376374077.1572513755; _fbp=fb.1.1572513755454.1839800735; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://mochange.mohist.com.tw',
            'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochanji.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',

        }
    elif computer == 'asus':
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'PHPSESSID=jdn2ik3190r8siralp67t6nus6; _ga=GA1.2.1571955753.1573874185; _gid=GA1.2.827395808.1573874185; _fbp=fb.1.1573874187509.1049686961; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://mochange.mohist.com.tw',
            'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochanji.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',



        }
    elif computer == 'pigpig':
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.203279062.1562989751; PHPSESSID=78tjrt78s5ijrlgbe7i8uvelf5; _gid=GA1.2.576081831.1575105621; _fbp=fb.1.1575105621920.719247802; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://mochange.mohist.com.tw',
            'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochanji.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }





    payload = {
        'from_socail_community': 'y',
        'account_ID': email
    }



    try:
        result = session_requests.post(login_url, data = payload, headers = login_headers)
        if result.status_code == requests.codes.ok:
            print("### login  Success! ###", login_url)
            html_context = BeautifulSoup(result.text, 'html.parser')
            # print('html_context: ', html_context)
            loginResult = html_context.find_all('script', type='')
            print('loginResult: ', loginResult[0].text)

            # print(loginResult[0])
            print("login  success!")
            loginResult = True

        else:
            print("login  Fail!", login_url)
            loginResult = False
    except ConnectionError:
        loginResult = False
        print('Connection error')
    except ReadTimeout:
        loginResult = False
        print('Time out')
    return loginResult
# 加入購物車
def AddCart(id,num):
    url = 'https://www.mochange.co/products/add_to_cart.php'
    headers = {
        # 'Accept': '*/*',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Origin': 'https://www.mochange.co',
        # 'Referer': 'https://www.mochange.co/products/shop_info.php?product_sernum='+num,
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest'

        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '115',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.325354729.1569124814; _gat_gtag_UA_139121893_1=1',
        'Host': 'www.mochange.co',
        'Origin': 'https://www.mochange.co',
        'Referer': 'https://www.mochange.co/products/shop_info.php?product_sernum=' + num,
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    payload = {
        'product_sernum': num,
        'account_id': id,
        'set_number': '1',
        'pay_way': '2',
        'vip_rating': '4'

    }



    try:
        result = session_requests.post(url, data = payload, headers = headers)
        if result.status_code == requests.codes.ok:
            print("id: ", id, "加入購物車 URL Success!", url)
        else:
            print("加入購物車 URL Fail!", url)
    except ConnectionError:
        print('Connection error')
    except requests.exceptions.ConnectionError as e:
        print('requests.exceptions.ConnectionError, e=', str(e))
    except ReadTimeout:
        print('Time out')
#清空購物車
def ClearCart(id):
    url = 'https://www.mochange.co/cart/clear_cart.php'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.mochange.co',
        'Referer': 'https://www.mochange.co/cart/cart.php',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    payload = {
        'account_id': id
    }


    try:
        result = session_requests.post(url, data = payload, headers = headers)
        if result.status_code == requests.codes.ok:
            print("清空購物車  Success!", url)
        else:
            print("清空購物車  Fail!", url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')
#付款
def Payment_legancy(id):
    url = 'https://www.mochange.co/cart/check_ProdNum.php'

    if id == 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=':
        content_length = '61'
        TransKey = 'OMd1SsifFW363CWpms7e632I6BLgJYIANta4alb7Cdc='
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    elif id == 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=':
        content_length = '57'
        # karenwang's cookie
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    elif id == 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=':
        content_length = '61'
        # chctrader's cookie
        cookie = 'PHPSESSID=vl8far634jeqeg99g0tf4u2465; _ga=GA1.2.1907774147.1566182733; _gid=GA1.2.31664247.1566182733; _fbp=fb.1.1566182733412.864437514; _gat_gtag_UA_139121893_1=1'
    elif id == '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=':
        content_length = '63'
        # karenwang's cookie
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'

    print("id: ", id)
    print("content_length: ", content_length)
    print("cookie: ", cookie)


    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': content_length,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'www.mochange.co',
        'Origin': 'https://www.mochange.co',
        'Referer': 'https://www.mochange.co/cart/payment.php',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'

    }
    payload = {
        'account_id': id
    }



    try:
        result = session_requests.post(url, data = payload, headers = headers)
        if result.status_code == requests.codes.ok:
            print("付款  Success!", url)
            print('pay result:', result.content)

            process_url = 'https://www.mochange.co/cart/ProcessTransData.php'

            procell_headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '55',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': cookie,
                'Host': 'www.mochange.co',
                'Origin': 'https://www.mochange.co',
                'Referer': 'https://www.mochange.co/cart/payment.php',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

                # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
                # Accept-Encoding: gzip, deflate, br
                # Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
                # Cache-Control: max-age=0
                # Connection: keep-alive
                # Content-Length: 55
                # Content-Type: application/x-www-form-urlencoded
                # Cookie: PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.1080974198.1570156735; _gat_gtag_UA_139121893_1=1
                # Host: www.mochange.co
                # Origin: https://www.mochange.co
                # Referer: https://www.mochange.co/cart/payment.php
                # Sec-Fetch-Mode: navigate
                # Sec-Fetch-Site: same-origin
                # Sec-Fetch-User: ?1
                # Upgrade-Insecure-Requests: 1
                # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

            }

            process_payload = {
                'TransKey': 'OMd1SsifFW363CWpms7e632I6BLgJYIANta4alb7Cdc='
            }


            try:
                process_result = session_requests.post(process_url, headers = procell_headers)
                print('pay result 2:', process_result.content)

                if process_result.status_code == requests.codes.ok:
                    print("付款程序  Success!", process_url)
                else:
                    print("付款程序  Fail!", process_url)
            except ConnectionError:
                print('Connection error')
            except ReadTimeout:
                print('Time out')

        else:
            print("付款  Fail!", url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')

# if email == 0, not loging to get transkey
def Payment(id, email, computer):

    paymentResult = 'False'
    transKey = None

    #login
    if type(email) == str:
        Login(email,computer)
        print('email login: ', email)

    # get TransKey

    key_url = 'https://www.mochange.co/cart/payment.php'

    if computer == 'mac':
        key_headers = {
            # karen mac
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.1080974198.1570156735',
            'Cookie': '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.1040713635.1582003150',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/cart/cart.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

        }

    elif computer == 'windows':
        key_headers = {

            # llibs windows
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=ft987iase39p75g278r50eb7q6; _gid=GA1.2.749101058.1571282254; _gat_gtag_UA_139121893_1=1',
            # 'Cookie': '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.1040713635.1582003150',
            'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',
            # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/cart/cart.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

        }
    elif computer == 'debbieS':
        key_headers = {
            # debbies computer
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.813832450.1563535954; PHPSESSID=5ds1iobsb93pki8deb6r1d0j01; _gid=GA1.2.1376374077.1572513755; _fbp=fb.1.1572513755454.1839800735; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://www.mochange.co',
            'Referer': 'https://www.mochange.co/cart/cart.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        }
    elif computer == 'asus':
        key_headers = {
            # debbies computer
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=jdn2ik3190r8siralp67t6nus6; _ga=GA1.2.1571955753.1573874185; _gid=GA1.2.827395808.1573874185; _fbp=fb.1.1573874187509.1049686961; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://www.mochange.co',
            'Referer': 'https://www.mochange.co/cart/cart.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
    elif computer == 'pigpig':
        key_headers = {
            # debbies computer
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.203279062.1562989751; PHPSESSID=78tjrt78s5ijrlgbe7i8uvelf5; _gid=GA1.2.576081831.1575105621; _fbp=fb.1.1575105621920.719247802; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Origin': 'https://www.mochange.co',
            'Referer': 'https://www.mochange.co/cart/cart.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }






    try:
        result = session_requests.get(key_url, headers = key_headers)
        print('### get TransKey page ###')
        # print(result.text)
        html_context = BeautifulSoup(result.text, 'html.parser')
        transKeyContext = html_context.find_all('input', type='hidden')
        # print(transKeyContext)
        idInfo = transKeyContext[0].get('value')
        transKey = transKeyContext[2].get('value')
        print('### Id ###: ', idInfo)
        print('### TransKey ###: ', transKey)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')


    url = 'https://www.mochange.co/cart/check_ProdNum.php'

    if id == 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=':
        content_length = '61'
        # cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
        cookie = '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.93618663.1582430731'
    elif id == 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=':
        content_length = '57'
        # karenwang's cookie
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    elif id == 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=':
        content_length = '61'
        # chctrader's cookie
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    elif id == '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=':
        content_length = '63'
        # karenwang's cookie
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    elif id == 'Knnjqe9jKT8z0Kp1XzNoT3wSmoqDggIhtnNuFLUalMs=':
        content_length = '57'
        cookie = 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1'
    print("id: ", id)
    # print("content_length: ", content_length)
    # print("cookie: ", cookie)


    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': content_length,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'www.mochange.co',
        'Origin': 'https://www.mochange.co',
        'Referer': 'https://www.mochange.co/cart/payment.php',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'


    }
    payload = {
        'account_id': id
    }



    try:
        # result = session_requests.get(url)
        # tree = html.fromstring(result.text)
        # soup = BeautifulSoup(result.text, 'html.parser')
        # print('## pay result ##:', result.content)
        # print('## check get RESULT ##', result.text)
        # print('## check get RESULT html fromstring ##', tree)
        # print('## html.parser', soup)
        result = session_requests.post(url, data = payload, headers = headers)
        if result.status_code == requests.codes.ok:
            print('### pay result ###:', result.text)
            if result.text == 'n':
                print('Nothing To Pay!!!')
            else:
                print("!!付款  中!!!", url)
                print("付款  check Success!", url)

                process_url = 'https://www.mochange.co/cart/ProcessTransData.php'
                if computer == 'mac':
                    procell_headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '55',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        # 'Cookie': cookie,
                        # 'Cookie': 'PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.309458116.1572321506; _gat_gtag_UA_139121893_1=1',
                        'Cookie': '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.93618663.1582430731',
                        'Host': 'www.mochange.co',
                        'Origin': 'https://www.mochange.co',
                        'Referer': 'https://www.mochange.co/cart/payment.php',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

                    }
                elif computer == 'windows':
                    procell_headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '55',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        # 'Cookie': cookie,
                        # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=ft987iase39p75g278r50eb7q6; _gid=GA1.2.749101058.1571282254; _gat_gtag_UA_139121893_1=1',
                        'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',
                        'Host': 'www.mochange.co',
                        'Origin': 'https://www.mochange.co',
                        'Referer': 'https://www.mochange.co/cart/payment.php',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

                    }

                elif computer == 'debbieS':
                    procell_headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '55',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        # 'Cookie': cookie,
                        'Cookie': '_ga=GA1.2.813832450.1563535954; PHPSESSID=5ds1iobsb93pki8deb6r1d0j01; _gid=GA1.2.1376374077.1572513755; _fbp=fb.1.1572513755454.1839800735; _gat_gtag_UA_139121893_1=1',
                        'Host': 'www.mochange.co',
                        'Origin': 'https://www.mochange.co',
                        'Referer': 'https://www.mochange.co/cart/payment.php',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',

                    }
                elif computer == 'asus':
                    procell_headers = {

                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '55',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        # 'Cookie': cookie,
                        'Cookie': 'PHPSESSID=jdn2ik3190r8siralp67t6nus6; _ga=GA1.2.1571955753.1573874185; _gid=GA1.2.827395808.1573874185; _fbp=fb.1.1573874187509.1049686961; _gat_gtag_UA_139121893_1=1',
                        'Host': 'www.mochange.co',
                        'Origin': 'https://www.mochange.co',
                        'Referer': 'https://www.mochange.co/cart/payment.php',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',

                    }
                elif computer == 'pigpig':
                    procell_headers = {

                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '55',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        # 'Cookie': cookie,
                        'Cookie': '_ga=GA1.2.203279062.1562989751; PHPSESSID=78tjrt78s5ijrlgbe7i8uvelf5; _gid=GA1.2.576081831.1575105621; _fbp=fb.1.1575105621920.719247802; _gat_gtag_UA_139121893_1=1',
                        'Host': 'www.mochange.co',
                        'Origin': 'https://www.mochange.co',
                        'Referer': 'https://www.mochange.co/cart/payment.php',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

                    }



                process_payload = {
                    'TransKey': transKey
                }




                try:
                    process_result = session_requests.post(process_url, data = process_payload, headers = procell_headers)
                    print('pay result 2:', process_result.content)
                    print('## process RESULT ##', process_result.text)


                    paymentResult = process_result.text
                    str_notEnought = '庫存不足'
                    str_buySuccess = '交易成功'
                    if paymentResult.find(str_notEnought) != -1:
                        print('搜尋結果: ', str_notEnought)
                        paymentResult = str_notEnought
                    elif paymentResult.find(str_buySuccess) != -1:
                        print('搜尋結果: ', str_buySuccess)





                    if process_result.status_code == requests.codes.ok:
                        print("付款程序  Success!", process_url)

                    else:
                        print("付款程序  Fail!", process_url)



                except ConnectionError:
                    print('Connection error')
                except ReadTimeout:
                    print('Time out')
        else:
            print("付款  Fail!", url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')


    return paymentResult




# if email == 0, not loging to get transkey
def GetTransKey(email, computer):

    if type(email) == str:
        Login(email, computer)
        print('email login: ', email)



    key_url = 'https://www.mochange.co/cart/payment.php'
    key_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=8dauvv3tblj3qeckov32j8jlt4; _ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; _gid=GA1.2.1080974198.1570156735',
        'Host': 'www.mochange.co',
        'Referer': 'https://www.mochange.co/cart/cart.php',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

    }

    result = session_requests.get(key_url, headers = key_headers)
    print('### get TransKey page ###')
    # print(result.text)
    html_context = BeautifulSoup(result.text, 'html.parser')

    transKeyContext = html_context.find_all('input', type='hidden')
    # print(transKeyContext)
    # # [<input id="account_id" type="hidden" value="fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI="/>, <input id="vip_rating" type="hidden" value="4"/>, <input id="process_key" name="TransKey" type="hidden" value="OMd1SsifFW363CWpms7e669vmP/wbh57qSRjJlYlnG8="/>]
    idInfo = transKeyContext[0].get('value')
    transKey = transKeyContext[2].get('value')
    print('### Id ###: ', idInfo)
    print('### TransKey ###: ', transKey)


#票券清單
def TicketList(email):
    ticket_number = []
    ticket_name = []

    login_url = 'https://www.mochange.co/member_login/member_login.php'

    login_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '59',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1',
        'Host': 'www.mochange.co',
        'Origin': 'https://mochange.mohist.com.tw',
        'Referer': 'https://mochange.mohist.com.tw/FrontEnd/member_login/Google_Login.php?domain=www.mochange.co',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    payload = {
        'from_socail_community': 'y',
        'account_ID': email
    }



    try:
        result = session_requests.post(login_url, data = payload, headers = login_headers)
        if result.status_code == requests.codes.ok:
            print("login  Success!", login_url)
        else:
            print("login  Fail!", login_url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')






    url = 'https://www.mochange.co/member_overview/member_ticket.php'
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257',
    #     'Host': 'www.mochange.co',
    #     'Referer': 'https://www.mochange.co/member_overview/member_overview.php',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    # }
    #
    # result = session_requests.get(url, headers = headers)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '56',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257; _gat_gtag_UA_139121893_1=1',
        'Host': 'www.mochange.co',
        'Origin': 'https://www.mochange.co',
        'Referer': 'https://www.mochange.co/member_overview/member_ticket.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    payload = {
        'time_validation': 'undefined',
        'ticket_status': 'unused',
        'top_cate':''
    }

    try:
        result = session_requests.post(url, data = payload, headers = headers)


        if result.status_code == requests.codes.ok:
            print("票券清單  Success!", url)

            html_context = BeautifulSoup(result.text, 'html.parser')
            # print('html_context=', html_context)
            stories = html_context.find_all('div', class_='name')
            stories_id = html_context.find_all('div', class_='type color023997')
            # print('stories= ', stories)
            for i in range(len(stories)):
                # 新聞標題
                print(stories_id[i].text + " " + stories[i].text)
                ticket_number.append(stories_id[i].text)
                ticket_name.append(stories[i].text)
        else:
            print("票券清單  Fail!", url)
        # print('TicketList= ', ticket_list)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')


    return ticket_number, ticket_name




# 購物車清單
def CartList(email, computer):
    print('function CarList mail: ', email)

    cart_list = []
    Login(email, computer)

    url = 'https://www.mochange.co/cart/cart.php'


    if computer == 'mac':
        headers = {
            # # karen mac
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.249788333.1567947916; _fbp=fb.1.1567947917202.1321095142; PHPSESSID=3psvbgn213e05rvcfkep1dlp85; _gid=GA1.2.1040713635.1582003150',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/index/index.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'


        }

    elif computer == 'windows':
        headers = {
            # llibs windows
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=ft987iase39p75g278r50eb7q6; _gid=GA1.2.749101058.1571282254; _gat_gtag_UA_139121893_1=1',
            'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/index/index.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

            # 'Cookie': '_ga=GA1.2.418205730.1557802358; _fbp=fb.1.1557802358417.1269756375; PHPSESSID=sqtjeplfhvnnhq3nspbltd42b7; _gid=GA1.2.1497596523.1581836286; _gat_gtag_UA_139121893_1=1',

        }

    elif computer == 'debbieS':
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.813832450.1563535954; PHPSESSID=5ds1iobsb93pki8deb6r1d0j01; _gid=GA1.2.1376374077.1572513755; _fbp=fb.1.1572513755454.1839800735; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/index/index.php',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',

        }
    elif computer == 'asus':
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=jdn2ik3190r8siralp67t6nus6; _ga=GA1.2.1571955753.1573874185; _gid=GA1.2.827395808.1573874185; _fbp=fb.1.1573874187509.1049686961; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/index/index.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
    elif computer == 'pigpig':
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.203279062.1562989751; PHPSESSID=78tjrt78s5ijrlgbe7i8uvelf5; _gid=GA1.2.576081831.1575105621; _fbp=fb.1.1575105621920.719247802; _gat_gtag_UA_139121893_1=1',
            'Host': 'www.mochange.co',
            'Referer': 'https://www.mochange.co/index/index.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }





    try:
        result = session_requests.get(url, headers = headers)


        if result.status_code == requests.codes.ok:
            print("購物清單  Success!", url)

            html_context = BeautifulSoup(result.text, 'html.parser')
            # print('html_context=', html_context)
            stories = html_context.find_all('div', class_='name')
            for s in stories:
                # 新聞標題
                cart_list.append(s.text)
                print("標題：" + s.text)
        else:
            print("購物清單  Fail!", url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')

    return cart_list

# 首頁商品：
    # 名稱
    # 商品連結
    # 照片連結
    # 商品描述
    # 原始價格
    # VIP2 價格
def ShowFrontPageList(vip_level):

      # a = [{'Name': '北投【春天酒店】單人泡湯劵MO',
      #       'Link': 'https://www.mochange.co//products/shop_info.php?product_sernum=337',
      #       'Picture': 'https://stage.mohist.com.tw/Mobuy/BackEnd/images/UpoladImage/20190413195059_ca7d6.jpg',
      #       'Original Price': '$900',
      #       'VIP2 Price': '391',
      #       'Attention': '※票券上銀行信託期限至2019/12/07，並非使用期限，本票券優惠期限為【2020年3月31日，逾期後不得要求提供原優惠，但仍可依其面額折抵$400元】。※本賣場票券為專案採購，載明之面額為【$400元】，不等同於本賣場零售價，無法接受者請勿購買。※如有退貨問題須於鑑賞期內聯絡原購買單位，逾鑑賞期恕不受理。1.本券限乙人使用,可享室內湯屋1小時或露天風呂(二擇一)。2.加碼:4至9月期間使用湯屋,加贈延長30分鐘。3.本券不分平/假日皆可使用,平/假日定義依飯店公告為主。4.室內湯屋24小時開放,泡湯皆須現場劃位,恕不提供電話預約;露天風呂營業時間09:00~22:00需著泳裝、泳帽入場(限進出一次)。5.本券一經使用恕不退換。6.本券發售時己開立統一發票,使用時不再開立統一發票。7.本商品不得與其他優惠方案合併使用,若塗改、偽造及翻印均屬無效。【使用注意事項】◎  不得與其他優惠合併使用，恕無法兌換現金及找零◎  請持手機簡訊或列印e-mail兌換券到店使用◎  兌換券逾期未使用，可辦理退費。以上規範如與兌換券不同，則依兌換券為準。春天酒店電話:(02)2897-5555地址:台北市北投區幽雅路18號'}]

    Production_info = []



    url = 'https://www.mochange.co/index/index.php'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257',
        'Host': 'www.mochange.co',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }


    result = session_requests.get(url, headers = headers)
    if result.status_code == requests.codes.ok:




        front_page_url = 'https://www.mochange.co/'
        print("Get Front Page  Success!", url)

        html_context = BeautifulSoup(result.text, 'html.parser')
        # print('html_context=', html_context)

        item_link = html_context.select('a[href^="../products/shop_info.php?"]')
        item_name = html_context.find_all('div', class_='name1 new_word')
        photo_link = html_context.find_all('img', class_='lazy')
        ori_price_text = html_context.find_all('span', class_='grayprice font12')
        # print('shop_itme= ', shop_itme)
        # print('item_link= ', item_link)
        # print('item_name= ', item_name)
        # print('photo_link= ', photo_link)

        for i in range(len(item_name)):
            name = item_name[i].text
            link = front_page_url + item_link[i].get('href')[2:len(item_link[i].get('href'))]
            phto = photo_link[i].get('src')
            ori_price = ori_price_text[i].text
            print('名稱：' + name)
            print('商品連結：' + link)
            print('照片連結：' + phto)
            print('原價：' + ori_price)

            # 商品描述
            # vip2價格
            # 注意事項

            item_headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257',
                'Host': 'www.mochange.co',
                'Referer': 'https://www.mochange.co/index/index.php',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
            }

            item_result = session_requests.get(link, headers = item_headers)
            if item_result.status_code == requests.codes.ok:

                print("Get Item Page  Success!", link)
                item_html_context = BeautifulSoup(item_result.text, 'html.parser')

                vip_price = item_html_context.find_all('div', class_='name2 wd100mo price2')
                attention = item_html_context.find_all('div', class_='info')
                # print('vip_price= ', vip_price)
                for i in range(len(vip_price)):
                    # print('vip_price' + str(i) + ': ', vip_price[i].text)
                    if i == vip_level:
                        vip2_price = vip_price[i].text[2:len(vip_price[i].text)]

                print('VIP2 價格 = ', vip2_price)

                attention_info = attention[2].text.strip().replace('\n', "").replace('\r', "").replace('\t', "" ).replace('\xa0', "") + attention[3].text.strip().replace('\n', "").replace('\r', "").replace('\t', "" ).replace('\xa0', "") + attention[4].text.strip().replace('\n', "").replace('\r', "").replace('\t', "" ).replace('\xa0', "")

                print('注意事項: ', attention_info)

                Production_info.append({'Name':name, 'Link':link, 'Picture':phto, 'Original Price': ori_price, 'VIP2 Price':vip2_price, 'Attention':attention_info})

            else:
                print("Get Item Page  Fail!", link)

    else:
        print("Get Front Page  Fail!", url)


    return Production_info

# # 批量購買票券
# 加購物車
# 付款(option)
# 清空購物車(option with payment)
def BuyTicket(id, email, item_List, loop_flag, only_add_flag, computer):
    if loop_flag == True:
        while True:
            for item_num in item_List:
                print('Item Num: ', item_num, 'id: ', id)
                if only_add_flag:
                    AddCart(id,item_num)
                    print('========ADD=========')
                else:
                    AddCart(id,item_num)
                    Payment(id, email, computer)
                    ClearCart(id)
                    print('========BUY=========')

    else:
        for item_num in item_List:
            print('Item Num: ', item_num, 'id: ', id)
            if only_add_flag:
                AddCart(id,item_num)
                print('========ADD=========')
            else:
                AddCart(id,item_num)
                Payment(id, email, computer)
                ClearCart(id)
                print('========BUY=========')


def OnlyAdd(id, email, item_List, loop_flag):
    if loop_flag == True:
        while True:
            for item_num in item_List:
                print('Item Num: ', item_num)
                AddCart(id,item_num)
                print('========ADD=========')
    else:
        for item_num in item_List:
            print('Item Num: ', item_num)
            AddCart(id,item_num)
            print('========ADD=========')

# 顯示商品狀態
def CheckItemStatus(num):

    ItenStatus = 'None'
    url = 'https://www.mochange.co/products/shop_info.php?product_sernum=' + num

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=abt6qj1bprtn03n3hl70obcbe4; _ga=GA1.2.1901514088.1561195421; _fbp=fb.1.1561195421075.1690105961; _gid=GA1.2.2023715889.1562558257',
        'Host': 'www.mochange.co',
        'Referer': 'https://www.mochange.co/point/point.php',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    payload = {
        'product_sernum': num
    }

    try:
        result = session_requests.get(url, headers = headers)


        if result.status_code == requests.codes.ok:
            print("Check Iten  Success!", url)

            html_context = BeautifulSoup(result.text, 'html.parser')
            # print('html_context=', html_context)
            stories = html_context.find_all('button', class_='buy_btn mgt30 fr')
            for s in stories:
                # 新聞標題
                ItenStatus = s.text
                # print("商品狀態：" + s.text)
        else:
            print("Check Iten  Fail!", url)
    except ConnectionError:
        print('Connection error')
    except ReadTimeout:
        print('Time out')
    return ItenStatus

def ShowPointItemNum():
    Item_Num = []
    url = 'https://www.mochange.co/point/point.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=vl8far634jeqeg99g0tf4u2465; _ga=GA1.2.1907774147.1566182733; _fbp=fb.1.1566182733412.864437514; _gid=GA1.2.1498526786.1567307556',
        'Host': 'www.mochange.co',
        'Referer': 'https://www.mochange.co/index/index.php',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    result = session_requests.get(url, headers = headers)
    if result.status_code == requests.codes.ok:
        print("Get Point Front Page  Success!", url)

        html_context = BeautifulSoup(result.text, 'html.parser')
        item_link = html_context.select('a[href^="../products/shop_info.php?"]')
        for link in item_link:
            link_temp = link.get('href')[2:len(link.get('href'))].split('=')[1]
            print('link: ', link_temp)

            Item_Num.append(link_temp)

    else:
        print("Get Point Front Page  Fail!", url)

    return Item_Num

def ShowPointInventory():
    Item_Num = []
    Item_Status = []

    url = 'https://www.mochange.co/point/point.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=vl8far634jeqeg99g0tf4u2465; _ga=GA1.2.1907774147.1566182733; _fbp=fb.1.1566182733412.864437514; _gid=GA1.2.1498526786.1567307556',
        'Host': 'www.mochange.co',
        'Referer': 'https://www.mochange.co/index/index.php',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    result = session_requests.get(url, headers = headers)
    if result.status_code == requests.codes.ok:
        print("Get Point Front Page  Success!", url)

        html_context = BeautifulSoup(result.text, 'html.parser')
        item_link = html_context.select('a[href^="../products/shop_info.php?"]')
        # token_link = html_context.find_all('svg', class_='svg-inline--fa fa-gg-circle fa-w-16')
        # produc_status = item_link.find_all('div', class_='circle')


        for link in item_link:
            link_temp = link.get('href')[2:len(link.get('href'))].split('=')[1]
            produc_temp = link.find('div', class_='circle')
            if produc_temp == None:
                produc_temp = '有'
            else:
                produc_temp = produc_temp.text


            print('link: ', link_temp)
            print('status: ', produc_temp)


            Item_Num.append(link_temp)
            Item_Status.append(produc_temp)

    else:
        print("Get Point Front Page  Fail!", url)

    return Item_Num, Item_Status

def InventoryWrite2File(loop_flag, file_name):

    [num, status] = ShowPointInventory()
    for i in range(len(num)):
        fp=open(file_name, 'a')
        if fp !=None:
            fp.write(num[i] + ' ')
            fp.write(status[i] + '\n')
        fp.close()

    fp=open(file_name, 'a')
    if fp !=None:
        fp.write('======================================' + '\n')
    fp.close()

    while loop_flag:
        [num, status] = ShowPointInventory()
        for i in range(len(num)):
            fp=open(file_name, 'a')
            if fp !=None:
                fp.write(num[i] + ' ')
                fp.write(status[i] + '\n')
            fp.close()

        fp=open(file_name, 'a')
        if fp !=None:
            fp.write('==================================' + '\n')
        fp.close()
