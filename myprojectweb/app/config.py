import os

# Configuración para la base de datos SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///TaskDB.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Parámetros de conexión a la base de datos de Microsoft Access
ACCESS_DATABASE_CONNECTION_STRING = (
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    'DBQ=C:\\Users\\jorge\\OneDrive\\Documentos\\universidad\\Buenas practicas de desarrollo\\RUBRICA\\myprojectweb\\TaskDB.accdb;'
)

