import xlrd
import xlwt
from xlrd import *
from xlutils.copy import copy


# book = xlrd.open_workbook(filename)
# sheel_1 = book.sheet_by_index(0)
# print("Worksheet name(s): ",book.sheet_names()[0])
# # Worksheet name(s):  工作表1
#
# print('book.nsheets',book.nsheets)
# book.nsheets 1

# print('sheel_1.name:',sheel_1.name,'sheel_1.nrows:',sheel_1.nrows,'sheel_1.ncols:',sheel_1.ncols)
# # sheel_1.name: 工作表1 sheel_1.nrows: 149 sheel_1.ncols: 7
#
# print('A1:',sheel_1.cell_value(rowx=1,colx=0))
# # A1: https://www.mochange.co/products/shop_info.php?product_sernum=340


# # 顯示sheet中某一欄位內容
# def ShowAllItem(file_name, sheet_name, row_idx, col_idx):
#     sheetName_flag = False
#     checkName = ShowSheet(file_name)
#
#
#     totalCols = ShowRowCol(file_name, sheet_name)


# 顯示所有的sheet
def ShowSheet(file_name):
    book = xlrd.open_workbook(file_name)
    sheetNum = book.nsheets
    sheetName = []
    print('book.nsheets: ',sheetNum)
    for i in range(sheetNum):
        sheetName.append(book.sheet_names()[i])

    print("Worksheet name(s): ", sheetName)
    return sheetName

# 顯示sheet 中的row & col數量
def ShowRowCol(file_name, sheet_name):
    AllSheet = ShowSheet(file_name)
    for i in range(len(AllSheet)):
        if AllSheet[i] == sheet_name:
            book = xlrd.open_workbook(file_name)
            sheet = book.sheet_by_index(i)
            print('get sheet name: ', sheet.name)
            print('rows: ', sheet.nrows)
            print('cols: ', sheet.ncols)
            break
    return sheet.nrows, sheet.ncols

# 增加一個sheet
def AddSheet(file_name, sheet_name):
    w = copy(xlrd.open_workbook(file_name))
    w.add_sheet(sheet_name)
    w.save(file_name)

# 寫入
def WriteContext(file_name, sheet_name, row, col, context):
    checkName = ShowSheet(file_name)
    sheet_idx = 0
    write_success = False
    for value in checkName:
        if value == sheet_name:
            w = copy(xlrd.open_workbook(file_name))
            w.get_sheet(value).write(row, col, context)
            w.save(file_name)
            write_success = True
            break
        else:
            sheet_idx += 1

    if write_success:
        print('=== write SUCCESS ===')
    else:
        print('=== write FAIL ===')
