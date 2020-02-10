import csv
import zipfile
import pandas as pd
from androguard.misc import AnalyzeAPK

# Select file 
# Use skiprows to choose starting point and nrows to choose number of rows
data = pd.read_csv('benign_dir_2017.csv', skiprows = 342, nrows=1200)


# Criar um CSV com permissoes
csv_base =  open('benign_342_2017_All.csv','w', newline='')
writer = csv.writer(csv_base)
writer.writerow(('Numero','Name','Permissions','Provider','Services','SINT','Receivers','RINT'))


# MY helper to extrac intents
def helper(obj,itemtype):
    alista =[]
    for name in obj:
            for action,intent_name in a.get_intent_filters(itemtype, name).items():
                        for intent in intent_name:
                                alista.append(intent)
    return alista



i = 0
while i < 1200:
    file =  (data.iloc[i][0])
    numero = (data.iloc[i][1])
    try:
        a, d, dx = AnalyzeAPK(file)
        print ("===> "+ file + " <===")
        perms =  (a.get_permissions())
        prov = (a.get_providers())
        serv = (a.get_services())
        sint = helper(serv,'service')
        receivers = a.get_receivers()
        r = []
        for x in receivers: r.append(x) 
        rint = helper(receivers,'receiver')
        writer.writerow((numero,file,perms,prov,serv,sint,r,rint))
        csv_base.flush()
    except zipfile.BadZipFile: # WiNDOWS FILE
        print ('THEY TRY 2 GET ME' + str(numero) )
    except KeyError: # DIC ERROR
            print('FUCK ====>' + str(numero))
    except TypeError:
            print ('Really ====>' + str(numero))

    print ("===> "+ str(numero) + " <===")
    i = i + 1



####
###https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
###