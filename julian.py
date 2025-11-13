from connection_with_db import get_cursor
from flask import jsonify

def start(): 
    myconn, mycursor = get_cursor()
    mycursor_dict = myconn.cursor(dictionary=True)
    mycursor_dict.execute("""SELECT * FROM club""")
    output = mycursor_dict.fetchall()
    return jsonify(output)