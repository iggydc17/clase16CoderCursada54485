from biblioteca import biblioteca, cliente, producto

print(r"Usted está en el modulo de control general del programa.")


class Menu_general:
    def mostrar_menu(self):
        while True:
            opcion = input('\nElija una opcion: '
                           '\n[1] Programa de la Biblioteca.'
                           '\n[2] Programa de Cliente.'
                           '\n[3] Programa Productos.'
                           '\n[4] Finalizar.'
                           '\nDigite una opción: ')
            if opcion == '1':
                print('\n\nUsted está en la sección BIBLIOTECA.')
                biblioteca.biblio.biblioteca_menu()
            elif opcion == '2':
                print('\n\nUsted está en la sección CLIENTE.')
                cliente.cliente.cliente_menu()
            elif opcion == '3':
                print('\n\nUsted está en la sección PRODUCTO.')
                producto.productos.producto_menu()
            elif opcion == '4':
                print('Programa finalizado.')
                break
            else:
                print('Opción incorrecta, intentelo de nuevo.')

if __name__ == '__main__':
    main = Menu_general()
    main.mostrar_menu()