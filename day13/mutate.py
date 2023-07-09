# Use a Dubugger
# paste python tutor web site. => visualize excuetion.

def mutate(a_list):
    b_list = []
    
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    # b_list.append(new_item) => this line clicked. so this line changed red line. And check the breakpoint. 
    # At that moment, it is used to investigate all variables and all of the functions of the line.
    print(b_list)

mutate([1, 2, 3, 5, 8, 13]) 
# We want to print [2, 4, 6, 10, 16, 26]

# You can isolate a particular time point to see what each of the values are. 