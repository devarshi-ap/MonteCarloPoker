"""
Use Poker table on sqlite3 DB to:
- Evaluate Hand Probabilities (Monte Carlo Method)
- Make graphs of sorts (use MTH380 knowledge)
"""
import sqlite3

if __name__ == '__main__':
    # Connect to DB
    connection = sqlite3.connect("poker.db")
    cursor = connection.cursor()

    # Read All Records
    for row in cursor.execute("SELECT * FROM Poker"):
        print(row)

    connection.commit()

    connection.close()