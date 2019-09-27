import pandas as pd
from sklearn.tree import DecisionTreeRegressor

dta = pd.read_csv("https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/DataSets/train/data_set_train.csv")

def class_counts(rows); #Cuenta en las columnas
    cuenta = {}
    for row in rows:
        label = row[-1]
        if label not in cuenta:
            cuenta[label]=0
        cuenta[label]+=1
    return counts

def imp_gini(rows):
    cuenta = class_counts(rows)
    minuscount = 0;
    for n in rows:
        chanceOfN = counts[n]/len(rows)
        minuscount += chanceOfN**2
    return (1-minuscount)

