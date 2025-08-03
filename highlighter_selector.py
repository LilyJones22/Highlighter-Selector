import random

colors = [
    "red", "orange", "yellow", "green", "teal", "baby blue", "blue", "dark blue", "purple", "magenta", "pink" # list of avaliable highlighter colors
]


while True: # input handling loop
    try:
        previous = input("Enter last used color\nType 'na' if unknown\n ")
        if previous not in colors:
            if previous != "na":
                raise ValueError #prevents invalid input from beign accepted

        if previous == "na":
            previous = random.choice(colors) # picks random color to start if not declared

        break # ends input loop

    except ValueError:
        print("Not a valid input. Please try again") # will restart ipnut loop

text = "" # instalizing variable for later loop

while text != quit:
    index_p = colors.index(previous) # getting color index number from list above

    if index_p == len(colors) - 1: # if color is last in item list
        before = colors[-2] # before is second to last color in list
        after = colors[0] # after is set to first color in list, creating a circle

    elif index_p == 0: # if color is first in item list
        before == colors[-1] # before is set to last item in list, creating a circle
        after = colors [1] # after is set to second item in list

    else:
        before = colors[index_p - 1]
        after = colors[index_p + 1]

    allowed_colors = [] #creating empty list to select new color from

    for color in colors:
        if color != before or color != previous or color != after:
            allowed_colors.append(color) # adds all colors but the current one, the one before, and the one after to random selection

    current = random.choice(allowed_colors) # selects random choice from the limited list
    print(f"New color: {current}")
    text = input("Type 'quit' to end. Or anything else to get a new color\n")
    previous = current

    