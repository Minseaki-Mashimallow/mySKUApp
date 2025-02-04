import sqlite3

dbloc = "../skudb.db"

def LoadDB():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM *")
    res = res.fetchall()
    con.close()
    return res

def AddSKU():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute();
    con.commit()
    con.close()

