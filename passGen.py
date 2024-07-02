import random, sys, pyperclip

print('---GENERATOR HASEŁ LOSOWYCH---\n')

def pass_gen(number):
    number=int(number)
    char_list = list(r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    random.shuffle(char_list)
    password=[]
    if number <8:
        print("\nPamiętaj, że dobre hasło powinno mieć conajmniej 8 znaków!\n")
    for i in range(0,number):
        password.append(random.choice(char_list))
    password=''.join(password)
    print(password)
    pyperclip.copy(password)
    

def menu():
    choice = input('\nPodaj liczbę znaków z ilu ma składać się Twoje hasło: \nAby zakończyć wpisz "Q"\n')
    if choice.lower() == 'q':
        sys.exit()
    elif not choice.isdecimal() or int(choice) < 1:
        print('\nPodaj liczbę całkowitą większą od 0!\n')
        menu()
    else:
        print()
        pass_gen(choice)
        print('\nHasło zostalo skopiowane do schowka!\n')
        print('\nCzy chcesz wygenerować kolejne hasło?[T/N]\n')
        choice = input()
        if choice.lower() == 't':
            menu()
        elif choice.lower() == 'n':
            sys.exit()
        else:
            print('\nBłąd wyboru, wprowadź T dla "TAK" lub N dla "Nie".\n')
            menu()

menu()