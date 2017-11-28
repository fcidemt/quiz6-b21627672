import sys

given_number = int(sys.argv[1])
print("Enter a number:", given_number)

star = ["*" * (i + 1) for i in range(0, given_number * 2 - 1, 2)]
space = [" " * (i - 1) for i in range(given_number,0,-1)]
for i in range(len(star)):
    print(space[i] + star[i])

star_reversed = ["*" * i for i in range((given_number - 1) * 2 - 1, 0, -2)]
space_reversed = [" " * (i + 1) for i in range(0, given_number, 1)]
for i in range(len(star_reversed)):
    print(space_reversed[i] + star_reversed[i])