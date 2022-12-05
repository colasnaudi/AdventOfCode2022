def main():
    with open('Day1/test/input.txt', 'r') as file:
        data = file.read()
        somme = 0
        max = 0
        for i in data.splitlines():
            if i == '':
                if (somme > max):
                    max = somme
                somme = 0
            else:
                somme += int(i)
        print(max)

if __name__ == "__main__":
    main()

# The test result is 24000
# The input result is 70116