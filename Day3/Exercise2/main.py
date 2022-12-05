from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

def main():
    somme = 0
    file = open('Day3/test/input.txt', "r")
    line = file.readline()
    while line:
        line2 = file.readline()
        line3 = file.readline()
        for i in line:
            if i in line2 and i in line3:
                letter = i
                break
        line = file.readline()

        print ("The common letter is ",letter)

        if(letter.islower()):
            print("It worth : ",alphabet_position(letter))
            somme += int(alphabet_position(letter))
        else:
            print("It worth : ",int((alphabet_position(letter)))+26)
            somme += int((alphabet_position(letter)))+26

    file.close()

    print("La somme totale est : ",somme)

if __name__ == "__main__":
    main()

# The test result is 70
# The input result is 2780