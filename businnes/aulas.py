import json
import os
from commons.utils import *
def guardarAulas_json():
    try:
      with open(os.path.join("data","Aulas.json"), 'w') as archivo_json:
        json.dump(lista_aulas, archivo_json, indent=2)
        print("La lista de Aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Aulas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def cargarAulas_json():
    try:
        with open(os.path.join("data","Aulas.json"), 'r') as archivo_json:        
            lista_aulas = json.load(archivo_json)
            print("La lista de Aulas ha sido cargada")
            return lista_aulas
    except FileNotFoundError:
        print("El archivo 'Aulas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
lista_aulas = cargarAulas_json()
    

def crearAulas():
    print("Seleccione el aula que desea revisar.")
    AulaNombre = input("Ingrese el nombre del Aula (Grupo): ")
    Ruta = input("Ingrese la Ruta del Aula: ")
    Modulo = input("Ingrese el modulo del Aula: ")
    ZonaEntrenamiento = input("Ingrese Zona de Entrenamiento del Aula: ")
    Trainer = input("Ingrese el trainer asignado al Aula: ")
    camper = {
        'Nombre':AulaNombre,
        'Ruta': Ruta,
        'Modulo': Modulo,
        'Zona de Entrenamiento': ZonaEntrenamiento,
        'Trainer': Trainer,
    }

    lista_aulas.append(camper)
    print("Se creó el aula con éxito")
    guardarAulas_json()

def modificarAulas():
    print("Seleccione el aula que desea revisar.")
    

def buscarAulas():
    print("Listado de campers: ")
    for camper in lista_aulas:
        print(camper)