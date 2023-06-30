#Functions with Outputs

# def format_name(f_name, l_name):
#     first = list(f_name)
#     last = list(l_name)
#     f_name[0].upper
#     l_name[0].upper
#     return (first + last)

# first_name = input("Write your first name: ")
# last_name = input("Write your last name: ")

# name = format_name(f_name=first_name, l_name=last_name)
# print(''.join(name))

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name("hailey", "HAILEY")

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     print(f"{formated_f_name} {formated_l_name}")

# format_name("HaIley", "KIM")


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("HaIley", "KIM"))
