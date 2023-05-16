def restaurant_program_action(args):
    if 'function' in args and 'params' in args:
        return args['function'](args['params'])

def get_last_version(args):
    if 'versions' in args:
        return args['versions'][-1]


def get_count_of_table(args):
    if 'states' in args and 'last_version' in args and 'numero_mesa' in args:
        state = args['states'][args['last_version']]
        return sum([pedido['monto'] for pedido in state['pedidos'] if pedido['mesa'] == args['numero_mesa']])

def get_orders_of_table(args):
    if 'states' in args and 'last_version' in args and 'numero_mesa' in args:
        state = args['states'][args['last_version']]
        return [ {'plato': pedido['nombre'], 'cantidad': pedido['cantidad'], 'monto': pedido['monto']} for pedido in state['pedidos'] if pedido['mesa'] == args['numero_mesa']]

def add_dish(args):
    if 'states' in args and 'last_version' in args and 'versions' in args and 'nombre_plato' in args and 'precio_plato' in args:
        new_version = str(float(args['last_version']) + 1)
        args['versions'].append(new_version)
        args['states'][new_version] = args['states'][args['last_version']].copy()
    
        args['states'][new_version]['platos'].append({
            'nombre': args['nombre_plato'],
            'precio': args['precio_plato'],
        })

        return {
            'nombre': args['nombre_plato'],
            'precio': args['precio_plato'],
        }

def add_table(args):
    if 'states' in args and 'last_version' in args and 'versions' in args and 'numero_mesa' in args and 'cantidad_sillas' in args:
        new_version = str(float(args['last_version']) + 1)
        args['versions'].append(new_version)
        args['states'][new_version] = args['states'][args['last_version']].copy()
    
        args['states'][new_version]['mesas'].append({
            'numero': args['numero_mesa'],
            'cantidad_sillas': args['cantidad_sillas'],
        })

        return {
            'numero': args['numero_mesa'],
            'cantidad_sillas': args['cantidad_sillas'],
        }

def add_order(args):
    if 'states' in args and 'last_version' in args and 'versions' in args and 'numero_mesa' in args and 'nombre_plato' in args and 'cantidad' in args:
        new_version = str(float(args['last_version']) + 1)
        args['versions'].append(new_version)
        args['states'][new_version] = args['states'][args['last_version']].copy()
    
        args['states'][new_version]['pedidos'].append({
            'mesa': args['numero_mesa'],
            'nombre': args['nombre_plato'],
            'cantidad': args['cantidad'],
            'monto': args['cantidad'] * [plato['precio'] for plato in args['states'][args['last_version']]['platos'] if plato['nombre'] == args['nombre_plato']][0],
        })

        return {
            'mesa': args['numero_mesa'],
            'nombre': args['nombre_plato'],
            'cantidad': args['cantidad'],
            'monto': args['cantidad'] * [plato['precio'] for plato in args['states'][args['last_version']]['platos'] if plato['nombre'] == args['nombre_plato']][0],
        }