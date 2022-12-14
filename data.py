import csv

laptops_data = []
laptops = []
with open('laptop_data.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        laptops_data.append(lines)
for i in range(1, len(laptops_data)):
    element = dict()
    element['ID'] = i-1
    for j in range(1, len(laptops_data[0])):
        element[laptops_data[0][j]] = laptops_data[i][j]
    element['Price'] = float(element['Price']) / 50
    laptops.append(element)
laptops_data.clear()

majors_data = []
majors = []
with open('majors-list.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        majors_data.append(lines)
for i in range(1, len(majors_data)):
    element = dict()
    element['ID'] = i - 1
    for j in range(1, len(majors_data[0])):
        element[majors_data[0][j]] = majors_data[i][j]
    majors.append(element)
majors_data.clear()

pcgames_data = []
pcgames = []
# load data from csv
with open('computer_games.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        pcgames_data.append(lines)
for i in range(1, len(pcgames_data)):
    element = dict()
    element['ID'] = i - 1
    for j in range(len(pcgames_data[0])):
        element[pcgames_data[0][j]] = pcgames_data[i][j]
    element['Date Released'] = element['Date Released'][-4:]
    pcgames.append(element)
pcgames_data.clear()









