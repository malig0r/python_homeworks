from russian_names import RussianNames 
import openpyxl


def create_person() -> tuple[str, str, str]:
    rp = RussianNames()
    person_tuple = rp.get_person().split(' ')
    return person_tuple

def wb_filler(names_tuple: tuple[str, str, str]) -> None:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(names_tuple)
    wb.save('sample.xlsx')


if __name__ == '__main__':
    first_tuple = create_person()
    wb_filler(first_tuple)