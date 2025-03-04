# fruit = "Apple"
fruit = "Kiwi"

if len(fruit) > 4:
    if "e" in fruit:
        print("Valid fruit")
    else:
        print("Invalid fruit")
else:
    if "p" in fruit:
        print("else => if")
    elif "w" in fruit:
        print("else => elif")
    else:
        print("else => else")
