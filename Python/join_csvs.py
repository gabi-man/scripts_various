import os
import pandas as pd

maindf = pd.DataFrame()


for filename in os.listdir('./CSV'):
    if filename[-13:] == 'ocupation.csv':
        df = pd.read_csv(os.path.join('./CSV', filename))
        if maindf.empty:
            maindf = df
        else:
            maindf = pd.concat([df, maindf])

maindf.to_excel(excel_writer='ocupacion.xlsx', sheet_name='ocup', na_rep='', float_format='%.2f')

#nótese que debe tener un subfolder "./CSV" en el path donde se ejecute.
#Hay que instalar ademas de panda (para trabajar con los .csv) y openpyxl para que pueda grabar el excel
