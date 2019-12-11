import csv
import calendar
from pprint import pprint
from collections import defaultdict

class Class:
    def __init__(self, list_input):
        self.code = list_input[0]
        self.description = list_input[1]
        self.group = list_input[2]
        self.activity = list_input[3]
        self.day = list_input[4]
        self.time = list_input[5]
        self.campus = list_input[6]
        self.location = list_input[7]
        self.duration = list_input[8]
        self.dates = list_input[9]

    def simplify_time(self):
        return int(self.time.split(":")[0])

    def simplify_day(self):
        if self.day == "Mon":
            return 0
        elif self.day == "Tue":
            return 1
        elif self.day == "Wed":
            return 2
        elif self.day == "Thu":
            return 3
        elif self.day == "Fri":
            return 4
        elif self.day == "Sat":
            return 5
        elif self.day == "Sun":
            return 6
        else:
            return -1

    def simplify_code(self):
        return self.code.split("_")[0]

    def simplify_group(self):
        return self.group

    def simplify_activity(self):
        return int(self.activity)

    
def print_line():
    print(u"\u2500" * (14 * 7 + 6))

def display_table(classes, active_activities, info):
    print_line()
    info_str = "Timetable for " + info[0] + ", student number " + info[1]
    print("|" + info_str.center(14 * 7 + 4) + "|")
    day_row = "|    |"
    for day in list(calendar.day_abbr):
        day_row += day.center(13) + "|"
    print_line()
    for hour in range(8, 20):
        row_1 = "|" + str(hour).rjust(3) + " |"
        row_2 = "|" + " " * 3 + " |"
        for day in range(7):
            if classes[(day, hour)] != []:
                if len(classes[(day, hour)]) == 1:
                    row_1 += classes[(day, hour)][0][0].center(13) + "|"
                    row_2 += classes[(day, hour)][0][1].center(9) + \
                        str(classes[(day, hour)][0][2]).center(4) + "|"
                else:
                    # Search for the right class (THIS IS BAREBONES)
                    # for option in classes[(day, hour)]:
                    #     print(option)
                    #     print(activities)
                        # if option[1] == activities[classes[(day, hour)][0][0]][0][1] and \
                        # option[2] == activities[classes[(day, hour)][0][0]][1][1]:
                        #     row_1 += option[0].center(13) + "|"
                        #     row_2 += option[1].center(9) + str(option[2]).center(4) + "|"
                        # else:
                        #     continue
                    row_1 += "CLASH".center(13, ".") + "|"
                    row_2 += "".center(13, ".") + "|"
            else:
                row_1 += " " * 12 + " |"
                row_2 += " " * 12 + " |"
        print(row_1)
        print(row_2)
        print_line()
    return "Success!"

# Main function
if __name__ == "__main__":
    name = "Matthew Low"
    number = "45300587"
    info = (name, number)
    dictionary = defaultdict(lambda: [])
    lol = list(csv.reader(open('timetable.csv', 'r'), delimiter='\t'))
    classes = lol[1:]
    for cl in classes:
        co = Class(cl)

        dictionary[(co.simplify_day(), co.simplify_time())].append((co.simplify_code(), co.simplify_group(), co.simplify_activity()))

    # pprint(dict(dictionary))
    activities = defaultdict(lambda: [])
    # Put in preferences here
    activities["COMP4403"] = [('LEC', 1), ('TUT', 1)]
    activities["MATH3401"] = [('LEC', 1), ('TUT', 5)]
    activities["STAT3001"] = [('LEC', 1), ('TUT', 2)]
    activities["STAT3004"] = [('LEC', 1), ('TUT', 1)]
    print(display_table(dictionary, activities, info))