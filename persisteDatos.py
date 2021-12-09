from datetime import datetime
from pymongo import MongoClient
from pathlib import Path


#conexión:
#con = MongoClient('localhost',27017)  #conexión local
#ca = Path(certifi.where())
#ca = certifi.where()
con = MongoClient('mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority')
db = con.datosprueba
propiedades = db.propiedades

def guardaDatos(data):
    fecha = data['fecha']
    fechaConvertida = datetime.fromisoformat(fecha)
    data['fecha'] = fechaConvertida
    propiedades.insert_one(data)