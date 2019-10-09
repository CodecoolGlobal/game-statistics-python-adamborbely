
# Printing functions

# Report functions

def count_games(file_name):
    
    with open(file_name, "r") as f:
        for value, line in enumerate(f):
            pass
    return value + 1

print("The file contains ", count_games("game_stat.txt"), "games.")

def decide(file_name, year):
    
    games = []
    release_date = 2
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if games[i][release_date] == str(year):
            return True
    return False

realease_year = int(input("What year do you want to check? "))
if decide("game_stat.txt", realease_year) == True:
    print("There is a game from that year.")
else:
    print("No game from the given year.")

def get_latest(file_name):
    
    games = []
    title = 0
    release_date = 2
    result =""
    maximum = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    for i in range(len(games)):
        if int(games[i][release_date]) > maximum:
            result = games[i][title]
            maximum = int(games[i][release_date])

    return result

print("The latest game is:", get_latest("game_stat.txt"))

def count_by_genre(file_name, genre):
    
    games = []
    game_type = 3
    counter = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))
    for i in range(len(games)):
        if games[i][game_type] == genre:
            counter += 1
   
    return counter 

genre_check = input("What genre you want to count? ")
print("The file countains", count_by_genre("game_stat.txt", genre_check), genre_check, "games.")

def get_line_number_by_title(file_name, title):
    
    games = []
    game_title = 0
    result = None
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if games[i][game_title] == title: 
            result = i + 1

    if result != None:
        return result
    else:
        raise ValueError

title_check = input("Which game are you searching for? ")
print("The game is in the following line:",get_line_number_by_title("game_stat.txt", title_check))

def sort_abc(file_name):
    
    games = []
    games_ordered = []
    game_title = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    while games:
        min_index = 0
        minimum = games[0][game_title]
        for i in range(len(games)):
            if games[i][game_title] < minimum:
                minimum = games[i][game_title]
                min_index = i
        games_ordered.append(minimum)
        games.remove(games[min_index])
    return (games_ordered)
print()
print("The file contains the following games:\n")
for i in sort_abc("game_stat.txt"):
    print(i)

def get_genres(file_name):


    games = []
    genres = []
    genre = 3
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    while games:    
        min_index = 0
        minimum = games[0][genre]
        for i in range(len(games)):
            if games[i][genre] < minimum:
                minimum = games[i][genre]
                min_index = i
        games.remove(games[min_index])
        if minimum not in genres:
            genres.append(minimum)
    return genres
    
print()
print("The games are the following genres:\n")
for i in get_genres("game_stat.txt"):
    print(i)

def when_was_top_sold_fps(file_name):

    games = []
    fps = []
    genre = 3
    year = 2
    total_copies = 1
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if games[i][genre] == "First-person shooter":
            fps.append(games[i])

    if fps == []:
        raise ValueError
    
    maximum = float(fps[0][total_copies])
    result = ""
    for i in range(len(fps)):
        if float(fps[i][total_copies]) > maximum:
            maximum = float(fps[i][total_copies])
            result = fps[i][year]

    return int(result)

print("The top sold first person shooter game was released in", when_was_top_sold_fps("game_stat.txt"),end=".""\n")

    

