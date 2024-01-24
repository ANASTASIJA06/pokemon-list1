
import csv

pokemons = []
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by name")
    print("5. Search by length of name")
    print("6. First 10 pokemons")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        num = int(input("Enter the number: "))
        print(pokemons[num -1])
        # https://www.w3schools.com/python/python_lists_access.asp
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
    elif choice == '4':
        name = input("Enter the name:")
        newlist = []
        newlist = [x for x in pokemons if name in x]
        print(newlist)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
    elif choice == '5':
        name = int(input("Enter the name lenght:"))
        newlist = []
        for x in pokemons:
            if name == len(x):
                newlist.append(x)
        #newlist = [x for x in pokemons if name = len(x)]
        print(newlist)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
    elif choice == '6':
        #newlist = [x for x in pokemons if name in x]
        print(pokemons[0:10])

    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
