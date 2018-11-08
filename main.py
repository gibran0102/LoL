from fetch import Fetch


def main(): 
    name = input('Nombre del invocador (solo LAN): ')

    new_search = Fetch(name)

    infor_user = new_search.get_user_info()

    print(infor_user['name'])
    

if __name__ == '__main__': main()