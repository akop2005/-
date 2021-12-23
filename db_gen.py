# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3

# Создаем соединение с нашей базой данных
conn = sqlite3.connect('test.db')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО


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
INSERT INTO users(name,reg_date) VALUES ('Aaa A','2021-01-01'), ('Bbb B','2021-02-02'),('Ccc C','2021-03-03');
''',
        '''
INSERT INTO connections(user_id,group_id) VALUES (1,2),(2,1),(3,2);
'''
    ]



transaction = '''
BEGIN TRANSACTION;
DELETE FROM users WHERE id = 2;
DELETE FROM connections WHERE user_id = 2;
COMMIT;
'''

cursor.execute('DROP TABLE connections')
cursor.execute('DROP TABLE groups')
cursor.execute('DROP TABLE users')


for i in tables:
    cursor.executescript(i)
print('Таблицы успешно созданы')

for i in contents:
    cursor.executescript(i)
conn.commit()
print('Данные успешно созданы')
 
cursor.execute('SELECT * FROM users')
print(*cursor.fetchall(),sep='\n')
print("А щас вот будет транзакция)")
cursor.executescript(transaction)
conn.commit()

cursor.execute('SELECT * FROM users')
print(*cursor.fetchall(),sep='\n')

# Не забываем закрыть соединение с базой данных
conn.close()
