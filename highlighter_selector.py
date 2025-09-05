import random

colors = [
    "red", "orange", "yellow", "green", "teal", "baby blue", "blue", "dark blue", "purple", "magenta", "pink" # list of avaliable highlighter colors
]

history = [] # for tracking all color selections from this session


def choose(previous_color_used):

    history.append(previous_color_used) # adds previous color to history

    index_p = colors.index(previous_color_used) # getting color index number from list above

    if index_p == len(colors) - 1: # if color is last in item list
        before = colors[-2] # before is second to last color in list
        after = colors[0] # after is set to first color in list, creating a circle

    elif index_p == 0: # if color is first in item list
        before = colors[-1] # before is set to last item in list, creating a circle
        after = colors [1] # after is set to second item in list

    else:
        before = colors[index_p - 1]
        after = colors[index_p + 1]


    allowed_colors = [] # creating empty list to select new color from

    for color in colors:
        if color == previous_color_used:
            pass # color used last cannot be used
        elif color == before:
            pass # color one hue left cannot be used
        elif color == after:
            pass # color one hue right cannot be used
        else:
            if color not in history[-3:]: # if color was not used in last 3 selections, it can be selected
                allowed_colors.append(color)

    current = random.choice(allowed_colors) # selects color from smaller list of allowed colors

    return current


while True: # input handling loop
    try:
        current = input("Enter last used color\nType 'na' if unknown\n ")
        if current not in colors:
            if current != "na":
                raise ValueError #prevents invalid input from beign accepted

        if current == "na":
            current = random.choice(colors) # picks random color to start if not declared

        break # ends input loop

    except ValueError:
        print("Not a valid input. Please try again") # will restart ipnut loop

text = "" # instalizing variable for later loop

while text != "quit":
    current = choose(current)
    print(f"\nNew color: {current}")
    text = input("Type \'quit\' to end. Or anything else to get a new color\n")

print("\nThank you!")
print("Have a good one")