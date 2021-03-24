# get_list 
"""
Reciba el nombre de un fichero de palabras y devuelva
un diccionario donde la clave de cada elemento sea un n´umero 1, 2, 3 y el valor sea una lista
con las palabras del fichero que tienen esa longitud. Si una palabra aparece repetida, solo se
tendr´a en cuenta una. En cada l´ınea del fichero puede haber m´as de una palabra. Si se le
pasa un fichero que no tiene ninguna palabra, la funci´on emitir´a una excepci´on ValueError
indicando que el fichero est´a vac´ıo
"""

def get_list(fichero):
    dic = {}
    f = open(fichero, mode="rt", encoding="utf-8")

    #texto = f.read()
    """if len(f) < 1:
        raise ValueError("El fichero está vacío")
    """
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
    

get_list("palabras.txt")
#get_list("texto_vacio.txt")
