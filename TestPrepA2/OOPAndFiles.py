try:                              # DONT FORGET
    with open("chars.txt", "r") as file:
        chars = file.readlines()  # Values HAVE NOT been stripped. They are in an Array tho :D
except OSError:                   # DONT FORGETTTTT 2. ELECTRIC BOOGALOO.
    print("File not found.")      # DONT FORGET 3. END OF THE TRILOGY.


class Character:
    def __init__(self):
        self._name = ""
        self._path = ""
        self._element = ""

    def Constructor(self, name, path, element):
        self._name = name
        self._path = path
        self._element = element

    # OR

    def Name_Setter(self, name):
        self._name = name

    def Name_Getter(self):
        return self._name


characters = ["", "", "", "", "", "", "", "", "", ""]
# You have to do this sadly, can't have infinite array as Array in CIE def is standard length

for i in range(10):
    char_temp = Character()
    if i % 3 == 0:
        char_temp.Constructor(chars[i].rstrip(), chars[i + 1].rstrip(), chars[i + 2].rstrip()) # DONT FORGET TO STRIP THESE BAD BOYS DOWN
        characters[int(i / 3)] = char_temp  # Similarly, try not to append but to store at specific index instead

for i in range(4):
    print(characters[i].Name_Getter())
