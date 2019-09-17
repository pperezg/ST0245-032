import pprint
dict = {}

def insertCompanyAux(companyName, companyCoutry, hash_tbl):
    hash_tbl[companyName] = companyCoutry

def deleteCompanyAux(companyName, hash_tbl):
    del hash_tbl[companyName]

def searchCompanyAux(companyName, hash_tbl):
    print(hash_tbl[companyName])

def insertCompany(companyName, companyCoutry):
    insertCompanyAux(companyName, companyCoutry, dict)

def deleteCompany(companyName):
    deleteCompanyAux(companyName, dict)

def searchCompany(companyName):
    searchCompanyAux(companyName, dict)

insertCompany('Google','Estados Unidos')
insertCompany('La locura','Colombia')
insertCompany('Nokia','Finlandia')
insertCompany('Sony','Japon')
pprint.pprint(dict)
