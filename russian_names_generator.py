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

def create_persons(names_number: int) -> list[list[str, str, str]]:
    persons_list = []
    while  names_number > 0:
        rp = RussianNames()
        person_data = rp.get_person().split(' ')
        persons_list.append(person_data)
        names_number -= 1
    return persons_list

def wb_filler(persons_list: list[list[str, str, str]]) -> None:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Номер','Фамилия', 'Имя', 'Отчество'])
    for i, person in enumerate(persons_list):
        ws.append([i + 1, person[2], person[0], person[1]])
    wb.save('sample.xlsx')


if __name__ == '__main__':
    persons_list = create_persons(input_names_number())
    wb_filler(persons_list)