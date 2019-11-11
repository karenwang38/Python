from tokokSearch import *
from tokokAccount import *


def nexOperarion(debug):
    ### 比特、以太的 usdt 成交價
    eth_usdtPrice_Result = TradeHistory('eth_usdt', 1)
    btc_usdtPrice_Result = TradeHistory('btc_usdt', 1)

    # 取資料成功
    if (eth_usdtPrice_Result != False) & (btc_usdtPrice_Result != False):
        eth_usdtPrice = float(eth_usdtPrice_Result[0]['price'])
        btc_usdtPrice = float(btc_usdtPrice_Result[0]['price'])

    else:
        eth_usdtPrice = 0
        btc_usdtPrice = 0
    print('eth_usdtPrice= ', eth_usdtPrice)
    print('btc_usdtPrice= ', btc_usdtPrice)
    ### 比特、以太的 usdt 成交價

    ###幣對以太、比特內外盤價格（換成usdt)
    token = ['nex_eth', 'nex_btc']

    while True:

        base01_sell_depth, base01_buy_depth = MarketDepth(token[0], 1)
        base02_sell_depth, base02_buy_depth = MarketDepth(token[1], 1)


        token_buyPrice_eth = float(base01_buy_depth[0][0])
        token_sellPrice_eth = float(base01_sell_depth[0][0])
        token_buyPrice_btc = float(base02_buy_depth[0][0])
        token_sellPrice_btc = float(base02_sell_depth[0][0])



        token_buyPrice_eth_doubleCheck, token_sellPrice_eth_doubleCheck = TokenPrice(token[0])
        token_buyPrice_btc_doubleCheck, token_sellPrice_btc_doubleCheck = TokenPrice(token[1])

        priceArray = [token_buyPrice_eth, token_sellPrice_eth, token_buyPrice_btc, token_sellPrice_btc]
        priceArray_doubleCheck = [token_buyPrice_eth_doubleCheck, token_sellPrice_eth_doubleCheck, token_buyPrice_btc_doubleCheck, token_sellPrice_btc_doubleCheck]

        print('priceArray= ', priceArray)
        print('priceArray_doubleCheck= ', priceArray_doubleCheck)


        if (priceArray == priceArray_doubleCheck) & (token_buyPrice_eth != token_sellPrice_eth) & (token_buyPrice_btc != token_sellPrice_btc):
            break



    if (token_buyPrice_eth != False) & (token_buyPrice_btc != False) & (token_sellPrice_eth != False) & (token_sellPrice_btc != False):
        token_buyPrice_eth_usdt = token_buyPrice_eth * eth_usdtPrice
        token_sellPrice_eth_usdt = token_sellPrice_eth * eth_usdtPrice
        token_buyPrice_btc_usdt = token_buyPrice_btc * btc_usdtPrice
        token_sellPrice_btc_usdt = token_sellPrice_btc * btc_usdtPrice
    else:
        token_buyPrice_eth_usdt = 0
        token_sellPrice_eth_usdt = 0
        token_buyPrice_btc_usdt = 0
        token_sellPrice_btc_usdt = 0


    print('eth_sell_depth=', base01_sell_depth)
    print('eth_buy_depth=', base01_buy_depth)
    print('btc_sell_depth=', base02_sell_depth)
    print('btc_buy_depth=', base02_buy_depth)

    print(token[0], ' buyPrice_usdt= ', token_buyPrice_eth_usdt)
    print(token[0], ' sellPrice_usdt= ', token_sellPrice_eth_usdt)
    print(token[1], ' buyPrice_usdt= ', token_buyPrice_btc_usdt)
    print(token[1], ' sellPrice_usdt= ', token_sellPrice_btc_usdt)
    ###幣對以太、比特內外盤價格（換成usdt)

    ###計算幣在以太、比特內外盤套利趴數，決定是否下單
    if (token_buyPrice_eth_usdt != False) & (token_buyPrice_btc_usdt != False) & (token_sellPrice_eth_usdt != False) & (token_sellPrice_btc_usdt != False):
        ethB_btcS = (token_buyPrice_eth_usdt - token_sellPrice_btc_usdt) / token_sellPrice_btc_usdt
        btcB_ethS = (token_buyPrice_btc_usdt - token_sellPrice_eth_usdt) / token_sellPrice_eth_usdt
        print('ethB_btcS= ', ethB_btcS)
        print('btcB_ethS= ', btcB_ethS)

        if debug == 1:
            btcB_ethS = 0.1

        #ethB_btcS= 0.016197612437833023
        if ethB_btcS >= btcB_ethS:
            profitInfo = {"ethB_btcS": ethB_btcS}
        else:
            profitInfo = {"btcB_ethS": btcB_ethS}

        print("profitInfo= ", profitInfo)

        #有利可圖啦
        profit_ratioThd = 0.007
        minBtcNum = 0.09
        minEthNum = 2.5

        if(ethB_btcS >= profit_ratioThd)|(btcB_ethS >= profit_ratioThd):
            print('下單時間:', time.asctime( time.localtime(time.time()) ))
            eth_ask_depth, eth_bid_depth = MarketDepth(token[0], 1)
            btc_ask_depth, btc_bid_depth = MarketDepth(token[1], 1)






            #下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單
            nexOderCondition(profitInfo, profit_ratioThd, minBtcNum, minEthNum, priceArray, debug)






            #下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單下單





            fp=open('Order.txt', 'a')
            if fp !=None:
                fp.write('**************************')
                fp.write(time.asctime( time.localtime(time.time()) ))
                fp.write('\n')
                fp.write('ethB_btcS= ')
                fp.write(str(ethB_btcS))
                fp.write('\n')
                fp.write('btcB_ethS= ')
                fp.write(str(btcB_ethS))
                fp.write('\n')

                fp.write('eth_ask_depth\n')
                for i in eth_ask_depth:
                    fp.write(i[0])
                    fp.write(' ')
                    fp.write(i[1])
                    fp.write('\n')

                fp.write('\n')

                fp.write('eth_bid_depth\n')
                for i in eth_bid_depth:
                    fp.write(i[0])
                    fp.write(' ')
                    fp.write(i[1])
                    fp.write('\n')

                fp.write('\n')

                fp.write('btc_ask_depth\n')
                for i in btc_ask_depth:
                    fp.write(i[0])
                    fp.write(' ')
                    fp.write(i[1])
                    fp.write('\n')

                fp.write('\n')

                fp.write('btc_bid_depth\n')
                for i in btc_bid_depth:
                    fp.write(i[0])
                    fp.write(' ')
                    fp.write(i[1])
                    fp.write('\n')

            fp.close()
    ###計算幣在以太、比特內外盤套利趴數，決定是否下單

# 進場條件、流程
'''
目標：不同交易對獲利 _input_ration >= profit_ratio 進場交易
流程：
    - 進場條件
        - 獲利 _input_ration >= profit_ratio
        - 比較nex , btc & eth 餘額 ？ minTradeDepth (足夠的下單餘額)
            - 餘額 >= minTradePrice下單,交易為內盤深度：
            - 餘額 < minTradePrice下單,交易為內盤深度：
                - 同時買進賣出 minTradePrice = min(sell depths, buy depth) Price
                    - 是否掛單成功
                        - 是
                            - 是否成交(End, 紀錄結果)
                                - 是
                                    - 紀錄成交紀錄
                                - 否
                                    - 紀錄掛單紀錄
                        - 否
                            - 再次掛單, 是否成功(End, 紀錄)
                                - 是
                                - 否
input :
    profitInfo =
        {"ethB_btcS": ethB_btcS}
        {"btcB_ethS": btcB_ethS}
    profit_ratioThd = 0.01
    minBtcNum = 0.15
    minEthNum = 4
    _buy_sell_Price_array = [01100111, 01147935, 000374, 00039119]
                            nex_eth  buyPrice =  0.01100111
                            nex_eth sellPrice =  0.01147935
                            nex_btc  buyPrice =  0.000374
                            nex_btc sellPrice =  0.00039119

    debug = 0 # 1:enable, 0:enable

    test : nexOderCondition({"ethB_btcS": 0.1}, 0.01, 0.15, 4, 1)

return :
'''

def nexOderCondition(_profitInfo,
                     profit_ratioThd,
                     minBtcNum,
                     minEthNum,
                     _buy_sell_Price_array,
                     debug):

    # get 獲利交易對 :
    #   ethB_btcS 或 btcB_ethS
    profit_tradePair = list(_profitInfo.keys())[0]
    profit_ratio = _profitInfo[profit_tradePair]
    print('profit_tradePair= ', profit_tradePair)
    print('profit_ratio= ', profit_ratio)



    # 獲利 _input_ration >= profit_ratio , 觸發下單
    if profit_ratio >= profit_ratioThd:
        print('有利可圖')
        print('獲利 profit_ratio: ', profit_ratio, '>= profit_ratioThd: ', profit_ratioThd)


        # nex , btc & eth 餘額 >= minTradePrice (最小的下單餘額)
        # eth , nex餘額
        BalanceNum = AccountCoinInfo('nex_eth')

        if BalanceNum != False:
            ethBalanceNum = float(BalanceNum['data'][1]['hotMoney'])
            nexBalanceNum = float(BalanceNum['data'][0]['hotMoney'])
        else:
            ethBalanceNum = 0
            nexBalanceNum = 0

        # btc 餘額
        BalanceNum = AccountCoinInfo('nex_btc')
        if BalanceNum != False:
            btcBalanceNum = float(BalanceNum['data'][1]['hotMoney'])
        else:
            btcBalanceNum = 0


        print('nexBalanceNum= ', nexBalanceNum)
        print('ethBalanceNum= ', ethBalanceNum)
        print('btcBalanceNum= ', btcBalanceNum)
        print('minEthNum =', minEthNum)
        print('minBtcNum =', minBtcNum)




        # minTradePrice (最小的下單餘額)
        if profit_tradePair == 'ethB_btcS':

            #priceArray = [token_buyPrice_eth, token_sellPrice_eth, token_buyPrice_btc, token_sellPrice_btc]

            print("ethB_btcS下單交易判斷")

            #決定內外盤的nex數量
            buyResult = MarketDepth('nex_eth', 1)
            sellResult = MarketDepth('nex_btc', 1)

            #買賣盤nex顆數與價格
            if (buyResult != False) & (sellResult != False):
                buyNexDepth = float(buyResult[1][0][1]) # nex掛買數量
                buyNexDepth_price = float(buyResult[1][0][0]) # nex 掛買價
                buyPrice_arr = _buy_sell_Price_array[0]

                sellNexDepth = float(sellResult[0][0][1]) # nex掛賣數量
                sellNexDepth_price = float(sellResult[0][0][0]) # nex 掛賣價
                sellPrice_arr = _buy_sell_Price_array[3]

                sellNexDepthBalance = btcBalanceNum / sellPrice_arr # 可吃的nex數量餘額

            else:
                buyNexDepth = 0
                sellNexDepth = 0


        elif profit_tradePair == 'btcB_ethS':
            print("btcB_ethS下單交易判斷")

            #決定內外盤的nex數量
            buyResult = MarketDepth('nex_btc', 1)
            sellResult = MarketDepth('nex_eth', 1)

            #買賣盤nex顆數與價格
            if (buyResult != False) & (sellResult != False):
                buyNexDepth = float(buyResult[1][0][1]) # 有多少nex掛買
                buyNexDepth_price = float(buyResult[1][0][0]) # nex 掛買價
                buyPrice_arr = _buy_sell_Price_array[2]

                sellNexDepth = float(sellResult[0][0][1]) # 有多少nex掛賣
                sellNexDepth_price = float(sellResult[0][0][0]) # nex 掛賣價
                sellPrice_arr = _buy_sell_Price_array[1]

                sellNexDepthBalance = ethBalanceNum / sellPrice_arr  # 自己可以買多少nex

            else:
                buyNexDepth = 0
                sellNexDepth = 0




        # 比較nex Num 與 eth/Btc Buy nex數量
        print('sellNexDepth= ', sellNexDepth)
        print('buyNexDepth= ', buyNexDepth)
        nexTradeNum = min(nexBalanceNum, buyNexDepth, sellNexDepth, sellNexDepthBalance)
        cancelOrder_flag = 0
        if nexTradeNum < 1:
            nexTradeNum = 1;
            cancelOrder_flag = 1

        print('nexTradeNum= ', nexTradeNum)
        print('**[no use]buyNexDepth_price= ', buyNexDepth_price)
        print('**[no use]sellNexDepth_price= ', sellNexDepth_price)
        print('buyPrice_arr= ', buyPrice_arr)
        print('sellPrice_arr= ' , sellPrice_arr)



        print('change price before ording:')
        # 掛賣變貴、掛買變便宜、利潤改變、不交易
        if (sellPrice_arr < sellNexDepth_price) | (buyPrice_arr > buyNexDepth_price):
            nexTradeNum = 0
        buyPrice_arr = max(buyPrice_arr, buyNexDepth_price)
        sellPrice_arr = min(sellPrice_arr, sellNexDepth_price)

        print('**[no use]buyNexDepth_price= ', buyNexDepth_price)
        print('**[no use]sellNexDepth_price= ', sellNexDepth_price)
        print('buyPrice_arr= ', buyPrice_arr)
        print('sellPrice_arr= ' , sellPrice_arr)



        if nexTradeNum == 0:
            print("交易顆數＝0,不交易")
            fp=open('OrderID.txt', 'a')
            if fp !=None:
                fp.write('**************** 奇怪的單 *********************')
                fp.write('\n')
                fp.write(time.asctime( time.localtime(time.time()) ))
                fp.write('\n')
            fp.close()

        else:

            print("下單交易")
            # 賣/買nex
            if profit_tradePair == 'ethB_btcS':
                if debug == 0:
                    sell_nex_tradeID = Trade('nex_eth', 2, buyPrice_arr, round(nexTradeNum, 4))
                    buy_nex_tradeID = Trade('nex_btc', 1, sellPrice_arr, round(nexTradeNum, 4))
                else:
                    sell_nex_tradeID = '0000'
                    buy_nex_tradeID = '1111'



            elif profit_tradePair == 'btcB_ethS':
                if debug == 0:
                    sell_nex_tradeID = Trade('nex_btc', 2, buyPrice_arr, round(nexTradeNum, 4))
                    buy_nex_tradeID = Trade('nex_eth', 1, sellPrice_arr, round(nexTradeNum, 4))
                else:
                    sell_nex_tradeID = '0000'
                    buy_nex_tradeID = '1111'


            print('sell_nex_tradeID= ',sell_nex_tradeID)
            print('buy_nex_tradeID= ',buy_nex_tradeID)

            # 撤單規則
            if debug == 1:
                buy_nex_tradeID = False

            if (sell_nex_tradeID == False) & (buy_nex_tradeID != False):
                CancelEntrust(buy_nex_tradeID)
                print('cancel order : ', CancelEntrust)

            elif (sell_nex_tradeID != False) & (buy_nex_tradeID == False):
                CancelEntrust(sell_nex_tradeID)
                print('cancel order : ', CancelEntrust)

            if cancelOrder_flag:
                CancelEntrust(buy_nex_tradeID)
                CancelEntrust(sell_nex_tradeID)




            fp=open('OrderID.txt', 'a')
            if fp !=None:
                fp.write('**************** order *********************')
                fp.write('\n')
                fp.write(time.asctime( time.localtime(time.time()) ))
                fp.write('\n')
                fp.write(str(sell_nex_tradeID))
                fp.write('\n')
                fp.write(str(buy_nex_tradeID))
                fp.write('\n')
            fp.close()




        #eth btc換錢
        DepthResult = MarketDepth('eth_btc', 3)
        if DepthResult != False:
            if (ethBalanceNum < minEthNum) & (btcBalanceNum > minBtcNum):

                # eth 太少，用BTC買ETH
                print("btc買eth")
                #第三檔賣價
                Depth_price = float(DepthResult[0][2][0])
                exchangeNum = (btcBalanceNum - minBtcNum) / Depth_price

                print("***************** btc換eth *********************")
                tokenExchangeID = Trade('eth_btc', 1, round(Depth_price, 5), round(exchangeNum,4))
                print('tokenExchangeID= ', tokenExchangeID)

                #記錄換錢log, 紀錄orderID
                fp=open('OrderID.txt', 'a')
                if fp !=None:
                    fp.write('**************** exchange *********************')
                    fp.write('\n')
                    fp.write(str(tokenExchangeID))
                    fp.write('\n')
                fp.close()


            elif (btcBalanceNum < minBtcNum) & (ethBalanceNum > minEthNum):
                # btc 太少，賣ETH換BTC
                print("賣eth換btc")


                #第三檔買價
                Depth_price = float(DepthResult[1][2][0])
                exchangeNum = ethBalanceNum - minEthNum

                print("***************** eth換btc *********************")
                tokenExchangeID = Trade('eth_btc', 2, round(Depth_price, 5), round(exchangeNum,4))
                print('tokenExchangeID= ', tokenExchangeID)

                #記錄換錢log, 紀錄orderID
                fp=open('OrderID.txt', 'a')
                if fp !=None:
                    fp.write('**************** exchange *********************')
                    fp.write('\n')
                    fp.write(str(tokenExchangeID))
                    fp.write('\n')
                fp.close()
            else:
                print("沒有換錢")
    else:
        print('沒利可圖')



nexOperarion(0)

Start = True
# Main run ****************
while Start:
    print('*********************** TIME *******************')
    print(time.asctime( time.localtime(time.time()) ))
    nexOperarion(0)
    time.sleep( 10 )





'''
#legency search
#Data1 = AllTickers()

fp=open('Order.txt', 'a')
if fp !=None:
    fp.write('START====\n')
fp.close()

print("search start!")
tick = 0
while True:
    Data01, Data02, Data03, Data04 = TargetInfo('nex')
    #print(Data01)
    #print(Data02)
    #print(Data03)
    #print('*********************')
    tick = tick + 10
    if tick == 3600:
        print('一小時')
        tick = 0
    time.sleep( 10 )
'''
