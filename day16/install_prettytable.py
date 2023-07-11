from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Poketmon Name", ["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l" 
# left align

print(table)

# pypi.org => PyPi helps you find and install software developed and shared by the Python community.


