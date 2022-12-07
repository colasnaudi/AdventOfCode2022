def main():
    file = open('Day5/test/input.txt', "r")
    line = file.readline()
    pile_max_height = 0
    while line:
        prev_line = line
        line = file.readline()
        if line in ['\n', '\r\n']:
            nb_pile = int(prev_line[len(prev_line)-3])
            break
        pile_max_height += 1
    file.seek(0)
    print("Nombre de pile : ",nb_pile)
    print("Hauteur max des piles : ",pile_max_height, "\n")
    pile = []
    for i in range(pile_max_height):
        line = file.readline()
        pile.append([])
        char_place = 1
        for k in range(nb_pile):
            if line[char_place] != ' ':
                pile[i].append(line[char_place])
            else:
                pile[i].append(None)
            char_place += 4
    #print(pile)
    new_pile = []
    for i in range(nb_pile):
        new_pile.append([])
        for j in range(pile_max_height):
            if pile[j][i] != None:
                new_pile[i].append(pile[j][i])
    print(new_pile, "\n")

    file.seek(0)
    line = file.readline()
    while line:
        if line not in ['\n', '\r\n']:
            line = file.readline()
        else:
            while line:
                line = file.readline()
                if line != '':
                    line = line.split()
                    print("Nb à déplacer : ",line[1])
                    print("Pile de départ : ",line[3])
                    print("Pile d'arrivée : ",line[5])
                    move = new_pile[int(line[3])-1][0:int(line[1])]
                    print ("Avant : ",new_pile)
                    del new_pile[int(line[3])-1][0:int(line[1])]
                    for i in move[::-1]:
                        new_pile[int(line[5])-1].insert(0,i)
                    print ("Après : ",new_pile, "\n")
    file.close()
    for i in new_pile:
        print(i[0], end="")
    print ("\n")

if __name__ == "__main__":
    main()

# The test result is MCD
# The input result is NHWZCBNBF