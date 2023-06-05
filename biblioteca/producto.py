import biblioteca


class Producto:
    def __init__(self, titulo=None, autor=None, anio=None, genero=None, id=None, precio=None, numero_paginas=None, cantidad=None):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.id = id
        self.precio = precio
        self.numero_paginas = numero_paginas
        self.cantidad = cantidad

    def producto_menu(self):
        while True:
            opcion = input('\nElija una opcion: '
                           '\n[1] Mostrar catálogos de los productos.'
                           '\n[2] Filtrar búsqueda en los catálogos.'
                           '\n[3] Salir del menú.'
                           '\nDigite la opción: ')

            if opcion == '1':
                try:
                    biblioteca.biblio.mostrar_catalogos_completos()
                except AttributeError:
                    biblioteca.biblioteca.biblio.mostrar_catalogos_completos()
            elif opcion == '2':
                try:
                    biblioteca.biblio.filtro_busqueda()
                except AttributeError:
                    biblioteca.biblioteca.biblio.filtro_busqueda()
            elif opcion == '3':
                print('Fin del programa.')
                break
            else:
                print('Opción incorrecta, intentelo de nuevo.')



class Libro(Producto):
    def __init__(self, titulo=None, autor=None, anio=None, genero=None, id=None, precio=None, numero_paginas=None, cantidad=None):
        super().__init__(titulo, autor, anio, genero, id, precio, numero_paginas, cantidad)

    def mostrar_catalogo(self):
        pass


class Revista(Producto):
    def __init__(self, titulo=None, autor=None, anio=None, genero=None, id=None, precio=None, numero_paginas=None, cantidad=None, editor=None, categoria=None, fecha=None):
        super().__init__(titulo, autor, anio, genero, id, precio, numero_paginas, cantidad)
        self.editor = editor
        self.categoria = categoria
        self.fecha = fecha

    def mostrar_catalogo(self):
        pass


class Periodico(Revista):
    def __init__(self, titulo=None, autor=None, anio=None, genero=None, id=None, precio=None, numero_paginas=None, cantidad=None, editor=None, categoria=None, fecha=None):
        super().__init__(titulo, autor, anio, genero, id, precio, numero_paginas, cantidad, editor, categoria, fecha)
        self.fecha = fecha

    def mostrar_catalogo(self):
        pass


productos = Producto()
if __name__ == '__main__':
    print(r"Usted está en el modulo 'PRODUCTOS'")

    productos.producto_menu()


