game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
	new_enemy = enemies[0] # this new_enemy is avaliable anywhere within this function. 

print(new_enemy) 

#If you were to create a new variable inside an if block or a while loop or a for loop, basically any sort of block of code that's indented.

### Python is no such thig as block scope. 

# but add new function. And now this line(print(new_enemy)) error is out. because within the function there is local scope. 

game_level = 3

def create_enemy():
	enemies = ["Skeleton", "Zombie", "Alien"]
	if game_level < 5:
		new_enemy = enemies[0]

print(new_enemy) # NameError: 'new_enemy' is not defined. 