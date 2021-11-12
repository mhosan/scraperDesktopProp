from datetime import datetime
from pymongo import MongoClient
from pathlib import Path

#conexión:
con = MongoClient('localhost',27017)  #conexión local
#ca = Path(certifi.where())
#ca = certifi.where()
#con = MongoClient("mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority", tlsCaFile=ca)
#con = MongoClient('mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority')
db = con.datosprueba
super = db.supermercados

def guardaDatos(data, supermercado):
    fecha = data['fecha']
    fechaConvertida = datetime.fromisoformat(fecha)
    precio = data['precio']
    if supermercado == "Dia":
        precio = precio[2:]
    precio = precio.replace(',','.')
    precio = precio.replace('$','')
    precio = precio.strip()
    precioConvertido = float(precio)
    data['fecha'] = fechaConvertida
    data['precio'] = precioConvertido
    super.insert_one(data)