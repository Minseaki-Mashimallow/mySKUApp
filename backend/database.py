import sqlite3
import ast

dbloc = "backend/skudb.db"

def LoadFamilies():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT SKUFAMILY FROM SKUFAMILY")
    try:
        res = res.fetchall()
        res = list(map(lambda x: ''.join(x), res))
        return res
    except:
        return []

def LoadModels(family_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT SKUMODEL FROM SKUMODEL WHERE SKUFAMILY = '{}'".format(family_name))
    try:
        res = res.fetchall()
        res = list(map(lambda x: ''.join(x), res))
        return res
    except:
        return []

def LoadModel(model_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    try:
        res = cur.execute("SELECT SKUMODEL FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = model_name)).fetchone()
        return res
    except:
        return "Couldn't find"

def LoadModelParameters(model_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT PARAMETERS FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = model_name)).fetchone()
    ast
    res = ''.join(res)
    res = str(res).replace("'", "")
    res = res.replace("[", "")
    res = res.replace("]", "")
    res = res.split(", ")
    print(res)
    return res

    
def CreateCategory(category_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    cur.execute("""INSERT INTO SKUCATEGORY (CATEGORY) 
                    VALUES ('{category}')""".format(category = category_name))
    con.commit()
    con.close()

def CreateFamily(family_name: str, category_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    cur.execute("""INSERT INTO SKUFAMILY (SKUFAMILY, SKUCATEGORY)
                    VALUES ('{family}','{category}')""".format(family = family_name, category = category_name))
    con.commit()
    con.close()

def CreateModel(model_name: str, family_name: str, parameters: list):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    ## Searches for the Category of the Family 
    category = cur.execute("""SELECT SKUCATEGORY FROM SKUFAMILY 
                                WHERE SKUFAMILY = '{fam}'""".format(fam = family_name)).fetchone()[0]
    cur.execute("""INSERT INTO SKUMODEL (SKUMODEL, SKUFAMILY, SKUCATEGORY, PARAMETERS)
                    VALUES('{model}', '{family}', '{category}', "{params}")
                    """.format(model = model_name, family = family_name, category = category, params = parameters))
    con.commit()
    con.close()


    ## TODO: HAVE THIS WORKING
def CreateSKU(sku_model: str, sku_desc: str, parameters: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    
    family = cur.execute("SELECT SKUFAMILY FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = sku_model)).fetchone()
   
    category = cur.execute("SELECT SKUCATEGORY FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = sku_model)).fetchone() 
    temp_code = len(cur.execute("SELECT SKUCODE FROM SKU").fetchall()) + 1
    cur.execute("""INSERT INTO SKU (SKUCODE, SKUFAMILY, SKUMODEL, SKUCATEGORY, SKUDESCRIPTION, SKUPARAMETERS) 
                    VALUES ('{code}', '{familiy}', '{model}', '{category}', '{desc}', '{params}')""")

def TestCreate():
    CreateCategory("Test")
    CreateFamily("TestFam", "Test")
    CreateModel("TestModel", "TestFam", ["Color", "Dimensions"])

