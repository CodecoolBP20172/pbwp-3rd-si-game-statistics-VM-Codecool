
# Printing functions
import reports


def print_get_most_played(file_name):
    print (reports.get_most_played(file_name))


def print_sum_sold(file_name):
    print (reports.sum_sold(file_name))


def print_get_selling_avg(file_name):
    print (reports.get_selling_avg(file_name))


def print_count_longest_title(file_name):
    print (reports.count_longest_title(file_name))


def print_get_date_avg(file_name):
    print (reports.get_date_avg(file_name))


def print_get_game(file_name, title):
    print (reports.get_game(file_name, title))


def printin_answers_part_2(file_name):
    print_get_most_played(file_name)
    print_sum_sold(file_name)
    print_get_selling_avg(file_name)
    print_count_longest_title(file_name)
    print_get_date_avg(file_name)
    print_get_game(file_name, "The Sims")


printin_answers_part_2("game_stat.txt")
