from connection_with_db import get_cursor
from flask import jsonify

def start():
    print("Het is gelukt!")

    myconn, mycursor = get_cursor()
    mycursor.execute("""SELECT * FROM club, player WHERE player.club_id = club.id""")
    rows = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return jsonify(rows)