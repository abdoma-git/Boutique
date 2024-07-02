


import sqlite3


connection = sqlite3.connect("database.db")


cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS tables (numero_table INT, numer_chaise INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS aliments (code INT, nom VARCHAR(50) , prix INT)")


def inserer_table(*args):

    cursor.execute("INSERT INTO tables(numero_table, numer_chaise) VALUES(?, ?)", args)

    connection.commit()


def inserer_aliment(*args):

    cursor.execute("INSERT INTO aliments(code, nom, prix) VALUES(?, ?, ?)", args)

    connection.commit()



def afficher_liste_tables():

    cursor.execute("SELECT * FROM tables")

    return cursor.fetchall()


def afficher_liste_alimets():

    cursor.execute("SELECT * FROM aliments")

    return cursor.fetchall()


def supprimer_aliment(id):

    cursor.execute("DELETE FROM aliments WHERE code = ?", (id,))
    connection.commit()


def supprimer_table(t,c):

    cursor.execute("DELETE FROM tables WHERE numero_table = ? AND numer_chaise = ?", (t,c))
    connection.commit()