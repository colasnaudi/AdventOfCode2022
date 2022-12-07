def main():
    file = open('Day4/test/input.txt', "r")
    line = file.readline()
    nb = 0
    while line:
        number = line.split(",")[0]
        nb1 = int(number.split("-")[0])
        nb2 = int(number.split("-")[1])

        number2 = line.split(",")[1]
        nb3= int(number2.split("-")[0])
        nb4 = int(number2.split("-")[1])

        if(((nb1 <= nb3 <= nb2) and (nb1 <= nb4 <= nb2)) or ((nb3 <= nb1 <= nb4) and (nb3 <= nb2 <= nb4))): 
            nb += 1

        line = file.readline()
    file.close()
    print("Number of such pairs : ", str(nb))


if __name__ == "__main__":
    main()

# The test result is 2
# The input result is 562