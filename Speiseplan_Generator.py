import random
import csv
import os.path


class Dish:
    def __init__(self, name, typus, cook_duration):
        self.name = name
        self.typus = typus
        self.cook_dur = cook_duration
        # self.rank = 5
        # self.sides == []
        if self.typus == "m":
            self.typus = "Fleischgericht"
        elif self.typus == "v":
            self.typus = "Vegetarisches Gericht"
        elif self.typus == "f":
            self.typus = "Fischgericht"
        elif self.typus == "s":
            self.typus = "Suessspeise"
        if self.cook_dur == "s":
            self.cook_dur = "Schnelles Gericht"
        elif self.cook_dur == "m":
            self.cook_dur = "Mittelschnelles Gericht"
        elif self.cook_dur == "l":
            self.cook_dur = "Aufwaendiges Gericht"

    def display(self):
        print(self.name)
        print(self.typus)
        print(self.cook_dur)


def check_sum(par_sum, value):
    par_sum += value
    if par_sum > 7:
        print(f"Zu große Anzahl eingegeben. Es verbleiben maximal {7 - (par_sum - value)} Tage")
        return False
    else:
        return True


def command():
    c = input("> ")
    return c


def create_plan(plan_dict, iteration):
    home = os.path.expanduser("~")
    with open(f"{home}/Desktop/Speiseplan {iteration + 1}.txt", "w") as file:
        for day in plan_dict:
            file.write(f"\r\n{day}: {plan_dict.get(day)}")


def determine_parameters():
    par_sum = 0
    parameters = {}

    print("Wie oft soll es Fleisch geben?")
    new_parameter = enter_parameter(par_sum)
    parameters.update({"Fleischgericht": new_parameter})
    par_sum += new_parameter

    print("Wie oft soll es vegetarisches Essen geben?")
    new_parameter = enter_parameter(par_sum)
    parameters.update({"Vegetarisches Gericht": new_parameter})
    par_sum += new_parameter

    print("Wie oft soll es Fisch geben?")
    new_parameter = enter_parameter(par_sum)
    parameters.update({"Fischgericht": new_parameter})
    par_sum += new_parameter

    # süß = Rest
    parameters.update({"Suessspeise": 7 - par_sum})

    par_sum = 0

    print("Wie oft soll es schnelles Essen geben?")
    new_parameter = enter_parameter(par_sum)
    parameters.update({"Schnelles Gericht": new_parameter})
    par_sum += new_parameter

    print("Wie oft soll es mittelschnelles Essen geben?")
    new_parameter = enter_parameter(par_sum)
    parameters.update({"Mittelschnelles Gericht": new_parameter})
    par_sum += new_parameter

    # aufwaendig = Rest
    parameters.update({"Aufwaendiges Gericht": 7 - par_sum})

    return parameters


def determine_propositions():
    print("Wie viele Vorschläge sollen erstellt werden?")
    while True:
        try:
            value = int(command())
        except ValueError:
            print("Eingabe muss eine Zahl sein")
            continue
        return value


def enter_parameter(par_sum):
    value = 0
    while True:
        try:
            value = int(command())
        except ValueError:
            print("Eingabe muss eine Zahl sein")
            continue
        if not check_sum(par_sum, value):
            continue
        break
    return value


def generate(number_props, parameters):
    iterations = range(0, number_props)
    for iteration in iterations:
        create_plan(generate_plan(parameters), iteration)
    print(f"{number_props} Vorschläge wurden erstellt.")
    menu()


def generate_plan(parameters):
    work_parameters = parameters.copy()
    dish_list = read()
    weeklyplan = {
        "Montag": "none",
        "Dienstag": "none",
        "Mittwoch": "none",
        "Donnerstag": "none",
        "Freitag": "none",
        "Samstag": "none",
        "Sonntag": "none"
    }
    for day in weeklyplan:
        work_list = dish_list.copy()

        while len(work_list) > 0:
            random_number = random.randint(0, len(work_list) - 1)
            dish = work_list[random_number]
            typus_wanted = False
            cookdur_wanted = False
            active_typus_key = ""
            active_cookdur_key = ""
            active_typus_key_value = 0
            active_cookdur_key_value = 0
            for key in work_parameters:
                if key == dish.typus and work_parameters.get(key) > 0:
                    typus_wanted = True
                    active_typus_key = key
                    active_typus_key_value = work_parameters.get(key)
                    break
            for key in work_parameters:
                if key == dish.cook_dur and work_parameters.get(key) > 0:
                    cookdur_wanted = True
                    active_cookdur_key = key
                    active_cookdur_key_value = work_parameters.get(key)
                    break
            if typus_wanted and cookdur_wanted:
                weeklyplan[day] = dish.name
                dish_list.remove(dish)
                work_parameters[active_typus_key] = active_typus_key_value - 1
                work_parameters[active_cookdur_key] = active_cookdur_key_value - 1
                break
            else:
                work_list.remove(dish)

    # Falls es unmöglich ist, Parameter zu beachten, werden sie ignoriert und die Liste wird aufgefüllt.
    for day in weeklyplan:
        if weeklyplan[day] == "none":
            random_number = random.randint(0, len(dish_list) - 1)
            dish = dish_list[random_number]
            weeklyplan[day] = dish.name
            dish_list.remove(dish)

    return weeklyplan


def import_dishes():
    pass


def menu():
    while True:
        print("Bitte Funktion wählen. Optionen: g(eneriere Speiseplan), n(eues Gericht hinzufügen)")
        while True:
            value = command()
            if value == "g":
                if len(read()) >= 7:
                    generate(determine_propositions(), determine_parameters())
                else:
                    print(
                        "Deine Speiseliste enthält weniger als 7 Gerichte. "
                        "Bitte füge neue Gerichte hinzu."
                    )
            elif value == "n":
                new_entry()
            else:
                print("Falsche Eingabe")


def new_entry():

    while True:
        print("Neues Gericht angeben. Beende Eingabe mit b ")
        dish_list = read()
        while True:
            value = command()
            already_there = False
            for dish in dish_list:
                if value == dish.name:
                    already_there = True
            if already_there:
                print("Gericht bereits vorhanden")
            elif value == "b":
                menu()
            else:
                line = [value]
                break

        print("Bitte Speisetyp angeben. Optionen: m(eat), v(egi), f(ish) oder s(weet)")
        while True:
            value = command()
            if value == "m" or value == "v" or value == "f" or value == "s":
                line.append(value)
                break
            else:
                print("Falsche Eingabe")

        print("Bitte Zubereitungsdauer angeben. Optionen: s(hort), m(edium), l(ong)")
        while True:
            value = command()
            if value == "s" or value == "m" or value == "l":
                line.append(value)
                break
            else:
                print("Falsche Eingabe")
        new_dish = Dish(line[0], line[1], line[2])

        # Sicherheitsabfrage
        new_dish.display()
        print("Zufrieden? Optionen: y, n")
        while True:
            value = command()
            if value == "y":
                write(new_dish)
                break
            elif value == "n":
                break
            else:
                print("Falsche Eingabe")


def read():
    file_exists = os.path.isfile("dishes.csv")
    if not file_exists:
        with open("dishes.csv", "w") as dishes:
            header = ["Gericht", "Speisetyp", "Zubereitungsdauer"]
            writer = csv.writer(dishes)
            writer.writerow(header)

    with open("dishes.csv", "r") as dishes:
        dish_list = []
        for line in dishes:
            dish_split = line.strip().split(",")
            if dish_split[0] == "Gericht" or dish_split == [""]:
                continue
            dish = Dish(dish_split[0], dish_split[1], dish_split[2])
            dish_list.append(dish)
    return dish_list


def show_database():
    pass


def write(new_dish):
    with open("dishes.csv", "a") as dishes:
        writer = csv.writer(dishes)
        writer.writerow([new_dish.name, new_dish.typus, new_dish.cook_dur])


menu()
