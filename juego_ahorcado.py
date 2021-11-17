import random
import os


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def read_file():
    words = []
    with open("./archivos/words.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.replace("\n", ""))
    return words


def run():
    welcome_message = "Adivina la palabra!\n"
    words = read_file()
    random_word = random.choice(words)
    progress = ["_" for letter in random_word]
    has_finished = False
    while not has_finished:
        try:
            print(progress)
            print(welcome_message+' '.join(progress))
            given_letter = input("Ingresa una letra: ")
            if given_letter.isnumeric():
                raise Exception("")
            if given_letter in random_word:
                positions = find(random_word, given_letter)
                for position in positions:
                    progress[position] = given_letter
            if len(list(filter(lambda el: el == "_", progress))) == 0:
                has_finished = True
            os.system("cls")
        except:
            os.system("cls")
            print(f"No debes ingresar numeros")
    print(f"Ganaste! La palabra era {random_word}")


if __name__ == '__main__':
    run()
