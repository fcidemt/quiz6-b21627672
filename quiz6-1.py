import sys

given_number = int(sys.argv[1])
print("Enter a number:", given_number)

def diamond_shape(number, star_number=0, control="top"):
    if number == 0 and control == "finish":
        return 0

    elif control == "bottom":
        print(" " * (star_number + 1) + "*" * (number * 2 - 1))
        if (number - 1) == 0:
            return diamond_shape(0, 0, control="finish")
        else:
            return diamond_shape(number - 1, star_number + 1, control="bottom")

    else:
        print(" " * (number - 1) + "*" * (star_number * 2 + 1))
        if (number - 1) == 0:
            return diamond_shape(given_number - 1, star_number=0, control="bottom")
        else:
            return diamond_shape(number - 1, star_number + 1)


diamond_shape(given_number)