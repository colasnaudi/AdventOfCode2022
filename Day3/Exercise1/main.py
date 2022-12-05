from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

def main():
    somme = 0
    with open('Day3/test/input.txt', 'r') as file:
        file = file.read()
        file = file.splitlines()
        file = [i.split() for i in file]
        for i in file:
            l = len(i[0])
            print ("First : ",i[0][:l//2])
            print ("Second : ",i[0][l//2:])
            for k in i[0][:l//2]:
                if k in (i[0][l//2:]):
                    letter = k
                    break
            print ("The letter is ",letter)

            if(letter.islower()):
                print(alphabet_position(letter))
                somme += int(alphabet_position(letter))
            else:
                print(int((alphabet_position(letter)))+26)
                somme += int((alphabet_position(letter)))+26

    print("La somme totale est : ",somme)

if __name__ == "__main__":
    main()

# The test result is 157
# The input result is 7568