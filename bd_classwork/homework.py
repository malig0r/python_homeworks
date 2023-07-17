import sqlite3

def db_adjuster(*args):
    conn = sqlite3.connect('name1.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
    match len(args):
        case 0:
            print("function must be called with at least one argument")
        case 1:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
            conn.commit()
        case 2 if type(args[1]) == int:
            cursor.execute('''DELETE from tab_1 WHERE id = 1''')
            conn.commit()
        case 3 if type(args[2]) == int:
            cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')
            conn.commit()
        case _:
            print('No conditions were met')

    cursor.execute('''SELECT * FROM tab_1''')
    k = cursor.fetchall()
    for i in k:
        print(i)
            
    print('_________________________')        
    return         


if __name__ == '__main__':
    db_adjuster()
    db_adjuster(1)
    db_adjuster(1)
    db_adjuster(1)
    db_adjuster(1, 'test')
    db_adjuster(1, 2)
    db_adjuster(1, 2, 'test')
    db_adjuster(1, 2, 3)