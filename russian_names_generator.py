from russian_names import RussianNames 
import openpyxl

def input_names_number() -> int:
    while True:
        try:
            names_number = int(input('Введите количество личностей для создания\n'))
        except:
            print('Неверное положительное целое число')
            continue
        if names_number <= 0:
            print('Неверное положительное целое число')
            continue
        break
    return names_number

def create_persons(names_number: int) -> list[[str, str, str]]:
    persons_list = []
    while  names_number > 0:
        rp = RussianNames()
        person_data = rp.get_person().split(' ')
        persons_list.append(person_data)
        names_number -= 1
    print(persons_list)
    return persons_list

def wb_filler(names_tuple: tuple[str, str, str]) -> None:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(names_tuple)
    wb.save('sample.xlsx')


if __name__ == '__main__':
    persons_list = create_persons(input_names_number())
#    wb_filler(first_tuple)