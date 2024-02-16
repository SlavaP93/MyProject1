server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_data, i_cl in server_data.items():
    print(f'{i_data}:')
    for dm, cl in i_cl.items():
        print(f' {dm}: {cl}')
