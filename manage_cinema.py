from pprint import pprint as pp

class Cinema:

    def __init__(self,rows,seats_per_row):
        """
        Args:
            rows: filas de la sala
            seats_per_row: butacas de cada fila    
        """
        self.__rows = rows
        self.__seats_per_row = seats_per_row
        self.__seating = []
    
    def create_cinema_seating(self):
        """
        Inicializa el seating de la sala, que es una lista de diccionarios.
          - Cada elemento de la lista representa una fila de butacas, empezando por la fila 0 que esta en la posicion 0.
          - Cada fila tiene un diccionario para representar las butacas de esa fila.
          - Las claves del diccionario son cada una de las butacas de esa fila (1, 2, 3, etc.).
        """     
        for j in range(1, self.__rows+1):
            row = { i : None for i in range(1, self.__seats_per_row+1) }  
            self.__seating.append(row)
        
    def print_seating(self):
        """
        Imprime el seating de la sala
        """
        pp(self.__seating)

    def book_seat(self,row,seat):
        """
        Marca una butaca como ocupada.
        Args:
            row: la fila de la butaca
            seat: el numero de la butaca
        """
        if self.__seating[row][seat] is None:
            self.__seating[row][seat] = "occupied"

    def count_free_seats(self,rows_seats,total):
        """
        Calcula la cantidad de butacas libres que hay en una lista
        Args:
            rows_seats: lista de butacas a buscar
            total: valor inicial donde se acumulará el total
        """
        for row, seat in rows_seats:
            if self.__seating[row][seat] is None:
                total+=1

        return total

#------------------------------------------- MAIN -----------------------------------------------
cinema = Cinema(rows=10, seats_per_row=8)

#ERROR 1: al reservar una butaca (p.e. fila 2 butaca 4) e imprimir el seating, veo que aparece como ocupada la 4 de cada fila, y no solo de la fila 2.
print("------------- Error 1 -----------------")
cinema.create_cinema_seating()
cinema.book_seat(2,4)
cinema.print_seating()
# El error aparece porque se esta asignando la misma istancia de diccionario a cada posicion de la lista
# Se ha solucionado cambiando el metodo create_cinema_seating, de forma que por cada posicion de la lista, se crea una nueva instancia de diccionario

#ERROR 2: le paso la lista de "seats" donde debería haber 2 libres y me dice que hay 0.
print("\n------------- Error 2 -----------------")
seats = [(2,4), (3,1), (5,2)]
total = 0
res = cinema.count_free_seats(seats,total)
print("total: "+str(res))
# El error aparece porque el total no se devuelve la variable total, entonces el valor de la variable total se quedará en como se ha establecido, es decir en 0
# Se ha solucionado cambiando el metodo count_free_seats para que al final de esta funcion devuelva el total de asientos libres

#ERROR 3: quiero modificar la butaca (2,4) de la lista anterior para que sea la (3,4) y no me deja.
print("\n------------- Error 3 -----------------")
seats[0]= (3,4)
total = 0
res = cinema.count_free_seats(seats,total)
print("total: "+str(res))
# El error aparece porque el valor que le introduces a la tupla no se puede modificar una vez instanciado
# Por ello, la solucion es asignar una nueva tubla con los valores que se deseen establecer, en este caso (3,4)
        
