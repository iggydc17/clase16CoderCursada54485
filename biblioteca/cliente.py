import biblioteca
import json
import os


class Cliente():
    def __init__(self, nombre_usuario, nombre, apellido, email, password):
        self.nombre_usuario = nombre_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.usuarios = {}
        self.registro_usuarios_file = os.path.dirname(__file__) + '/datos/registro_usuarios.json'
        self.sesion_iniciada = False
        self.pago = False




    def cliente_menu(self):
        while True:

            opcion = input('\nElija una opcion: '
                           '\n[1] Registrar nuevo usuario.'
                           '\n[2] Iniciar sesión.'
                           '\n[3] Cerrar sesión.'
                           '\n[4] Ver catalogos productos.'
                           '\n[5] Filtrar productos especificos.'
                           '\n[6] Finalizar.'
                           '\nDigite la opción: ')
            if opcion == '1':
                cliente.registrar_usuario()
            elif opcion == '2':
                cliente.login()
            elif opcion == '3':
                cliente.cerrar_sesion()
            elif opcion == '4':
                try:
                    biblioteca.biblio.mostrar_catalogos_completos()
                except AttributeError:
                    biblioteca.biblioteca.biblio.mostrar_catalogos_completos()
            elif opcion == '5':
                try:
                    biblioteca.biblio.filtro_busqueda()
                except AttributeError:
                    biblioteca.biblioteca.biblio.filtro_busqueda()
            elif opcion == '6':
                cliente.cerrar_sesion()
                print('\nGracias, vuelva pronto.')
                break
            else:
                print('Opción no disponible. Inténtelo de nuevo.')



    def registrar_usuario(self):
        try:
            with open(self.registro_usuarios_file, 'r') as file:
                    diccionario = json.load(file)

        except:
            diccionario = {}
            with open(self.registro_usuarios_file, 'w') as file:
                file.write(json.dumps(diccionario) + '\n\n')
        print('\n**** Registro de usuarios ****\n')

        while True:
            nombre_usuario = input('Ingrese su nombre de usuario (Mayor a 6 caracteres, menor a 12 y sin espacios): ')
            if ' ' in nombre_usuario:
                print('Espacio detectado, intentelo de nuevo.')
                continue
            elif len(nombre_usuario) < 6 or len(nombre_usuario) > 12:
                print('El nombre de usuario no respeta la cantidad de caracteres. Vuela a intentarlo.')
                continue
            else:
                print('Nombre de usuario aprobado.')
                break

        while True:
            try:
                nombre = input('\nIngrese su nombre: ').capitalize()
                apellido = input('Ingrese su apellido: ').capitalize()
                if nombre.isalpha() and apellido.isalpha():
                    break
                else:
                    print('Nombre no válido, inténtelo nuevamente.')
            except ValueError:
                continue

        while True:
            email = input("\nIngrese su mail (únicamente direcciones de gmail): ")
            if "@gmail.com" not in email:
                print('Mail no permitido, únicamente direcciones de correo gmail. Inténtelo de nuevo.')
                continue
            else:
                print('Correo electrónico aprobado.')
                break

        while True:
            password = input('\nIngrese su contraseña (mínimo 6 caracteres, máximo 12, al menos 1 número): ')
            if len(password) < 6 or len(password) > 12:
                print('La contraseña no cumple con la cantidad de caracteres. Vuelva a intentarlo.')

            contiene_numero = False
            for num in password:
                if num.isdigit():
                    contiene_numero = True
                    break
            if not contiene_numero:
                print('Olvidó poner un número en su contraseña. Inténtelo de nuevo.')
                continue

            password_check = input('Escriba nuevamente su contraseña para corroborar autenticidad: ')
            if password_check == password:
                print('Contraseña aprobada.')
                break
            else:
                print('Sus contraseñas no coinciden. Inténtelo de nuevo.')

        nuevo_usuario = {
            'nombre_usuario': nombre_usuario,
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'password': password
        }

        diccionario[nombre_usuario] = nuevo_usuario

        with open(self.registro_usuarios_file, 'w') as file:
            json.dump(diccionario, file, indent=2)

        print(f'\nRegistro exitoso! Hola {nombre_usuario}, bienvenido a la biblioteca!!!')



    def login(self):
        try:
            with open(self.registro_usuarios_file) as file:
                contenido = json.load(file)
        except FileNotFoundError:
            pass

        print('\n\n_________Iniciar Sesión_________:')
        while True:
            username = input('\nIngrese su nombre de usuario: ')
            for key, value in contenido.items():
                if key == username:
                    password = input('Ingrese su contraseña: ')
                    for k, v in value.items():
                        if k == "password":
                            if password == v:
                                print('\nAcceso aprobado! Bienvenido!')
                                self.sesion_iniciada = True
                                return
                            else:
                                print('Error, contraseña incorrecta. Inténtelo de nuevo.')
                elif key != username:
                    continue
                else:
                    print('Error, usuario no registrado. Inténtelo de nuevo.')


    def cerrar_sesion(self):
        self.sesion_iniciada = False
        print('\nSesión cerrada.')


"""class Carrito:
    def __init__(self):
        self.catalogo_libros_file = "datos/catalogo_libros.json"    #### TERMINAR
        self.catalogo_revistas_file = "datos/catalogo_revistas.json"
        self.catalogo_periodicos_file = "datos/catalogo_periodicos.json"
        self.pagado = False

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto} agregado al carrito.")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"{producto} eliminado del carrito.")
        else:
            print(f"{producto} no está en el carrito.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(producto)
        else:
            print("El carrito está vacío.")

    def vaciar_carrito(self):
        self.productos = []
        print("El carrito se ha vaciado.")

    def pagar(self):
        self.pagado = True
        print('Pago realizado con éxito.') """

"""
    def menu_carrito(self):
        while True:
            opcion = input('\nCarrito de compras: '
                           '\n[1] Agregar producto.'
                           '\n[2] Eliminar producto.'
                           '\n[3] Mostrar productos en el carrito con precio total.'
                           '\n[4] Vaciar carrito.'
                           '\n[5] Pagar.'
                           '\n[6] Volver al menú principal.'
                           '\nDigite la opción: ')
            if opcion == '1':
                self.agregar_producto_carrito()
            elif opcion == '2':
                self.eliminar_producto_carrito()
            elif opcion == '3':
                self.mostrar_productos_carrito()
            elif opcion == '4':
                self.vaciar_carrito()
            elif opcion == '5':
                self.pagar()
            elif opcion == '6':
                break
            else:
                print('Opción no disponible. Inténtelo de nuevo.')

    def agregar_producto_carrito(self):
        nombre_producto = input('Ingrese el nombre del producto: ')
        self.carrito.agregar_producto(nombre_producto)

    def eliminar_producto_carrito(self):
        nombre_producto = input('Ingrese el nombre del producto a eliminar: ')
        self.carrito.eliminar_producto(nombre_producto)

    def mostrar_productos_carrito(self):
        self.carrito.mostrar_productos()

    def vaciar_carrito(self):
        self.carrito.vaciar_carrito()

    def pagar(self):
        self.pago = True
        print('Pago realizado con éxito.')

"""
cliente = Cliente(None, None, None, None, None)

if __name__ == '__main__':
    print(r"Usted está en el modulo 'CLIENTES'")
    cliente.cliente_menu()
