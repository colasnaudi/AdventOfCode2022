def main():
    with open('Day2/test/input.txt', 'r') as file:
        file = file.read()
        file = file.splitlines()
        file = [i.split() for i in file]
        somme = 0
        for i in file:
            print(i)
            if i[1] == 'X':
                somme += 1
                if i[0] == 'A':
                    print("Draw")
                    somme += 3
                elif i[0] == 'B':
                    print("Perdu")
                elif i[0] == 'C':
                    print("Gagné")
                    somme += 6
            elif i[1] == 'Y':
                somme += 2
                if i[0] == 'A':
                    print("Gagné")
                    somme += 6
                elif i[0] == 'B':
                    print("Draw")
                    somme += 3
                elif i[0] == 'C':
                    print("Perdu")
            elif i[1] == 'Z':
                somme += 3
                if i[0] == 'A':
                    print("Perdu")
                elif i[0] == 'B':
                    print("Gagné")
                    somme += 6
                elif i[0] == 'C':
                    print("Draw")
                    somme += 3
            print(somme)
        print(somme)


if __name__ == "__main__":
    main()

# The test result is 15
# The input result is 9177