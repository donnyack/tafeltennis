from connection_with_db import get_cursor

def start(): 
    myconn, mycursor = get_cursor()
    mycursor.execute("""SELECT 
        m.id,
        t.name AS tournament,
        m.round,
        m.table_number,
        p1.first_name AS player1_first_name,
        p1.last_name  AS player1_last_name,
        p2.first_name AS player2_first_name,
        p2.last_name  AS player2_last_name,
        m.player1_score,
        m.player2_score,
        pw.first_name AS winner_first_name,
        pw.last_name  AS winner_last_name,
        m.match_time
        FROM match_game m
        JOIN tournament t ON m.tournament_id = t.id
        JOIN player p1    ON m.player1_id = p1.id
        JOIN player p2    ON m.player2_id = p2.id
        JOIN player pw    ON m.winner_id  = pw.id
        WHERE t.name = 'Eindhoven Open';
        """)
    output = mycursor.fetchall()
    return output