import unittest
from examen import *
from libro import Libro
from autor import Autor

class Pruebas (unittest.TestCase):

    def test_lista_libros_devuelta(self):
        
        listaLibros = []
        libro1 = Libro(autor = Autor(id_autor = "1", nombre= "Pedro", apellido= "Pujol"), titulo= "El tesoro 1" , anyo= "2006")
        libro2 = Libro(autor = Autor(id_autor = "2", nombre= "Juan", apellido= "Pujol"), titulo= "El tesoro 2" , anyo= "2000")
        libro3 = Libro(autor = Autor(id_autor = "3", nombre= "Sergio", apellido= "Pujol"), titulo= "El tesoro 3" , anyo= "2003")
        listaLibros.append(libro1)
        listaLibros.append(libro2)
        listaLibros.append(libro3)

        self.assertEqual(mas_antiguos(listaLibros, "2003"), ['El tesoro 2', 'El tesoro 3'])
        self.assertEqual(mas_antiguos(listaLibros, "2004"), ['El tesoro 2', 'El tesoro 3'])
        self.assertEqual(mas_antiguos(listaLibros, "2009"), ['El tesoro 1', 'El tesoro 2', 'El tesoro 3'])


    def test_lista_libros_vacia(self):
        
        listaLibros = []
        libro1 = Libro(autor = Autor(id_autor = "1", nombre= "Pedro", apellido= "Pujol"), titulo= "El tesoro 1" , anyo= "2006")
        libro2 = Libro(autor = Autor(id_autor = "2", nombre= "Juan", apellido= "Pujol"), titulo= "El tesoro 2" , anyo= "2000")
        libro3 = Libro(autor = Autor(id_autor = "3", nombre= "Sergio", apellido= "Pujol"), titulo= "El tesoro 3" , anyo= "2003")
        listaLibros.append(libro1)
        listaLibros.append(libro2)
        listaLibros.append(libro3)

        self.assertEqual(mas_antiguos(listaLibros, "1995"), [])

    def test_anyo_valido(self):
        
        listaLibros = []
        libro1 = Libro(autor = Autor(id_autor = "1", nombre= "Pedro", apellido= "Pujol"), titulo= "El tesoro 1" , anyo= "2006")
        libro2 = Libro(autor = Autor(id_autor = "2", nombre= "Juan", apellido= "Pujol"), titulo= "El tesoro 2" , anyo= "2000")
        libro3 = Libro(autor = Autor(id_autor = "3", nombre= "Sergio", apellido= "Pujol"), titulo= "El tesoro 3" , anyo= "2003")
        listaLibros.append(libro1)
        listaLibros.append(libro2)
        listaLibros.append(libro3)

        self.assertRaisesRegex(ValueError, "El anyo no es valido", mas_antiguos, listaLibros, "1800")


if __name__ == "__main__":
    unittest.main()