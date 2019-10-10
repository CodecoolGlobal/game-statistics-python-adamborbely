
# Report functions

def get_most_played(file_name):
   
    games = []
    sold = 1
    title = 0
    
    with open("game_stat.txt", "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    
    maximum = float(games[0][sold])
    result = games[0][title]
    for i in range(len(games)):
        if float(games[i][sold]) > maximum:
            maximum = float(games[i][sold])
            result = games[i][title]
    return result


def sum_sold(file_name):
    games = []
    sold = 1
    value = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    
    for i in range(len(games)):
        value += float(games[i][sold])
    return value

def get_selling_avg(file_name):
    games = []
    value = 0
    sold = 1
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        value += float(games[i][sold])

    return value / len(games)

def count_longest_title(file_name):
    games = []
    title = 0
    maximum = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if len(games[i][title]) > maximum:
            maximum = len(games[i][title])

    return maximum

def get_date_avg(file_name):
    games = []
    year = 2
    summ = 0
    with open(file_name,"r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        summ += int(games[i][year])

    return -(-summ // len(games))

def get_game(file_name, title):
    games = []
    result = []
    name = 0
    year = 2
    sold = 1
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if games[i][name] == title:
            for y in (games[i]):
                result.append(y)
            result[sold] = float(result[sold])
            result[year] = int(result[year])
    return result
    
def count_grouped_by_genre(file_name):
    games = []
    result = {}
    genre = 3
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    
    for i in range(len(games)):
        if games[i][genre] not in result:
            result[games[i][genre]] = 1
        else:
            result[games[i][genre]] += 1
    return result   
   
def get_date_ordered(file_name):
    games = []
    year = 2
    title = 0
    result_dict = {}
    tuple_year = 1
    result = []
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    
    while games:
        min_index = 0
        maximum = int(games[0][year])
        for i in range(len(games)):
            if int(games[i][year]) > maximum:
                maximum = int(games[i][year])
                min_index = i
        if games[min_index][year] not in result_dict:
            result_dict[games[min_index][year]] = [games[min_index][title]]
        else:
            result_dict[games[min_index][year]] += [games[min_index][title]]
        games.remove(games[min_index])

    for key, value in sorted(result_dict.items(), reverse=True):
        if len(value) == 1:
            result.append(value[0])
        else:
            while value:
                min_index = value[0]
                for i in range(len(value)):
                    if value[i] < min_index:
                        min_index = value[i]
                result.append(min_index)
                value.remove(min_index)

    return (result)

      

