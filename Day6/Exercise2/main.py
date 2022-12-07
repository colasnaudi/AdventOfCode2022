import collections

def main():
    somme = 0
    with open('Day6/test/input.txt', 'r') as file:
        file = file.read()
        file = file.splitlines()
        file = [i.split() for i in file]
        deb = 0
        end = 14
        trouve = False
        while not trouve:
            for i in file:
                mot = i[0][deb:end]
            if collections.Counter(mot).most_common(1)[0][1] == 1:
                trouve = True
            deb += 1
            end += 1
        print("Place of the letter : ", end-1)

if __name__ == "__main__":
    main()

# The test1 result is 23
# The test2 result is 23
# The test3 result is 29
# The test4 result is 26
# The input result is 2202