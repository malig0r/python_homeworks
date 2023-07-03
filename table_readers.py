from abc import ABC, abstractmethod
import csv
import openpyxl


CellValue = str | int | float


class TableReader(ABC):
    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def read(self) -> list[list[CellValue]]:
        pass

class CSVTableReader(TableReader):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> list[list[CellValue]]:
        with open(self._filename, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter = ',')
            count = 0
            values_list = []
            for i in file_reader:
                values_list.append(i)
            return values_list

class XLSXTableReader(TableReader):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> list[list[CellValue]]:      
        wb = openpyxl.load_workbook(self._filename)
        sheet = wb.active
        values_list = []
        for i in sheet['A1':'I8']:
            row = []
            for j in i:
                if  j.value != None:
                    row.append(j.value)
                else:
                    continue
            if len(row) != 0:  
                values_list.append(row)
            else:
                continue
        return values_list


if __name__ == "__main__":
#    reader = CSVTableReader('output.csv')
#    print(reader.read())
    reader = XLSXTableReader('output.xlsx')
    print(reader.read())

