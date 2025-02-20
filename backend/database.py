import sqlite3
import ast

dbloc = "backend/skudb.db"

""" LOADS ALL CURRENT SKU FAMILIES *** DEPRECATED ***"""
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

""" LOADS ALL CURRENT SKU MODELS *** DEPRECATED ***"""
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

""" LOADS THE MODEL BEING SELECTED *** DEPRECATED ***"""
def LoadModel(model_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    try:
        res = cur.execute("SELECT SKUMODEL FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = model_name)).fetchone()
        return res
    except:
        return "Couldn't find"

""" LOADS THE PARAMETERS OF AN SKU MODEL *** DEPRECATED ***"""
def LoadModelParameters(model_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT PARAMETERS FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = model_name)).fetchone()
    res = ''.join(res)
    res = str(res).replace("'", "")
    res = res.replace("[", "")
    res = res.replace("]", "")
    res = res.split(", ")
    return res

    
""" CREATES AN SKU CATEGORY *** DEPRECATED ***"""
def CreateCategory(category_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    cur.execute("""INSERT INTO SKUCATEGORY (CATEGORY) 
                    VALUES ('{category}')""".format(category = category_name))
    con.commit()
    con.close()

""" CREATES AN SKU FAMILY ***DEPRECATED***"""
def CreateFamily(family_name: str, category_name: str):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    cur.execute("""INSERT INTO SKUFAMILY (SKUFAMILY, SKUCATEGORY)
                    VALUES ('{family}','{category}')""".format(family = family_name, category = category_name))
    con.commit()
    con.close()

""" CREATES AN SKU MODEL *** DEPRECATED ***"""
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
                                                    
""" LOADS ATTRIBUTENAMES """
def LoadAttributeNames():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT ATTRIBUTENAME FROM ATTRIBUTE")
    try:
        res = res.fetchall()
        res = list(map(lambda x: ''.join(x), res))
        return res
    except:
        return []

""" LOADS ALL POSSIBLE ATTRIBUTES WITHIN EACH GROUP OF ATTRIBUTES """
def LoadAttributes():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()

    res = LoadAttributeNames() 
    res_dict = {}
    try:

        for x in res:
            current_res = cur.execute("SELECT PARAMETERS FROM ATTRIBUTE WHERE ATTRIBUTENAME = '{}'".format(x)).fetchone()
            listing = []
            current_res = ''.join(current_res)
            current_res = str(current_res).replace("'", "")
            current_res = current_res.replace("[", "")
            current_res = current_res.replace("]", "")
            current_res = current_res.split(", ")
            for x in current_res:
                listing.append(x)
            res_dict[x] = listing
        return res_dict
    except:
        return res_dict



""" ONE TIME USE FUNCTION FOR INSERTING ALL SKUDESCRIPTIONS INTO THE DATABASE """
def InsertDescriptions(skus):
    
    con = sqlite3.connect(dbloc)
    cur = con.cursor()

    for x in skus:
        print(x)
        try:
            res = cur.execute("""INSERT INTO SKUDESCRIPTION (SKUDESCRIPTION) VALUES ("{}")""".format(x,))
        except:
            res = cur.execute("""INSERT INTO SKUDESCRIPTION (SKUDESCRIPTION) VALUES ('{}')""".format(x,))

    con.commit()
    con.close()

""" LOAD DESCRIPTIONS FROM THE SKUDESCRIPTION TABLE """
def LoadDescriptions():
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    res = cur.execute("SELECT SKUDESCRIPTION FROM SKUDESCRIPTION")
    try:
        res = res.fetchall()
        res = list(map(lambda x: ''.join(x), res))
        return res
    except:
        return []
