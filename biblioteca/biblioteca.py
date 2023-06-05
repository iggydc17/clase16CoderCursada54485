import json
import os

class Biblioteca:
    def __init__(self):
        self.catalogos = {
            "libro": os.path.dirname(__file__) + '/datos/catalogo_libros.json',
            "revista": os.path.dirname(__file__) + '/datos/catalogo_revistas.json',
            "periodico": os.path.dirname(__file__) + '/datos/catalogo_periodicos.json'
        }
        self.registro_usuarios_file = os.path.dirname(__file__) + '/datos/registro_usuarios.json'

    def biblioteca_menu(self):
        while True:
            opcion = input('\nElija una opción: '
                           '\n[1] Mostrar datos de los usuarios.'
                           '\n[2] Eliminar usuario del registro.'
                           '\n[3] Mostrar catálogos de los productos.'
                           '\n[4] Filtrar búsqueda en los catálogos.'
                           '\n[5] Salir del menú.'
                           '\nDigite la opción: ')

            if opcion == '1':
                biblio.mostrar_datos_usuarios()
            elif opcion == '2':
                biblio.eliminar_usuario()
            elif opcion == '3':
                biblio.mostrar_catalogos_completos()
            elif opcion == '4':
                biblio.filtro_busqueda()
            elif opcion == '5':
                print('\nPrograma finalizado.')
                break
            else:
                print('Opción no disponible. Inténtelo de nuevo.')

    def mostrar_datos_usuarios(self):
        while True:
            mostrar_usuarios = input('\n¿Desea ver el registro de usuarios? (si/no): ')
            if mostrar_usuarios == 'si':
                with open(self.registro_usuarios_file, "r") as file:
                    datos = json.load(file)
                    if len(datos) > 0:
                        for usuario in datos.values():  # Iterar sobre los valores del diccionario
                            print(usuario)  # Imprimir cada usuario
                    else:
                        print("La lista del registro de usuarios se encuentra vacía.")
                break
            elif mostrar_usuarios == 'no':
                break
            else:
                print("Respuesta inválida. Por favor, ingrese 'si' o 'no'.")



    def eliminar_usuario(self):
        with open(self.registro_usuarios_file, "r") as file:
            contenido = json.load(file)

        mal_usuario = input(
            '\n¿Algún usuario infringió las leyes de la biblioteca? ¿Deseas eliminar su suscripción? (si/no): ')
        if mal_usuario.lower() == 'si':
            eliminar_usuario = input('¿Cómo se llama el usuario que deseas eliminar de los registros?: ')
            if eliminar_usuario in contenido:
                del contenido[eliminar_usuario]
                print(f'El usuario {eliminar_usuario} ha sido eliminado del registro.')
            else:
                print(f'El usuario {eliminar_usuario} no existe en los registros.')

        with open(self.registro_usuarios_file, "w") as file:
            json.dump(contenido, file, indent=4)

        verificar_datos = input('¿Desea visualizar los usuarios registrados? (si/no): ')
        if verificar_datos.lower() == 'si':
            with open(self.registro_usuarios_file, "r") as file:
                datos = json.load(file)
                if len(datos) > 0:
                    for usuario in datos:
                        print(usuario)
                else:
                    print("La lista del registro de usuarios se encuentra vacía.")

    def cargar_catalogo(self, tipo_catalogo):
        catalogo_file = self.catalogos.get(tipo_catalogo)
        if catalogo_file:
            with open(catalogo_file, "r") as file:
                catalogo = json.load(file)
                return catalogo
        else:
            print("Opción de catálogo inválida")
            return []

    def imprimir_catalogo(self, catalogo):
        for item in catalogo:
            print(item)

    def mostrar_catalogos_completos(self):
        while True:
            catalogos = input('\n¿Desea visualizar algún catálogo completo? (si/no): ')
            if catalogos == 'si':
                elegir_catalogo = input('¿Qué catálogo desea visualizar? (1: libros, 2: revistas, 3: periódicos): ')
                if elegir_catalogo == '1':
                    catalogo_libros = self.cargar_catalogo("libro")
                    self.imprimir_catalogo(catalogo_libros)
                elif elegir_catalogo == '2':
                    catalogo_revistas = self.cargar_catalogo("revista")
                    self.imprimir_catalogo(catalogo_revistas)
                elif elegir_catalogo == '3':
                    catalogo_periodicos = self.cargar_catalogo("periodico")
                    self.imprimir_catalogo(catalogo_periodicos)
                else:
                    print("Opción inválida. Inténtelo de nuevo.")
            elif catalogos == 'no':
                print('Visualización de catálogos finalizada.')
                break
            else:
                print('Opción inválida. Inténtelo de nuevo.')

    def filtro_busqueda(self):
        while True:
            tipo_producto = input("\nIngrese el tipo de producto a buscar (1: Libro, 2: Revista, 3: Periódico): ")

            if tipo_producto == "1":
                catalogo = self.cargar_catalogo("libro")
                break
            elif tipo_producto == "2":
                catalogo = self.cargar_catalogo("revista")
                break
            elif tipo_producto == "3":
                catalogo = self.cargar_catalogo("periodico")
                break
            else:
                print("No existe ese producto. Inténtelo de nuevo.")

        while True:
            parametro_busqueda = input(
                "Ingrese el parámetro de búsqueda (1: Título, 2: Autor, 3: Año, 4: Género, 5: ID, 6: Precio, 7: número de páginas): ")
            valor_buscado = input("Ingrese el valor a buscar: ")

            productos_encontrados = []
            for producto in catalogo:
                if parametro_busqueda == "1":
                    if producto.get("titulo") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "2":
                    if producto.get("autor") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "3":
                    if producto.get("anio") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "4":
                    if producto.get("genero") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "5":
                    if producto.get("id") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "6":
                    if producto.get("precio") == valor_buscado:
                        productos_encontrados.append(producto)
                elif parametro_busqueda == "7":
                    if producto.get("numero de paginas") == valor_buscado:
                        productos_encontrados.append(producto)
                else:
                    print("Parámetro de búsqueda inválido")
                    return []

            if productos_encontrados:
                print("\nResultados encontrados:")
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")

            while True:
                respuesta = input("\n¿Desea realizar otra búsqueda? (si/no): ")
                if respuesta == "si":
                    biblio.filtro_busqueda()
                elif respuesta == "no":
                    print('\nBúsqueda finalizada.')
                    return
                else:
                    print("Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

    """def menu_manipular_catalogos(self):
        while True:
            opcion = input('\nElija una opción: '
                           '\n[1] Agregar producto al catálogo.'
                           '\n[2] Quitar producto del catálogo.'
                           '\n[3] Ver catálogos completos.'
                           '\n[4] Filtrar búsqueda en los catálogos.'
                           '\n[5] Volver al menú principal.'
                           '\nDigite la opción: ')
            if opcion == '1':
                self.agregar_producto_catalogo()
            elif opcion == '2':
                self.eliminar_producto_catalogo()
            elif opcion == '3':
                self.mostrar_catalogos_completos()
            elif opcion == '4':
                biblio.filtro_busqueda()
            elif opcion == '5':
                print('\nVolver al menú principal.')
                break
            else:
                print('Opción no disponible. Inténtelo de nuevo.')

    def agregar_producto_catalogo(self):
        tipo_catalogo = input("\nElija el tipo de catálogo a agregar (libro/revista/periodico): ")
        catalogo_file = self.catalogos.get(tipo_catalogo)
        if catalogo_file:
            with open(catalogo_file, "r") as file:
                catalogo = json.load(file)

            nuevo_producto = {}
            nuevo_producto['nombre'] = input("Digite el nombre del producto: ")
            nuevo_producto['autor'] = input("Digite el autor del producto: ")
            nuevo_producto['precio'] = input("Digite el precio del producto: ")

            catalogo.append(nuevo_producto)

            with open(catalogo_file, "w") as file:
                json.dump(catalogo, file, indent=4)
                print(f"\nEl producto ha sido agregado al catálogo de {tipo_catalogo}.")
        else:
            print("Opción de catálogo inválida.")

    def eliminar_producto_catalogo(self):
        tipo_catalogo = input("\nElija el tipo de catálogo a eliminar (libro/revista/periodico): ")
        catalogo_file = self.catalogos.get(tipo_catalogo)
        if catalogo_file:
            with open(catalogo_file, "r") as file:
                catalogo = json.load(file)

            producto_eliminar = input("Digite el nombre del producto que desea eliminar: ")
            for item in catalogo:
                if item['nombre'] == producto_eliminar:
                    catalogo.remove(item)
                    print(f"\nEl producto {producto_eliminar} ha sido eliminado del catálogo de {tipo_catalogo}.")
                    break

            with open(catalogo_file, "w") as file:
                json.dump(catalogo, file, indent=4)
        else:
            print("Opción de catálogo inválida.")

    def comprobar_disponibilidad(self):
        codigo_producto = input("Ingrese el ID del producto: ")
        encontrado = False

        for catalogo in self.catalogos:
            for producto in catalogo.productos:
                if producto.codigo == codigo_producto:
                    encontrado = True
                    if producto.stock > 0:
                        print("El producto está disponible.")
                    else:
                        print("El producto está agotado.")
                    break

        if not encontrado:
            print("El producto no existe en ningún catálogo.")
            
            """

biblio = Biblioteca()
if __name__ == '__main__':
    print(r"Usted está en el modulo 'BIBLIOTECA'.")
    biblio.biblioteca_menu()
