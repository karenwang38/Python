import random

# 0:隨機地點產生英文例句
# 1:輸入地點產生英文
# 2: other
Mode = 0
location_list = {'台北市':{'台北101':['Taipei 101 will hold a fireworks show during the New Year\'s Eve','跨年的時候台北101會舉辦煙火秀'],
                          '國立故宮博物院':['National plalce museum is one of the eight scenic spots in Taiwan','國家宮殿博物館是台灣八大景區之一'],
                          '陽明山國家公園':['It is most comfortable to have a hot spring here in winter!','冬天這裡有溫泉最舒服'],
                          '西門町':['Here is where young people like to come.','這裡是年輕人喜歡來的地方。'],
                          '中正紀念堂':['In addition to people’s leisure, it is often a venue for large-scale arts and cultural events, often holding exhibitions.','除了人們的休閒活動外，它還經常舉辦大型藝術和文化活動，經常舉辦展覽。']},
                '新北市':{'九份':['Jiufen taro ball  is very delicious!','九份芋圓非常好吃'],
                        '野柳風景特定區':['One of the premier destinations in northern Taiwan, Yehliu Geopark is home to a number of unique geological formations including the iconic "Queen\'s Head"','野柳風景特定區是台灣北部的首要目的地之一，擁有眾多獨特的地質構造，包括標誌性的“女王頭”'],
                        '艋舺龍山寺':['It is most comfortable to have a hot spring here in winter!','冬天這裡有溫泉最舒服'],
                        '十分瀑布':['Shihfen Waterfall falls about 20 meters high, very spectacular','十分瀑布高約20米，非常壯觀'],
                        '金瓜石':['JinGuaShih shrine, here is a must for photography enthusiasts','金瓜石神社啦，這裡可是攝影愛好者的必來之處']}}
City_list = list(location_list.keys())


#print(location_list)
if Mode==0:
    City_idx = random.choice(range(len(location_list)))

    Position_idx = random.choice(range(len(location_list[City_list[City_idx]])))
    position_list = list(location_list[City_list[City_idx]].keys())
    '''
    print ("City_list =", City_list)
    print("City_idx =", City_idx)
    print("Position_idx =", Position_idx)
    print("position_list =", position_list)
    print("你要去",City_list[City_idx],"的",position_list[Position_idx])
    print("你要學的英文是：\n",location_list[City_list[City_idx]][position_list[Position_idx]][0],
                         "\n",location_list[City_list[City_idx]][position_list[Position_idx]][1])
    '''
    
    text = ["你要去"+City_list[City_idx]+"的"+position_list[Position_idx]+"\n""你要學的英文是： "
            +location_list[City_list[City_idx]][position_list[Position_idx]][0]
            +"("+location_list[City_list[City_idx]][position_list[Position_idx]][1]+")"]
    print(text[0])
elif Mode == 1:
    # 輸入地址、返回英文例句
    while True:
        position_exit = False
        user_input = input('你的所在地：')
        #search english
        for city in location_list:
            #print(city)
            #print(location_list[city],'\n\n')
            for position in location_list[city]:
                if user_input in location_list[city]:
                    print('\n=======',user_input,'=============')
                    print(location_list[city][user_input][0],location_list[city][user_input][1])
                    print('====================\n')
                    position_exit = True
                    break
            if position_exit:
                break
        if position_exit != True:
            print('\n=======',user_input,'=============')
            print('世界上沒這個地方')
            print('==================================\n')
