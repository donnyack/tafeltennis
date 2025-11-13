from connection_with_db import get_cursor

def start():
    myconn, mycursor = get_cursor()
    mycursor.execute("SELECT * FROM club;")  
    output = mycursor.fetchall()
    print(output)
    return output
