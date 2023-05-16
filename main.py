from restaurant import add_dish, add_order, add_table, get_count_of_table, get_last_version, get_orders_of_table, restaurant_program_action


if __name__ == '__main__':
    states = {
        '1.0': {
            'pedidos': [
                {
                    'mesa': 1,
                    'nombre': 'Ceviche',
                    'cantidad': 2,
                    'monto': 40,
                },
                                {
                    'mesa': 1,
                    'nombre': 'Ceviche',
                    'cantidad': 2,
                    'monto': 80,
                },
            ],
            'mesas': [
                {
                    'numero': 1,
                    'cantidad_sillas': 4,
                },
                {
                    'numero': 2,
                    'cantidad_sillas': 4,
                }
            ],
            'platos': [
                {
                    'nombre': 'Ceviche',
                    'precio': 20,
                },
                {
                    'nombre': 'Lomo Saltado',
                    'precio': 25,
                }
            ]
        }
    }

    versions = ['1.0']

    while(True):
        print('¿Qué desea hacer?')
        print('1.- Agregar un plato')
        print('2.- Agregar una mesa')
        print('3.- Agregar un pedido')
        print('4.- Ver la cuenta de una mesa')
        print('5.- Ver los pedidos de una mesa')
        print('6.- Salir')

        action = input()

        if action == '1':
            nombre_plato = input('Nombre del plato: ')
            precio_plato = float(input('Precio del plato: '))

            new_dish = restaurant_program_action({
                'function': add_dish,
                'params': {
                    'states': states,
                    'last_version': restaurant_program_action({
                        'function': get_last_version,
                        'params': {
                            'versions': versions,
                        }
                    }),
                    'versions': versions,
                    'nombre_plato': nombre_plato,
                    'precio_plato': precio_plato,
                }
            })

            print(f'Nuevo plato agregado: {new_dish}')
        
        elif action == '2':
            numero_mesa = int(input('Número de mesa: '))
            cantidad_sillas = int(input('Cantidad de sillas: '))

            new_table = restaurant_program_action({
                'function': add_table,
                'params': {
                    'states': states,
                    'last_version': restaurant_program_action({
                        'function': get_last_version,
                        'params': {
                            'versions': versions,
                        }
                    }),
                    'versions': versions,
                    'numero_mesa': numero_mesa,
                    'cantidad_sillas': cantidad_sillas,
                }
            })
            
            print(f'Nueva mesa agregada: {new_table}')

        elif action == '3':
            numero_mesa = int(input('Número de mesa: '))
            nombre_plato = input('Nombre del plato: ')
            cantidad = int(input('Cantidad: '))

            new_order = restaurant_program_action({
                'function': add_order,
                'params': {
                    'states': states,
                    'last_version': restaurant_program_action({
                        'function': get_last_version,
                        'params': {
                            'versions': versions,
                        }
                    }),
                    'versions': versions,
                    'numero_mesa': numero_mesa,
                    'nombre_plato': nombre_plato,
                    'cantidad': cantidad,
                }
            })

            print(f'Nuevo pedido agregado: {new_order}')

        elif action == '4':
            numero_mesa = int(input('Número de mesa: '))

            count = restaurant_program_action({
                'function': get_count_of_table,
                'params': {
                    'states': states,
                    'last_version': restaurant_program_action({
                        'function': get_last_version,
                        'params': {
                            'versions': versions,
                        }
                    }),
                    'numero_mesa': numero_mesa,
                }
            })

            print(f'La cuenta de la mesa es: {count}')

        elif action == '5':
            numero_mesa = int(input('Número de mesa: '))

            orders = restaurant_program_action({
                'function': get_orders_of_table,
                'params': {
                    'states': states,
                    'last_version': restaurant_program_action({
                        'function': get_last_version,
                        'params': {
                            'versions': versions,
                        }
                    }),
                    'numero_mesa': numero_mesa,
                }
            })

            print(f'Pedidos de la mesa {numero_mesa}: {orders}')

        elif action == '6':
            break

        
        
 