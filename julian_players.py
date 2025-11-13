from connection_with_db import get_cursor
from flask import jsonify

def start(): 
    myconn, mycursor = get_cursor()
    mycursor_dict = myconn.cursor(dictionary=True)
    mycursor_dict.execute("""
        SELECT 
            p.id,
            p.first_name,
            p.last_name,
            p.birthdate,
            p.gender,
            p.playing_style,
            p.club_id,
            c.name AS club_name
        FROM player p
        LEFT JOIN club c ON p.club_id = c.id
        """)
    output = mycursor_dict.fetchall()
    return jsonify(output)