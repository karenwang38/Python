from MoChange import *
from excelUseSample import *

emailList = ['karen.wang38@gmail.com', 'chctrader@gmail.com', 'llibs38@gmail.com', 'chctrader001@gmail.com']
filename = '券集商城大集合713.xlsx'
sheetName = '20191120'
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



for mail_idx in emailList:
    ticket_listDB = TicketList(mail_idx)
    ticket_numberDB = ticket_listDB[0]
    ticket_nameDB = ticket_listDB[1]
    print("(DB)ticket_number: ", ticket_numberDB)
    print("(DB)ticket_number: ", ticket_nameDB)

    # 開始寫入的行數，不要覆蓋之前的資料
    start_row = ShowRowCol(filename, sheetName)[0]
    print("(DB) start_row: ", start_row)
    for i in range(len(ticket_numberDB)):
        ticket_numberDB_idx = ticket_numberDB[i]
        ticket_nameDB_idx = ticket_nameDB[i]
        WriteContext(filename, sheetName, start_row + i, 0, ticket_numberDB_idx)
        WriteContext(filename, sheetName, start_row + i, 1, ticket_nameDB_idx)
        WriteContext(filename, sheetName, start_row + i, 2, mail_idx)
