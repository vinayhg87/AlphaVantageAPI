import openpyxl

class ExcelOperation(object):
    def readExcelData(self, sheetname):
        workbook = openpyxl.open("exceldata.xlsx")
        worksheet = workbook[sheetname]