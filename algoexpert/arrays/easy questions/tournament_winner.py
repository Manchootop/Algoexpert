def tournamentWinner(competitions, results):
    dict = {}
    for i in range(len(competitions)):
        dict[competitions[i][0]] = 0
        dict[competitions[i][1]] = 0

    for i in range(len(results)):
        if results[i] == 0:
            dict[competitions[i][1]] = dict.get(competitions[i][1]) + 3
        else:
            dict[competitions[i][0]] = dict.get(competitions[i][0]) + 3

    winner = max(dict, key=dict.get)
    return winner
