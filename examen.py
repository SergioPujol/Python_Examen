from libro import Libro
from autor import Autor

def get_list(fichero):
    dic = {}
    f = open(fichero, mode="rt", encoding="utf-8")

    if len(open(fichero, mode="rt", encoding="utf-8").read()) < 1:
        raise ValueError("El fichero esta vacio")
    
    for linea in f:
        listaPalabras = linea.split()
        for palabra in listaPalabras:
            try:
                if(dic[len(palabra)].count(palabra) == 0):
                    dic[len(palabra)].append(palabra)
            except:
                dic[len(palabra)] = []
                dic[len(palabra)].append(palabra)


    print(dic)

def mas_antiguos(libros, anyo):

    if int(anyo) < 1900 or int(anyo) > 2021:
        raise ValueError("El anyo no es valido")

    lista = []
    for libro in libros:
        if not int(libro.get_anyo()) > int(anyo):
            lista.append(libro.get_titulo())
    return lista

