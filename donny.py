from connection_with_db import get_cursor

def start():
    connection, cursor = get_cursor()
    cursor.execute("""SELECT CONCAT(first_name, " ", last_name) as full_name, gender, playing_style, club.name as club
FROM player
JOIN club
on player.club_id = club.id""")
    rows = cursor.fetchall()
    keys = [i[0] for i in cursor.description]
    data = [dict(zip(keys,row)) for row in rows]
    return data