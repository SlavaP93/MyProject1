players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

players = []

for i_team in players_dict:
    if players_dict[i_team]['team'] == 'A' and players_dict[i_team]['status'] == 'Rest':
        players.append(players_dict[i_team]['name'])
        print('Сейчас отдыхают в А: ',players_dict[i_team]['name'])
    elif players_dict[i_team]['team'] == 'B' and players_dict[i_team]['status'] == 'Training':
        players.append(players_dict[i_team]['name'])
        print('Сейчас тренируются в В: ', players_dict[i_team]['name'])
    elif players_dict[i_team]['team'] == 'C' and players_dict[i_team]['status'] == 'Travel':
        players.append(players_dict[i_team]['name'])
        print('Сейчас путишествуют в С: ', players_dict[i_team]['name'])
print(players)
