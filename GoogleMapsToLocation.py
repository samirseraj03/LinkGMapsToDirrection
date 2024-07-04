import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


file = pd.read_csv(r'localizaciones.csv')
f = open("Direciones.csv", "a")
for row in file['Localizaciones']:
    print (row)
    #leer los datos
    datos = urllib.request.urlopen(row).read().decode()
    #transofrmar los datos de html a texto
    soupp = BeautifulSoup(datos , 'html.parser' )
    tags = soupp ('meta')
    print ("procesando")
    #geolocilazador de ubicacion opcion 2
    print (tags[-2].get('content'))
    t = tags[-2].get('content')
    f.write(t + "\n")
    
f.close()

    



print ("list hecha ")

    
print ("final")


#df = pd.DataFrame(lista)  
#df.to_csv('C:/Users/sa-se/Desktop/direcion/hola.csv')