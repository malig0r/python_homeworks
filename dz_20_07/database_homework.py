import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        """1. Создайте метод класса для работы с БД, который будет создавать новую таблицу с двумя колонками: 
        id и name. Типы данных колонок INT и TEXT соответственно. 
        Если таблица уже существует, метод должен выводить сообщение об ошибке."""
        # sqlite вернет ошибку вверх по стеку вызова т.к. не используется IF NOT EXISTS
        self.cursor.execute("""CREATE TABLE mytable(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)""")
        self.conn.commit()
        print('Table created')
        return
    
    def insert_record(self, id, name):
        """2. Создайте метод класса для работы с БД, который добавляет новую запись в таблицу. 
        Метод должен принимать два аргумента: id (INT) и name (TEXT). 
        Запись должна быть добавлена только в том случае, если такого id в таблице еще нет."""
        self.cursor.execute('SELECT id from mytable where id = ?',(id, ))
        k = self.cursor.fetchall()
        if len(k):
            print('Id already exists')
        else:    
            self.cursor.execute('''INSERT INTO mytable(id, name) VALUES (?, ?)''', (id, name))
            self.conn.commit()
            print('Added record with id =', id)
        return

    def update_record(self, id, name):
        """3. Создайте метод класса для работы с БД, который обновляет значение name в записи с заданным id. 
        Метод должен принимать два аргумента: id (INT) и новое значение для name (TEXT)."""
        self.cursor.execute('SELECT id from mytable WHERE id = ?', (id, ))
        k = self.cursor.fetchall()
        if len(k):
            self.cursor.execute("UPDATE mytable SET name = ? WHERE id= ?", (name, id))
            self.conn.commit()
            print('Updated record with id =', id)
        else:
            print('Id for update does not exist')
        return


    def delete_record(self, id):
        """4. Создайте метод класса для работы с БД, который удаляет запись с заданным id. 
        Метод принимает один аргумент - id (INT)."""
        self.cursor.execute('SELECT id from mytable WHERE id = ?', (id, ))
        k = self.cursor.fetchall()
        if len(k):
            self.cursor.execute("DELETE from mytable WHERE id= ?", (id, ))
            self.conn.commit()
            print('Deleted record with id =', id)
        else:
            print('Id for deletion does not exist')
        return

    def print_records(self):
        """5. Создайте метод класса для работы с БД, который выводит все записи из таблицы."""
        self.cursor.execute('''SELECT * FROM mytable''')
        k = self.cursor.fetchall()
        if len(k):
            print('Printing entire table')
            for i in k:
                print(i)
        else:
            print('The table is empty')
        return
    
    def delete_all_records(self):
        self.cursor.execute("DELETE from mytable")
        self.conn.commit()
        print('Deleted all records')
        return

if __name__ == '__main__':
    db = Database()
    try:
        db.create_table()
    except:
        print('Table already exists')
    db.insert_record(1, 'aboba')
    db.insert_record(2, 'fastsat')
    db.insert_record(3, 'dasdasdas')
    db.update_record(3, 'abudabi')
    db.update_record(4, 'abudabi')
    db.delete_record(4)
    db.delete_record(3)
    db.print_records()
    db.delete_all_records()
    db.print_records()