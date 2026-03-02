from pyscript import display, document # type: ignore

def show_players(e):
    document.getElementById('output').innerHTML = ""

    team = int(document.getElementById('team_selected').value)

    red_names = [ "Agudo Jairo", "Al Hazmi Naser", "Alaiza Mikko"
                 "Banaag Matthew", "Barcelona Emille", "Brion Cyrene",
                 "Buo Miguel", "Castro Lian", "Cruz Shia",
                 "Del Prado Karla", "Entrada Gianna", "Francisco Gavin", 
                 "Gavina Adrian", "Goyenechea Xylee", "Guevarra Sofia",
                 "Haberia Ioana", "Janayan Alexander", "Libutan Jabez",
                 "Lubo Arabella", "Manuel Luisa", "Mariposque Janine",
                 "Pagtalunan Rycob", "Reyes lucas", "Singh Fateh",
                 "Subaan Tyronne", "Tan Audrey", "Vargas Alexandra",
                 "Zaldivar James" ]

    blue_names = ["", ""]

    green_names = ["", ""]

    yellow_names = ["", ""]

    for red_name in red_names:
        display(red_name, target="output")

    for blue_name in blue_names:
        display(blue_name, target="output")

    for green_name in green_names:
        display(green_name, target="output")

    for yellow_name in yellow_names:
        display(yellow_name, target="output")