import sqlite3, os

class Database:
    def __init__(self):
        self.db_path = 'database/scores.db'

        if not os.path.exists('database'):
            os.makedirs('database')

        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = '''CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT,
                score INTEGER,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP )'''
            cursor.execute(query)

    def save_score(self, name, score):
        if not name.strip():
            name = 'Player'
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO high_scores (player_name, score) VALUES (?, ?)'
            cursor.execute(query, (name, score))

    def get_top_scores(self, limit=5):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = '''SELECT player_name, score FROM high_scores 
                    ORDER BY score DESC LIMIT ?'''
            cursor.execute(query, (limit,))
            return cursor.fetchall()