import random

list = []
with open("D:\project\python2.py\hangman\hangman_wordlist.txt", "r") as file:
    list = file.read().split("\n")
# word = random.choice(list)
word = "karim"
print(
    "-------------------------- Welcome in Hangman Game-------------------------------\n"
)
print("                  -----------------------------------------\n")

for i in word:
    print("_", end=" ")


def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def printword(guessedletters):
    count = 0
    rightcount = 0
    for char in word:
        if char in guessedletters:
            print(word[count], end=" ")
            rightcount += 1
        else:
            print(" ", end=" ")
        count += 1
    return rightcount


def printLines():
    print("\r")
    for char in word:
        print("\u203E", end=" ")


length_of_word = len(word)
times_wrong = 0
guess_index = 0
letters_index = []
letters_right = 0

while times_wrong != 6 and letters_right != length_of_word:
    print("\nLetters guessed so far: ")
    for letter in letters_index:
        print(letter, end=" ")
    letterGuessed = input("\nGuess a letter: ")
    if word[guess_index] == letterGuessed:
        print_hangman(times_wrong)
        guess_index += 1
        letters_index.append(letterGuessed)
        letters_right = printword(letters_index)
        printLines()
    else:
        times_wrong += 1
        letters_index.append(letterGuessed)
        print_hangman(times_wrong)
        letters_right = printword(letters_index)
        printLines()

print("Game is over! Thank you for playing :)")
