import random
import sys

word_list = ["chameau", "singe", "pomme", "gateau"]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main():
    print ("Bienvenue dans le jeu du pendu !")
    print("\n")
    print("Trouvez le mot caché en devinant les lettres une par une")
    print("\n")
    print("Bonne chance !")
    print("\n")

    word = random.choice(word_list)
    tries = 6
    display = []
    for _ in range(len(word)):
        display += "_"

    while "_" in display and tries > 0:
        print(HANGMANPICS[6 - tries])
        print(f"{' '.join(display)}")
        print("\n")
        print(f"Il vous reste {tries} essais")
        print("\n")
        guess = input("Entrez une lettre: ").lower()
        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                display[position] = letter
        if guess not in word:
            tries -= 1


    if "_" not in display and tries > 0:
        print("Vous avez gagné !")
    elif tries == 0:
        print("Vous avez perdu !")
        print(f"Le mot caché était {word}")
        print("Voulez-vous rejouer ? (o/n)")
        replay = input().lower()
        if replay == "o":
            main()
        else:
            sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
