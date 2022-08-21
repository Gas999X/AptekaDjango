import sqlite3
import parser_script

with sqlite3.connect('parsing#N#H#T.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS parser (id INT, name TEXT, href TEXT, abbreviated TEXT)"""
    cursor.execute(query)
    db.commit()


def sorting_lists():
    to_SQL = parser_script.get_parsing_lsgeotar()

    query = """DELETE FROM parser"""
    cursor.execute(query)
    db.commit()

    query = """INSERT INTO parser (id, name, href, abbreviated) 
                                    VALUES (?,?,?,?)"""

    for i in range(len(to_SQL[0])):
        name = to_SQL[0][i]
        href = to_SQL[1][i]
        text = to_SQL[2][i]
        print()
        print(f"{name} \n {href}\n {text}")

        query_list = (i, name, href, text)
        cursor.execute(query, query_list)
        db.commit()
    print()
    print("Добавлено ", i + 1, " строк")


sorting_lists()
