
from subprocess import call
from tkinter import ttk, Tk
from tkinter import*
from tkinter import messagebox
from sql import afficher_liste_tables, afficher_liste_alimets, supprimer_table, supprimer_aliment, inserer_table, inserer_aliment

root =Tk()
root.title("vitrines")
root.geometry("1250x1000")
root.resizable(False,False)
root.configure(background="#FF8333")


# Formulaire d'enregistrement des tables
lbltitre =Label(root,borderwidth=3,relief = SUNKEN
,text = "Formulaire d'enregistrement des tables", font = ("Sans Serif",18), background = "#164159",
 foreground="white")
lbltitre.place(x=-5,y= 20, width = 600)


def inserer_tab():
 numero_table = int(txttable.get())
 numero_chaise = int(txtarticle.get())

 if numero_table and numero_chaise:
  inserer_table(numero_table, numero_chaise)




lbtable = Label(root,text="Numéro de table", font=("Sans Serif",14), background = "#164159",
 foreground="white")
lbtable.place(x=10,y= 70, width = 200)

txttable =Entry(root,bd=4,font=("Arial", 14))
txttable.place(x=200,y=70,width=150)


lblchaise = Label(root,text="Numéro des chaiess", font=("Sans Serif",14), background = "#164159",
 foreground="white")
lblchaise.place(x=10,y= 120, width = 200)

txtarticle =Entry(root,bd=4,font=("Arial", 14))
txtarticle.place(x=200,y=120,width=150)

def supprimer_ligne_table():
 selected_item = table.selection()
 if selected_item:
  # Récupère les valeurs de la ligne sélectionnée
  item = table.item(selected_item)
  values = item['values']
  print(values[0], values[1])
  # Supprime la ligne de la base de données
  supprimer_table(values[0], values[1])

  # Supprime la ligne de la table Treeview
  table.delete(selected_item)



# Table
table = ttk.Treeview(root, columns= (1,2), height = 10, show= "headings")
table.place(x = 550, y= 60,width = 800, height = 200)
table.heading(1, text= "NUMERO TABLE")
table.heading(2, text= "NUMERO DE CHAISE")


# Récupère les nouvelles données et les insère dans la table
rows = afficher_liste_tables()
for row in rows:
 table.insert("", "end", values=row)


btnenregistrerTable = Button(root, text = "Enregistrer",command=inserer_tab,font =("Arial",18),bg = "#180461",fg ="white")
btnenregistrerTable.place(x=10, y= 170, width=200)
btnsuprimerTable = Button(root, text = "Supprimer", command=supprimer_ligne_table, font =("Arial",18),bg = "#180461",fg ="white")
btnsuprimerTable.place(x=230, y= 170, width=200)


def inserer_ali():
 code = int(txtcodealiment.get())
 nom = txtnomaliment.get()
 prix = int(txtprixaliment.get())

 inserer_aliment(code, nom, prix)

# définir les dimentions de colones
# Formulaire d'enregistrement des aliments
lbltitreAliment =Label(root,borderwidth=3,relief = SUNKEN
,text = "Formulaire d'enregistrement des aliments", font = ("Sans Serif",18), background = "#164159",
 foreground="white")
lbltitreAliment.place(x=-5,y= 300, width = 600)
lblcodealilent = Label(root,text="Code aliment", font=("Sans Serif",14), background = "#164159",
 foreground="white")
lblcodealilent.place(x=10,y= 350, width = 200)


txtcodealiment =Entry(root,bd=4,font=("Arial", 14))
txtcodealiment.place(x=200,y=350,width=150)
lblnomaliment = Label(root,text="Noms des aliments ", font=("Sans Serif",14), background = "#164159",
 foreground="white")
lblnomaliment.place(x=10,y= 400, width = 200)

txtnomaliment =Entry(root,bd=4,font=("Arial", 14))
txtnomaliment.place(x=200,y=400,width=300)


lblprixaliment = Label(root,text="Prix des aliments ", font=("Sans Serif",14), background = "#164159",
 foreground="white")
lblprixaliment.place(x=10,y= 450, width = 200)


txtprixaliment =Entry(root,bd=4,font=("Arial", 14))
txtprixaliment.place(x=200,y=450,width=100)



def supprimer_ligne_aliment():
 selected_item = tablealiment.selection()
 if selected_item:
  # Récupère les valeurs de la ligne sélectionnée
  item = tablealiment.item(selected_item)
  values = item['values']
  print(values[0])
  # Supprime la ligne de la base de données
  supprimer_aliment(values[0])

  # Supprime la ligne de la table Treeview
  tablealiment.delete(selected_item)

tablealiment = ttk.Treeview(root, columns= (1,2,3), height = 10, show= "headings")
tablealiment.place(x = 550, y=300,width = 800, height = 200)
tablealiment.heading(1, text= "CODE ALIMENT")
tablealiment.heading(2, text= "NOM ALIMENT")
tablealiment.heading(3, text= "PRIX ALIMENT")
# définir les dimentions de colones


# Récupère les nouvelles données et les insère dans la table
rows = afficher_liste_alimets()
for row in rows:
 tablealiment.insert("", "end", values=row)

btnenregistrerAliment = Button(root, text = "Eregistrer", command=inserer_ali,font =("Arial",18),bg = "#180461",fg ="white")

btnenregistrerAliment.place(x=10, y= 500, width=200)


btnsuprimerAliment = Button(root, text = "Supprimer", command=supprimer_ligne_aliment,font =("Arial",18),bg = "#180461",fg ="white")
btnsuprimerAliment.place(x=230, y= 500, width=200)

root.mainloop()
