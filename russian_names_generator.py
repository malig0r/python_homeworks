from russian_names import RussianNames 
import openpyxl


def create_person() -> tuple[str, str, str]:
    rp = RussianNames()
    person_tuple = rp.get_person().split(' ')
    return person_tuple

def wb_filler(names_tuple: tuple[str, str, str]) -> None:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws['A1'].value = names_tuple[0]
    wb.save('sample.xlsx')


if __name__ == '__main__':
    rp = RussianNames()
    print(create_person())