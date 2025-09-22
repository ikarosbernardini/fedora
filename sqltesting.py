import sqlite3
con = sqlite3.connect("tutorial.db") # här skapas en databasfil
cur = con.cursor()  # em cursor används för att utföra SQL-kommandon

# cur.execute("CREATE TABLE IF NOT EXISTS movie(title,year,score)") # här skapas en databas-tabell

res = cur.execute("SELECT title FROM movie")
print(res.fetchone())

res = cur.execute("SELECT title FROM movie WHERE title='spam'")
print(res.fetchall())


