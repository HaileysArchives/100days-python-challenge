### How to Modify variables with Globla scope

# Modifying Global Scope

enemies = "Skeleton" #global variable

def increase_enemies():
	enemies = "Zombie" #local variable
	print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = 1

def increase_enemies():
	global enemies # 글로벌 변수가 있다고 명시적으로 선언해주어야 한다. 
	global enemies
	print(f"enemies inside function: {enemies}")

# 그러나 글로벌 변수를 생성함으로써 언제만들었는지에 관계없이 완전히 독립적으로 수정할 수 있어 주의해야 한다. 
# 먼저 전역변수는 코드의 어느 곳에서나 생성될 수 있기 때문에 더 쉽게 오류가 발생한다. 

# So avoid modify the global variable. 

# 그렇다면 함수 내에서 전역 범위를 수정하지 않고 어떻게 기능을 변경하는 목표를 달성할 수 있을까? return 문 사용하기 

enemies = 1

def increase_enemies():
	print(f"enemies inside function: {enemies}")
	return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")









