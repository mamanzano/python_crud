def add_clients(list,client):
    list.append(client)
    return list

if __name__ == '__main__':
    list = ['Mario','Jose','Adriana']

    #print('Hola')
    #print(list)
    clients = add_clients(list,'Alonso')

    print('Mis clientes favs:')
    for client in clients:
        print(client)