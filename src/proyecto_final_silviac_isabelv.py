import pandas as pd
#import os

# 1. Se realiza la carga de los datos con el uso el URL datos cargados 
# en el GitHub

precip = ('https://raw.githubusercontent.com/silviamcm/prueba2/'
          'refs/heads/main/csv/precip.csv')

temp =('https://raw.githubusercontent.com/silviamcm/'
       'prueba2/refs/heads/main/csv/temp.csv')


#Se crean los dataframe de precipitación, temperatura, e índice mei  a las variables 
#establecidas para el respectivas modificaciones y analisis correspondiente
df_precip = pd.read_csv(precip)
df_temp = pd.read_csv(temp)
#df_mei = pd.read_csv(mei)

# 2. Información básica del dataset 

#print(df_precip.head())
#print(df_temp.head())
#print(df_mei)

#-- ddff..iinnffoo(())
#print(f'La información de precipitación es:{df_precip.info()}')
#print(f'La información de temperaura es:{df_temp.info()}')
#-- ddff..ddeessccrriibbee(())
#-- ddff..sshhaappee
#

#Se implementa la aplicación de la función df.describe
print(f)
print(df_temp.describe())





