from connection_with_db import get_cursor

def start():
    print("Het is gelukt!")

    myconn, mycursor = get_cursor()
    mycursor.execute("""SELECT * FROM club WHERE country = 'Netherlands'""")
    rows = mycursor.fetchall()
    print("hoi")
    keys = [i[0] for i in mycursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return data