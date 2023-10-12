from GenerarMatriz import generar_y_guardar_matriz
from ReadCSV import cargar_laberinto, imprimir_laberinto, obtener_ruta_matriz_mas_actualizada
from Dijkstra import Dijkstra
from Bellman import Bellman
from BreadthFirstSearch_BFS import BFS
from DepthFirstSearch_DFS import DFS
from AStarSearch import AStar
import os
import time
# from memory_profiler import profile


def menu():
    print("\n\n     ≫ Primer proyecto IA ≪\n\n")

    opc = input("Por favor, digite la opcion que desea escoger: "
                "\n0- Generar otra matriz \n1- Dijkstra \n2- Bellman \n3- Depht First Search (DFS) "
                "\n4- Breadth-First Search (BFS) \n5- A* Search \n6- Salir\n\nOpcion: ")

    match opc:
        case "0":
            print("Elegiste la opcion 0, generar otra matriz\n")
            n = input("Por favor, digite el numero de filas de la matriz: ")
            m = input("Por favor, digite el numero de columnas de la matriz: ")
            generar_y_guardar_matriz(int(n), int(m))
            print("Matriz generada!")

        case "1":
            print("Elegiste la opcion 1, Dijkstra\n")
            cargaCSV("1")

        case "2":
            print("Elegiste la opcion 2, Bellman\n")
            cargaCSV("2")

        case "3":
            print("Elegiste la opcion 3, DFS\n")
            cargaCSV("3")

        case "4":
            print("Elegiste la opcion 4, BFS\n")
            cargaCSV("4")

        case "5":
            print("Elegiste la opcion 5, A * Search\n")
            cargaCSV("5")

        case "6":
            print("Saliendo del programa... \n")
            exit()
        case _:
            print("\n¡Opcion invalida!")
            time.sleep(2)


def cargaCSV(algoritmo):

    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    carpeta_matrices = os.path.join(directorio_actual, 'MatricesGeneradas')
    ruta_archivo = obtener_ruta_matriz_mas_actualizada(carpeta_matrices)
    print("Ruta del archivo:", ruta_archivo)
    
    # Nombre del laberinto utilizado
    nombre_archivo = os.path.basename(ruta_archivo)

    laberinto, inicio, meta = cargar_laberinto(ruta_archivo)
    print("Nombre del laberinto: " + nombre_archivo + "\n\n")
    print("\nLaberinto Inicial:")
    imprimir_laberinto(laberinto)
    print("\nCoordenadas del punto de inicio:", inicio)
    print("Coordenadas del punto final:", meta)

    # este metodo recibe todos los metodos y solo tiene que pasarle a cada uno sus parametros que solicita
    # por ejemplo, "1" es dijkstra, "2" es Bellman y asi sucesivamente
    match algoritmo:
        case "1":
            dijkstra = Dijkstra(laberinto, inicio, meta)
            dijkstra.resolver_laberinto("Dijkstra", nombre_archivo)
        case "2":
            bellman = Bellman(laberinto, inicio, meta)
            bellman.resolver_laberinto("Bellman", nombre_archivo)
        case "3":
            dfs = DFS(laberinto, inicio, meta)
            dfs.resolver_laberinto("Depth First Search", nombre_archivo)
        case "4":
            bfs = BFS(laberinto, inicio, meta)
            bfs.resolver_laberinto("Breadth First Search", nombre_archivo)
        case "5":
            astar = AStar(laberinto, inicio, meta)
            astar.resolver_laberinto("A* Search", nombre_archivo)
        case _:
            print("Incorrecto!")


if __name__ == '__main__':
    while True:
        menu()
