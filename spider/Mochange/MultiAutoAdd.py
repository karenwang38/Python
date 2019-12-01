from MoChange import *
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing as mp
import time
import math

print('process number:', mp.cpu_count())

idList = ['+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=',  # chctrader001
          'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=',  # llibs38
          'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=',  # karenwang38
          'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='   # chctrader
          'Knnjqe9jKT8z0Kp1XzNoT3wSmoqDggIhtnNuFLUalMs=']  # diabloiiiblizzard
# idList = ['fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=']

def f(x):
    return x*x

def AccountAdd(id):
    ###################################  initial parameter
    email = 'llibs38@gmail.com' # only for payment
    computer = 'mac' # only for payment

    # itmeList = ['200044', '747', '750', '759', '624', '626', '628', '527', '509', '531', '593', '597', '683', '200200']
    itemList = ['200216',           # 台中商旅【CHEZ HUNG】異國百匯假日午餐吃到飽一客 (含現煎台)
                '200219',           # 台中商旅【CHEZ HUNG】異國百匯平日午餐吃到飽一客 (含現煎台)
                '200200',           # 【瓏山林台北中和飯店】1F國際酒吧-午間或晚間單人套餐券
                '200197',           # 台北【優兒親子教育集團】體驗優兒BBS統整遊戲課程一堂 (共100分鐘)
                '200188',           # 台中【沙夏汽車旅館】不限房型雙人3H休息券
                '200183',           # 【奇蹟莊園Med+Space體驗所】SPA芳療體驗劵 (平假日皆可使用)
                '200180',           # 台北【總裁牛肉麵】晶贊總裁牛肉麵乙碗
                '200075',           # 【台北城大飯店】超值午間套餐券-每日限量主廚鳳梨牛肉麵
                '200177',           # 成旅晶贊飯店-台中民權【晶贊粵菜廳】早午餐吃到飽一客
                '200057',           # 【麥茵茲纖體美塑沙龍】纖纖細腿美臀翹+純手技排導舒壓-限女性使用 (全台分店適用)
                '200055',           # 麥茵茲纖體美塑沙龍】膠原激增緊緻仿真電波UPUP (全台分店適用)
                '200120',           # 台中【心驛旅館】異國風情客房雙3H休息券
                '200076',           # 【台北城大飯店】超值午間套餐券-黑玉燉肉飯
                '200024',           # 台北【立德Cafe83餐廳-國父紀念館】平日單人午晚餐吃到飽一客
                '200021',           # 台北【立德Cafe83餐廳-國父紀念館】平日單人下午茶吃到飽一客
                '200054',           # 【麥茵茲纖體美塑沙龍】瞬效Q彈無暇蛋白殼美肌 (全台分店適用)
                '200056',           # 【麥茵茲纖體美塑沙龍】手技鬆筋舒壓+纖體甩油燃脂-限女性使用 (全台分店適用)
                '507',              # 台北新板希爾頓酒店【逸廊】下午茶雙人套餐券
                '560',              # 烏來【山之川溫泉會館】大眾裸湯+單人下午茶點 (1張) 平假日皆可★
                '561',              # 台中【水舞系列-麗緹旅館】不限房型休息券K00405
                '593',              # 【100％紐西蘭黃金奇異果汁】2入組 (已含宅配60元運費)
                '620',              # 【宜蘭力麗威斯汀度假酒店】CAFÉ LOUNGE雙人下午茶(不分平假日)
                '626',              # 台中【黑牛炭火岩燒牛排】雙拼套餐安格斯板腱牛排(4盎司)拚多利魚
                '628',              # 台中【黑牛炭火岩燒牛排】蒜尼狠-蒜味平鐵牛排(10盎司)
                '683',              # 台北【一号基地炭火食堂】平日串燒盛合+啤酒抵用券
                '709',              # 澎湖福朋喜來登酒店【宜客樂海港自助百匯】晚餐吃到飽單人券
                '795',              # 承億輕旅】平日混合背包房單人床位住宿券MO(嘉義/台南/高雄三館通用)
                '651',              # 台中【LaPizza那間披薩】單人披薩炸物吃到飽 (中興大學商圈聚餐首選)
                '624',              # 台中【黑牛炭火岩燒牛排】雙拼套餐碳烤雞腿排拚多利魚
                '541',              # 礁溪【山泉飯店】田野湯屋90分鐘★
                '542',              # 礁溪【山泉飯店】星辰湯屋90分鐘★
                '539',              # 北投【水都溫泉會館】客房泡湯120 mins
                '538',              # 烏來【山之川溫泉會館】雙人溫馨湯屋1.5H+雙人套餐 (1張) 免預約★
                '536',              # 烏來【山之川溫泉會館】大眾裸湯+單人套餐 (1張) 平假日皆可，免預約
                '535',              # 烏來【驛站溫泉會館】豪華房雙人湯屋1.5小時+雙人義大利麵 (1張)
                '534',              # 烏來【驛站溫泉會館】豪華房雙人湯屋1.5小時+雙人下午茶 (1張)★
                '533',              # 烏來【泉世界溫泉會館】雙人套房 休息泡湯券(1張)★
                '531',              # 礁溪【鳳凰德陽川泉旅】蘭陽在地美食百匯吃到飽+泡湯★
                '530',              # 宜蘭礁溪泉鄉風華雙人湯屋90分鐘-平日泡湯券 (1張)
                '522',              # 台中【水舞系列-麗心旅館】不限房型休息券K00450
                '517',              # 台中【水舞系列-湖水岸旅館】 蝶舞A套房休息券K00540
                '516',              # 台中【水舞行館】花舞套房休息券(1張) K00719
                '512',              # 台中【沐蘭】楓舞A套房休息券K00972
                '514',              # 台北【沐蘭】雲舞套房休息券(1張) K001296
                '509',              # 台北新板希爾頓酒店【Market Flavor 悅市集】平日自助晚餐或週末自助午餐單人券
                '489',              # 水相餐廳 法式排餐系列 平日限定套餐券
                '488',              # 水相餐廳 單人超值下午茶 假日不加價
                '383',              # 烏來【山之川溫泉會館】雙人溫馨湯屋1.5H+雙人下午茶點 (1張)★
                '382',              # 烏來東風溫泉會館 雙人湯屋+下午茶 平假日皆可用★
                '364',              # 【水舞饌-崇德店】港式 饌潮流 個人套餐 K00495
                ]
    LiveList = [#'795',              # 承億輕旅】平日混合背包房單人床位住宿券MO(嘉義/台南/高雄三館通用)
                #'804',              # 台北【Come Inn 客盈旅館】背包客棧標準單人床位住宿券
                #'200043',           # 高雄【宮賞藝術大飯店】平日雙人雅致套房一泊一食住宿券 (平日可免費升等房型)
                    ]
    SpaList = [ #'200183',
                '200057',
                '200056',
                '200055',
                '200054',
                '560',
                #'542',
                #'541',
                '539',
                '538',
                '536',
                '535',
                '534',
                '533',
                '531',
                '530',
                '383',
                '382',
                ]
    MealList = ['512',
                '514',
                '516',
                '200021',
                '200024',
                '200075',
                '200076',
                '200177',
                '628',
                '651',
                '683',
                '709',
                '539',
                '200120',
                '200188',
                '200272',
                '200303',
                '200293',
                '200296',
                '200318',
                '200284',
                '200287',
                '200180',
                '200216',
                '200219',
                '200280',
                '364',
                '531',
                '624',
                '626',
                '200336',
                '517',
                '522',
                '561',
                ]



    time_flag = True

    time_period = 4 # min
    # 1 min = 60 sec = 60*60 micro sec

    run_time = 1570420680 # 20191006 11:58
    sleeptime = 0 # min
    onlyAdd = True

    num = round(len(MealList)/4)
    print('## MealList: ', MealList)


    if id == '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=':    # chctrader001
        # AddList = LiveList + SpaList
        AddList = [ '512',
                    '514',
                    '516',
                    '539',
                    '200120',
                    '200188',
                    '200272',
                    '200303',
                    '200293',
                    '200296',
                    '200318',
                    '200284',
                    '200287',]
    elif id == 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=':  # llibs38
        # AddList = MealList + LiveList + SpaList
        AddList = MealList
    elif id == 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=':  # chctrader
        # AddList = MealList[:9]
        AddList = [ '512',
                    '514',
                    '516',
                    '200021',
                    '200024',
                    '200075',
                    '200076',
                    '200177',
                    '628',
                    '651',
                    '683',
                    '709',]
    elif id == 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=':  # karenwang38
        # AddList = MealList
        AddList = [ '512',
                    '514',
                    '516',
                    '200180',
                    '200216',
                    '200219',
                    '200280',
                    '364',
                    '531',
                    '624',
                    '626',
                    '200336',]
    elif id == 'Knnjqe9jKT8z0Kp1XzNoT3wSmoqDggIhtnNuFLUalMs=': # diabloiiiblizzard
        AddList = [ '512',
                    '514',
                    '516',
                    '683',
                    '531',
                    '200336',
                    '517',
                    '522',
                    '561',]
    ###################################  initial parameter
    # print('id:', id)
    print('id:', id, '\nAddlist= ', AddList)

    if onlyAdd == False:
        Login(email)

    if time_flag:
        # 檢查是否要開始
        while time_flag:
            now = time.time()
            print('### Not Start Runing ###')
            #開始後有時間限制！
            start_time = time.time()
            while now - run_time > 0:
                end_time = time.time()
                print('start_time: ', start_time)
                print('end_time: ', end_time)
                print('start - end: ', end_time - start_time)
                print('check time: ', time.asctime( time.localtime(end_time) ))
                print('=============time count===============', end_time - start_time)
                print('===================')
                print('===================')
                print('===================')
                if (end_time - start_time) <= (time_period*60):
                    print('購買票券...')
                    BuyTicket(id, 0, AddList, False, onlyAdd, computer)
                else:
                    print('停止購買。')
                    time_flag = False
                    break
                #time.(3)
            if time_flag == False:
                break
            # time.(time*60)
    else:
        BuyTicket(id, email, AddList, False, onlyAdd, computer)


if __name__ == '__main__':
    p = Pool(5) # 建立有5個程序的程序池
    # print(p.map(f, [2,4,6])) # 將f函式的操作給程序池
    print(p.map(AccountAdd, idList))

# def f(name,age):
#     print ('hello', name, age)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',2)) # p程序執行f函式，引數為'bob'，注意後面的“,”
#     p.start() # 程序開始
#     p.join() # 阻塞主執行緒，直至p程序執行結束
