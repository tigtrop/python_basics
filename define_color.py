with open('data/colors.txt') as file:
    colors = file.read()
    import ast

    colors = ast.literal_eval(colors)
file.close()


def check_output(out):
    if out == 0:
        print("There is no such color")


def define_color_by_code():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    out = 0
    ink = [a, b, c]
    for key, val in colors.items():
        if val == ink:
            print(key)
            out += 1
        else:
            continue
    check_output(out)


# define_color_by_code()


def define_color_by_name():
    a = input("Enter color name: ")
    ink = a.upper()
    out = 0
    for key, val in colors.items():
        if key == ink:
            print(val)
            out += 1
        else:
            continue
    check_output(out)


# define_color_by_name()

def find_special_colors():
    counter = 0
    for val in colors.values():
        cou = 0
        for num in val:
            if num == 0:
                cou += 1
            else:
                continue
        if cou == 2:
            counter += 1
            cou -= 2
        else:
            cou = 0
    print(counter)


find_special_colors()
