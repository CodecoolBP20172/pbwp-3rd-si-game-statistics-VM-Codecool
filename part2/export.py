
# Export functions
import reports

file_name = 'game_stat.txt'
with open("export.txt", "w") as export:
    export.write(str(reports.get_most_played(file_name)) + "\n")
    export.write(str(reports.sum_sold(file_name)) + "\n")
    export.write(str(reports.get_selling_avg(file_name)) + "\n")
    export.write(str(reports.count_longest_title(file_name)) + "\n")
    export.write(str(reports.get_date_avg(file_name)) + "\n")
    export.write(str(reports.get_game(file_name, "Minecraft")) + "\n")