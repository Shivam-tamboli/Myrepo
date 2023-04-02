# game to find the random number
n  = 18
number_of_gusses=1
print("number of gusses is limited to only 10 times:")
while(number_of_gusses<10):
    gusses_number = int(input("gusses the number:\n"))
    if gusses_number<18:
        print("you enterd less value please increase the number :\n")
    elif gusses_number>18:
        print("you enterd greater value please decrase the number :\n")
    else:
        print("you won the game:\n")
        print(number_of_gusses,"num. of gusses he took for finish:\n")
        break
    print(10-number_of_gusses,"num. of gusses left")
    number_of_gusses = number_of_gusses + 1
    if(number_of_gusses>10):
        print("Game over")