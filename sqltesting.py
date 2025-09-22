import sqlite3
con = sqlite3.connect("tutorial.db") # här skapas en databasfil
cur = con.cursor()  # em cursor används för att utföra SQL-kommandon

cur.execute("CREATE TABLE IF NOT EXISTS movie(title,year,score)") # här skapas en databas-tabell

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
print(res.fetchone())


