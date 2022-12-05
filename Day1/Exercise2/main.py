def main():
    with open('Day1/test/input.txt', 'r') as file:
        data = file.read()
        somme = 0
        nb = 0
        max = []
        for i in data.splitlines():
            if i != '':
                somme += int(i)
                print ("somme", str(somme))
            if i == '':
                print("somme finale :", str(somme))
                max.append(somme)
                somme = 0
                nb += 1
        print("somme finale :", str(somme))
        max.append(somme)
        somme = 0
        nb += 1
        max.sort()
        print(max)
        max = max[len(max)-3:len(max)]
        print(max)
        for i in max:
            somme += i
        print(somme)

if __name__ == "__main__":
    main()

# The test result is 45000
# The input result is 206582