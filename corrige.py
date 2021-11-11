from datetime import datetime
from pymongo import MongoClient
from pathlib import Path

#conexión:
#con = MongoClient('localhost',27017)  #conexión local
con = MongoClient('mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority')
db = con.datosprueba
super = db.supermercados

""" db.collection.update(
  {},
  { $rename: { 'name.additional': 'name.last' } },
  { multi: true }
)
"""
#super.find_one_and_replace({'supermercado': 'Wallmart'},{'descripcion': 1}, {'descrip': 1})
documentosActualizar = super.find({"supermercado" : "Wallmart"})
for documento in documentosActualizar:
    id = documento['_id']
    supermercado = documento["supermercado"]
    fecha = documento["fecha"]
    descrip = documento["descripcion"]
    precio = documento["precio"]
    super.delete_one({'_id': id})
    super.insert_one({'supermercado': supermercado, 'fecha': fecha, 'descrip': descrip, 'precio': precio})
    
