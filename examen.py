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

listaLibros = []
libro1 = Libro(autor = Autor(id_autor = "1", nombre= "Pedro", apellido= "Pujol"), titulo= "El tesoro 1" , anyo= "2006")
libro2 = Libro(autor = Autor(id_autor = "2", nombre= "Juan", apellido= "Pujol"), titulo= "El tesoro 2" , anyo= "2000")
libro3 = Libro(autor = Autor(id_autor = "3", nombre= "Sergio", apellido= "Pujol"), titulo= "El tesoro 3" , anyo= "2003")
listaLibros.append(libro1)
listaLibros.append(libro2)
listaLibros.append(libro3)
def mas_antiguos(libros, anyo):

    if int(anyo) < 1900

    lista = []
    for libro in libros:
        if not int(libro.get_anyo()) > int(anyo):
            lista.append(libro.get_titulo())
    return lista

get_list("palabras.txt")
print(mas_antiguos(listaLibros, "2004"))
#get_list("texto_vacio.txt")
