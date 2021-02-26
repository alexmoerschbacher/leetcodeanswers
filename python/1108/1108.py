def defangIPaddr(address):
    holder = ""
    for letter in address:
        if letter == ".":
            holder += "[.]"
        else:
            holder += letter
    return holder

