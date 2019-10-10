
# Printing functions
import reports

print("The most played game is:",reports.get_most_played("game_stat.txt"))

print("The summary of the sold copies:", reports.sum_sold("game_stat.txt"), "million.")

print("The avarage of sold copies:",reports.get_selling_avg("game_stat.txt"),"million.")

print("The longest title contains",reports.count_longest_title("game_stat.txt"),"characters.")

print("The average release date is: ",reports.get_date_avg("game_stat.txt"))

game_title = input("Which game details do you want to check? ")
print(reports.get_game("game_stat.txt", game_title))

print("The following dictionary contains the number of the games by genre:\n",reports.count_grouped_by_genre("game_stat.txt"))

print()
print("The ordered game library is here:\n")
for i in reports.get_date_ordered("game_stat.txt"):
    print(i)