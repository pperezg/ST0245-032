import pprint
dict = {}

def insertContactAux(contact_name, contact_number, hash_tbl):
    hash_tbl[contact_name] = contact_number

def deleteContactAux(contact_name, hash_tbl):
    del hash_tbl[contact_name]

def searchContactAux(contact_name, hash_tbl):
    print(hash_tbl[contact_name])

def insertContact(contact_name, contact_number):
    insertContactAux(contact_name, contact_number, dict)

def deleteContact(contact_name):
    deleteContactAux(contact_name, dict)

def searchContact(contact_name):
    searchContactAux(contact_name, dict)

insertContact('Santiago Cartagena', 3210000)
insertContact('Mauricio Jaramillo', 3168417)
deleteContact('Mauricio Jaramillo')
searchContact('Santiago Cartagena')
pprint.pprint(dict)
