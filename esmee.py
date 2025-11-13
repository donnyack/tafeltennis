from connection_with_db import get_cursor

def start():
    myconn, mycursor = get_cursor()
    mycursor.execute("SELECT * FROM club;")  
    rows = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]
    data = [dict(zip(keys, row)) for row in rows]
    
    return data


