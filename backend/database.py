import sqlite3
import ast
import sys, os

if getattr(sys, 'frozen', False):
    dbloc = "_internal/skudb.db"
    application_path = sys._MEIPASS
else:
    dbloc = "backend/skudb.db"
    application_path = os.path.dirname(os.path.abspath(__file__))

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
    res = cur.execute("SELECT ATTRIBUTES FROM SKUMODEL WHERE SKUMODEL = '{model}'".format(model = model_name)).fetchone()
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
    cur.execute("""INSERT INTO SKUMODEL (SKUMODEL, SKUFAMILY, SKUCATEGORY, ATTRIBUTES)
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
        for attribute_name in res:
            current_res = cur.execute("SELECT PARAMETERS FROM ATTRIBUTE WHERE ATTRIBUTENAME = '{}'".format(attribute_name)).fetchone()
            listing = []
            current_res = ''.join(current_res)
            current_res = str(current_res).replace("'", "")
            current_res = current_res.replace("[", "")
            current_res = current_res.replace("]", "")
            current_res = current_res.split(", ")
            for y in current_res:
                listing.append(y)
            res_dict[attribute_name] = listing
        return res_dict
    except:
        return res_dict

def LoadAttribute(attribute_name):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()

    listing = []
    res = cur.execute("SELECT PARAMETERS FROM ATTRIBUTE WHERE ATTRIBUTENAME ='{}'".format(attribute_name)).fetchone()
    for x in res:
        res = ''.join(res)
        res = str(res).replace("'", "")
        res = res.replace("[", "")
        res = res.replace("]", "")
        res = res.split(", ")
        for y in res:
            listing.append(y)
        return listing

""" ONE TIME USE FUNCTION FOR INSERTING ALL SKUDESCRIPTIONS INTO THE DATABASE """
def InsertDescriptions(skus):
    
    con = sqlite3.connect(dbloc)
    cur = con.cursor()

    for x in skus:
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


def UpdateAttributes(attributes, attribute_name):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    query = 'UPDATE ATTRIBUTE SET PARAMETERS=? WHERE ATTRIBUTENAME=?'
    cur.execute(query, (str(attributes[attribute_name]), attribute_name)) 
    con.commit()
    con.close()
    

def AddDescription(description):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    cur.execute(f"INSERT INTO SKUDESCRIPTION (SKUDESCRIPTION) VALUES ('{description}')") 
    con.commit()
    con.close()
