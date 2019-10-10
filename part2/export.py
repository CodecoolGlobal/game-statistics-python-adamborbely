
# Export functions
import reports

result = []

result.append(reports.get_most_played("game_stat.txt"))

result.append(reports.sum_sold("game_stat.txt"))

result.append(reports.get_selling_avg("game_stat.txt"))

result.append(reports.count_longest_title("game_stat.txt"))

result.append(reports.get_date_avg("game_stat.txt"))

game_title = input("Which game details do you want to check? ")
result.append(reports.get_game("game_stat.txt", game_title))

result.append(reports.count_grouped_by_genre("game_stat.txt"))

result.append(reports.get_date_ordered("game_stat.txt"))

def write_to_file(filename, lista):
    with open(filename, "w") as f:
        for element in lista:
            f.write("%s\n" % element)

write_to_file("answers.txt", result)