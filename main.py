# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def generateCards():
    cards = ["joker_red", "joker_black"]
    signs = ['spades', 'clubs', 'hearts', "diamonds"]
    faces = ['queen', 'king', 'jack', 'ace']

    for i in signs:
        for j in range(2, 11):
            number = str(j)
            card = number + "_of_" + i
            cards.append(card)
        for k in range(len(faces)):
            faceCard = faces[k] + "_of_" + i
            cards.append(faceCard)

    print(cards)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print_hi('PyCharm')
    generateCards()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
