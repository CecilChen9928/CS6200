import re

from data import laptops, pcgames, majors

def get_id(element):
    return element['ID']
def get_company(element):
    return element['Company']
def get_cpu(element):
    return element['Cpu']
def get_gpu(element):
    return element['Gpu']
def get_inches(element):
    return element['Inches']
def get_resolution(element):
    return element['ScreenResolution']
def get_price(element):
    return element['Price']
def get_weight(element):
    return element['Weight']
def get_opsys(element):
    return element['OpSys']
def get_memory(element):
    return element['Memory']
def get_ram(element):
    return element['Ram']

def contains_word(source : str, target : str):
    source_lower = ""
    target_lower = ""
    for char in source:
        if char != ' ':
            source_lower += char.lower()
    for char in target:
        if char != ' ':
            target_lower += char.lower()
    return source_lower in target_lower

def get_ram_value(string : str):
    ans = ""
    for m in string:
        if m.isdigit():
            ans += m
    return int(ans)

def get_weight_value(string : str):
    ans = ""
    i = 0
    while string[i] != 'k':
        ans += string[i]
        i += 1
    return float(ans)

def get_memory_value(string : str):
    ans = ""
    for m in string:
        if m.isdigit():
            ans += m
    return int(ans)

def get_inches_value(string : str):
    return float(string)

def get_price_value(string : str):
    return float(string)

def get_intel_value(string : str):
    ans = 0
    for i in range(len(string)):
        if string[i] == 'i' and string[i+1].isdigit():
            ans = int(string[i+1])
            break
    return ans

def get_amd_value(string : str):
    ans = 0
    for i in range(len(string)):
        if i != 0 and string[i] == 'A':
            ans = int(string[i+1])
            break
    return ans

def get_resolution_value(string : str):
    ans = ""
    i = 0
    while i <= len(string) - 1:
        if string[i].isdigit() and (string[i+1].isdigit() or string[i+1] == 'x'):
            ans += string[i]
        if string[i] == 'x':
            break
        i += 1
    return int(ans)

weight_ref = {
    2 : 3,
    3 : 3,
    4 : 2,
    5 : 1.5
}

inches_ref = {
    2: 20,
    3: 16,
    4: 15,
    5: 14
}

high_cpu_game_genre = [
    'Real-time strategy',
    'First-person shooter',
    'MMORPG',
    'Action',
    'FPS',
    'RTS',
    'Action role-playing',
    'action-adventure',
    'Third-person shooter'
    'Sports',
    'Racing',
    'Online role-playing game',
    'MOBA',
    'Action, FPS'
]

high_cpu_major_category = [
    'Biology & Life Science',
    'Computers & Mathematics',
    'Engineering',
    'Physical Sciences'
]

high_resolution_game_genre = [
    'First-person shooter',
    'FPS',
    'Action role-playing',
    'MMORPG',
    'Third-person shooter',
    'Sports',
    'Racing',
    'Action, FPS'
]

frequency = 0
intel_cpu_standard = 0
amd_cpu_standard = 0
ram_standard = 0
resolution_standard = 0
memory_standard = 8

laptops_game_selected = []
laptops_size_selected = []
laptops_price_selected = []


print('''
Welcome to the Laptop Search Engine!
Wish you find your desired laptop!\n\n''')

# Ask users if they have game requirement
game_status = input("Do you have game requirement? y/n \n")
# if users answer no, skip. Else, ask which game(s) do they play

if game_status == 'y' or game_status == 'Y':

    game_play_list = []
    isFinished = False

    while not isFinished:
        game_input = input("Which game do you play? Enter the key word: \n")
        game_name = []

        for i in range(len(pcgames)):
            if contains_word(game_input, pcgames[i]['Name']):
                game_name.append({pcgames[i]['ID'] : pcgames[i]['Name']})

        print("Here are the games we found:\n")
        for game in game_name:
            print(game)

        game_id = int(input("\nPlease select the ID of the game you played\n"))
        game_play_list.append(pcgames[game_id])

        other_game = input("Is that all? y/n\n")
        if other_game == 'Y' or other_game == 'y':
            isFinished = True

    for game in game_play_list:
        if game['Genre'] in high_cpu_game_genre:
            intel_cpu_standard = 7
            amd_cpu_standard = 9
            ram_standard = 16
        if game['Genre'] in high_resolution_game_genre:
            resolution_standard = 1920

    # Select cpu
    for laptop in laptops:
        if contains_word('intel', get_cpu(laptop)):
            if get_intel_value(get_cpu(laptop)) >= intel_cpu_standard:
                laptops_game_selected.append(laptop)
        if contains_word('amd', get_cpu(laptop)):
            if get_amd_value(get_cpu(laptop)) >= amd_cpu_standard:
                laptops_game_selected.append(laptop)

    # Select resolution
    for laptop in laptops_game_selected:
        if get_resolution_value(get_resolution(laptop)) < resolution_standard:
            laptops_game_selected.remove(laptop)

    # Select ram
    for laptop in laptops_game_selected:
        if get_ram_value(get_ram(laptop)) < ram_standard:
            laptops_game_selected.remove(laptop)
    frequency = input('''\nPlease describe your frequency of playing games: 1 to 5\n''')

hobbies = input('''Do you have the following computer-based hobbies:
                   * Video Editor
                   * Game Design
                   * 3D Drawing\n''')

major_input = input("What is your major? Type the key word \n")
major_name = []

for i in range(len(majors)):
    if contains_word(major_input, majors[i]['Major']):
        major_name.append({majors[i]['ID']: majors[i]['Major']})

print("Here are the majors we found:\n")
for major in major_name:
    print(major)

major_id = int(input("\nPlease select the ID of your major\n"))

if majors[major_id]['Major_Category'] in high_cpu_major_category:
    intel_cpu_standard = 7
    amd_cpu_standard = 9
    ram_standard = 16
    memory_standard = 500

if game_status == 'Y' or game_status == 'y':
    # Select cpu
    for laptop in laptops_game_selected:
        if contains_word('intel', get_cpu(laptop)):
            if get_intel_value(get_cpu(laptop)) < intel_cpu_standard:
                laptops_game_selected.remove(laptop)
        if contains_word('amd', get_cpu(laptop)):
            if get_amd_value(get_cpu(laptop)) < amd_cpu_standard:
                laptops_game_selected.remove(laptop)

        # Select resolution
    for laptop in laptops_game_selected:
        if get_resolution_value(get_resolution(laptop)) < resolution_standard:
            laptops_game_selected.remove(laptop)

        # Select ram
    for laptop in laptops_game_selected:
        if get_ram_value(get_ram(laptop)) < ram_standard:
            laptops_game_selected.remove(laptop)

        # Select memory
    for laptop in laptops_game_selected:
        if get_memory_value(get_memory(laptop)) < memory_standard:
            laptops_game_selected.remove(laptop)

else:
    # Select cpu
    for laptop in laptops:
        if contains_word('intel', get_cpu(laptop)):
            if get_intel_value(get_cpu(laptop)) >= intel_cpu_standard:
                laptops_game_selected.append(laptop)
        if contains_word('amd', get_cpu(laptop)):
            if get_amd_value(get_cpu(laptop)) >= amd_cpu_standard:
                laptops_game_selected.append(laptop)

    # Select resolution
    for laptop in laptops_game_selected:
        if get_resolution_value(get_resolution(laptop)) < resolution_standard:
            laptops_game_selected.remove(laptop)

    # Select ram
    for laptop in laptops_game_selected:
        if get_ram_value(get_ram(laptop)) < ram_standard:
            laptops_game_selected.remove(laptop)

    # Select memory
    for laptop in laptops_game_selected:
        if get_memory_value(get_memory(laptop)) < memory_standard:
            laptops_game_selected.remove(laptop)



size_demand = int(input("Do you often use laptops during travels or outside? \n"
                        "Please level your frequency from 1 to 5\n"
                        "(1: never, 5: often)\n"))

inches_upper = inches_ref[size_demand]
weight_upper = weight_ref[size_demand]

for laptop in laptops:
    if get_weight_value(get_weight(laptop)) <= weight_upper and get_inches_value(get_inches(laptop)) <= inches_upper:
        laptops_size_selected.append(get_id(laptop))

price_demand_lower = float(input("What is your accepted price range? \n"
                                "Please give the lowest price you accept\n"))
price_demand_upper = float(input("What is your accepted price range? \n"
                                "Please give the highest price you accept\n"))


for laptop in laptops:
    if get_price(laptop) <= price_demand_upper and get_price(laptop) >= price_demand_lower:
        laptops_price_selected.append(get_id(laptop))


selected_list = []

for laptop in laptops_game_selected:
    if get_id(laptop) in laptops_price_selected and get_id(laptop) in laptops_size_selected:
        selected_list.append(laptop)

if int(frequency) <= 3:
    for i in range(len(selected_list) - 2):
        print(selected_list[i])


for laptop in selected_list:
    print(laptop)