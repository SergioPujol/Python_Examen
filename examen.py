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
    for linea in f:
        listaPalabras = linea.split()
        print(listaPalabras)
        for palabra in listaPalabras:
            if dic[len(palabra)] == list
            print("Palabra " + palabra + " con longitud "+ str(len(palabra)))
            #dic[len(palabra)].append(palabra)

    print(dic)
    

get_list("palabras.txt")
