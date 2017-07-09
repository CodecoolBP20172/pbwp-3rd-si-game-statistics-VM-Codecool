
# Report functions
"""
-------------------------------PART 2 -----------------------------------
What is the title of the most played game (i.e. sold the most copies)?
Expected name of the function: get_most_played(file_name)
Expected output of the function: (string)
Other expectation:  if there is more than one, then return the first from the file
"""
import math


def get_most_played(file_name):
    with open(file_name) as all_games:
        most_played_game = 0
        name_of_most_played_game = str()
        for line in all_games:
            actual_played_game = float(line.split("\t")[1])
            name_actual_played_game = line.split("\t")[0]
            if actual_played_game > most_played_game:
                most_played_game = actual_played_game
                name_of_most_played_game = name_actual_played_game
        return (name_of_most_played_game)


"""How many copies have been sold total?
Expected name of the function: sum_sold(file_name)
Expected output of the function: (number)
"""


def sum_sold(file_name):
    with open(file_name) as all_games:
        sold_games = []
        for line in all_games:
            sold_games.append(float(line.split("\t")[1]))
            sum_games = sum(sold_games)
        return (sum_games)


"""What is the average selling?
Expected name of the function: get_selling_avg(file_name)
Expected output of the function: (number)
"""


def get_selling_avg(file_name):
    with open(file_name) as all_games:
        average = []
        for line in all_games:
            average.append(line.split("\t")[0])
        return (sum_sold(file_name) / len(average))


"""How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)
"""


def count_longest_title(file_name):
    with open(file_name) as all_games:
        title = []
        for line in all_games:
            title.append(line.split("\t")[0])
            maxlenght = max(len(s) for s in title)
        return maxlenght


"""What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation: the return value must be the rounded up average
"""


def get_date_avg(file_name):
    with open(file_name) as all_games:
        date_of_release = []
        for line in all_games:
            date_of_release.append(int(line.split("\t")[2]))
        return math.ceil(sum(date_of_release) / len(date_of_release))


"""What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game. This is the title of the game (string).
This is an existent game. The function return a list of the properties of this game including the title.
An example return value: ["Minecraft",23.0,2009,"Survival game","Microsoft"].
"""


def get_game(file_name, title):
    with open(file_name) as all_games:
        for line in all_games:
            game = (line.split("\t"))
            if title == game[0]:
                game[1] = float(game[1])
                game[2] = int(game[2])
                game[-1] = game[-1].replace("\n", "")
                return game