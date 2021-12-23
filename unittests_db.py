import unittest
import sqlite3
#
#
#
# Структура создания такого файлика такова:
# - импорты(юниттест и sqlite)
# - функции по работе с таблицей, которые можно использовать в инициализации(я использую try except, поэтому пишу их отдельно)
# - создание класса юниттеста
# - setup и teardown (создание таблицы, заполнение и очистка. можно использовать не файл, а оперативную память, вместо названия базы указав :memory:)
# - cами тесты
# - открытие соединения
# - ВОТ ТУТ ВЫЗЫВАЕМ ТЕСТЫ
# - закрываем соединение
#
# Всё, збс, всё круто работает. 
# Если какая-то переменная не определена, то скорее всего вы не туда что-то вписали
#
#
#
#

def create():
    tables = [
    '''
CREATE TABLE groups (
    id     INTEGER PRIMARY KEY AUTOINCREMENT
                   NOT NULL,
    letter CHAR    NOT NULL,
    num    INTEGER NOT NULL
);
''',
    '''
CREATE TABLE users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL,
    name     STRING  NOT NULL,
    reg_date DATE    NOT NULL
);
''',

    '''CREATE TABLE connections (
    group_id INTEGER REFERENCES groups(id),
    user_id INTEGER REFERENCES groups(id)
);''']
    contents = [
    '''
INSERT INTO groups(letter,num) VALUES ('A',1),('A',2),('A',3);
    ''',
    '''
INSERT INTO users(name,reg_date) VALUES 
('Aaa A','2021-01-01'),
('Bbb B','2021-02-02'),
('Ccc C','2021-03-03'),
('Fff F','2021-04-04'),
('Eee E','2021-03-03'),
('Ggg G','2021-03-03')
;
''',
     '''
INSERT INTO connections(user_id,group_id) VALUES (1,2),(2,1),(3,2);
'''
    ]


    for i in tables:
        cursor.executescript(i)

    for i in contents:
        cursor.executescript(i)
    conn.commit()


def skip_db():
    cursor.execute('DROP TABLE users')
    cursor.execute('DROP TABLE groups')
    cursor.execute('DROP TABLE connections')



class TestDB(unittest.TestCase):
    def setUp(self): # эта часть выполняется перед тестами
        try:
            create()
        except sqlite3.OperationalError:
            skip_db()
            create()
        # Если база данных не создана, то создаётся, если создана, то очищается и заполняется заново, чтобы работали тесты

    def tearDown(self): # эта часть выполняется после всех тестов
        skip_db()
        # Очищаем базу данных после тестов
    
    def test_add_d(self):
        cursor.execute("INSERT INTO users(name,reg_date) VALUES ('Ddd D','2021-01-01');")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE name='Ddd D';")
        conn.commit()
    
        self.assertTrue(len(cursor.fetchall()) == 1)
        
    def test_delete_one_user(self):
        cursor.execute("DELETE FROM users WHERE name='Ddd D';")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE name='Ddd D';")
        self.assertTrue(len(cursor.fetchall()) == 0)
        
    def test_delete_many_users(self): # удаление с помощью транзакции
        transaction = '''
        BEGIN TRANSACTION;
        DELETE FROM users WHERE id = 2;
        DELETE FROM connections WHERE user_id = 2;
        COMMIT;
        '''
        cursor.executescript(transaction)
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id = 2")
        x = len(cursor.fetchall())
        cursor.execute("SELECT * FROM connections WHERE user_id = 2;")
        x+=len(cursor.fetchall())
        self.assertTrue(x == 0)




# Создаем соединение с нашей базой данных
conn = sqlite3.connect('test1.db')
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
# Остальной код находится в функциях <з

if __name__ == '__main__':
    unittest.main()
    
conn.close()


