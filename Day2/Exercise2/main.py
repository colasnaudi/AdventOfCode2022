def main():
    with open('Day2/test/input.txt', 'r') as file:
        file = file.read()
        file = file.splitlines()
        file = [i.split() for i in file]
        somme = 0
        for i in file:
            print(i)
            if i[1] == 'X':
                # Loose
                if i[0] == 'A':
                    somme += 3
                elif i[0] == 'B':
                    somme += 1
                elif i[0] == 'C':
                    somme += 2
            elif i[1] == 'Y':
                # Draw
                somme += 3
                if i[0] == 'A':
                    somme += 1
                elif i[0] == 'B':
                    somme += 2
                elif i[0] == 'C':
                    somme += 3
            elif i[1] == 'Z':
                # Win
                somme += 6
                if i[0] == 'A':
                    somme += 2
                elif i[0] == 'B':
                    somme += 3
                elif i[0] == 'C':
                    somme += 1
        print(somme)
if __name__ == "__main__":
    main()

# The test result is 12
# The input result is 