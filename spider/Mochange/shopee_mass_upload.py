from MoChange import *
from excelUseSample import *

filename = 'Shopee_mass_upload_template_sku_tw.xlsx'
sheetName = 'VIP2_Price'
SheetAll = ShowSheet(filename)
sheetExit = False

# 檢查sheet存在
for sheet_idx in SheetAll:
    if sheet_idx == sheetName:
        sheetExit = True
        break
# 如果sheet不存在，增加sheet
if sheetExit == False:
    AddSheet(filename, sheetName)
    ShowSheet(filename)

print('(DB)SheetAll: ', SheetAll)



a = [{'Name': '北投【春天酒店】單人泡湯劵MO', 'Link': 'https://www.mochange.co//products/shop_info.php?product_sernum=337', 'Picture': 'https://stage.mohist.com.tw/Mobuy/BackEnd/images/UpoladImage/20190413195059_ca7d6.jpg', 'Original Price': '$900', 'VIP2 Price': '391', 'Attention': '※票券上銀行信託期限至2019/12/07，並非使用期限，本票券優惠期限為【2020年3月31日，逾期後不得要求提供原優惠，但仍可依其面額折抵$400元】。※本賣場票券為專案採購，載明之面額為【$400元】，不等同於本賣場零售價，無法接受者請勿購買。'}]

print('a= ', a)

#批量寫入蝦皮excel
def Write2Excel(data):
    for i in range(len(data)):
        print('======================================')
        print(data[i]['Name'])
        print(data[i]['Link'])
        print(data[i]['Picture'])
        print(data[i]['Original Price'].replace('$', ''))
        print(data[i]['VIP2 Price'])
        print(data[i]['Attention'])

        WriteContext(filename, sheetName, 6+i, 0, '8216')
        WriteContext(filename, sheetName, 6+i, 1, data[i]['Name'])
        WriteContext(filename, sheetName, 6+i, 2, data[i]['Attention'])
        WriteContext(filename, sheetName, 6+i, 3, data[i]['Original Price'].replace('$', ''))
        WriteContext(filename, sheetName, 6+i, 4, '4')
        WriteContext(filename, sheetName, 6+i, 5, data[i]['VIP2 Price'])
        WriteContext(filename, sheetName, 6+i, 89, data[i]['Picture'])
        WriteContext(filename, sheetName, 6+i, 90, 'https://mochange.mohist.com.tw/BackEnd/images/UpoladImage/images/MoChange_1912615380242318.jpg')
        WriteContext(filename, sheetName, 6+i, 99, '關閉')
        WriteContext(filename, sheetName, 6+i, 101, '關閉')
        WriteContext(filename, sheetName, 6+i, 102, '關閉')
        WriteContext(filename, sheetName, 6+i, 103, '關閉')
        WriteContext(filename, sheetName, 6+i, 104, '關閉')
        WriteContext(filename, sheetName, 6+i, 105, '關閉')
        WriteContext(filename, sheetName, 6+i, 107, '關閉')
        WriteContext(filename, sheetName, 6+i, 108, '0')
