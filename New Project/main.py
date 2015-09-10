count = 0
float(count)
while ( True ) :
    inp = input('ENTER PASSWORD: ')
    if inp == 'left' :
        break
    if inp == 'exit()' :
        exit()
        float(count)
    else :
        print ('INVALID PASSWORD')
        count = count + 1
        final = 3 - count
        if count == 2 :
            print(final, 'MORE CHANCE:')
        if count == 1 :
            print(final, 'MORE CHANCES:')
        if count == 3 :
            print('----NO MORE CHANCES: YOU WILL BE LOGGED OFF----')
            input('')
            exit()
while ( True ) :
    cmd = input('TYPE COMMAND: ')
    if cmd == 'help' :
        print('       =+=+=+=+=+=+=+=+=+      ')
        print('       +=+=+=+=+=+=+=+=+=      ')
        print('ENTER ANY NAME OF FAMILY MEMBER')
        print('  MORE COMMANDS WILL BE MADE   ')
        print('   ENTER "exit()" TO EXIT      ')
        print('       =+=+=+=+=+=+=+=+=+      ')
        print('       +=+=+=+=+=+=+=+=+=      ')
        continue
    if cmd == 'Mikey' :
        print('----------')
        print('-----MAKER OF CODE')
        print('-----LOVES PROGRAMMING')
        print('-----LOVES PIANO')
        print('-----HAllELUJAH IS FAVORITE SONG')
        print('----------')
        continue
    if cmd == 'Emily' :
        print('----------')
        print('-----GONE THROUGH CHEMO')
        print('-----LIVES A GOOD LIFE')
        print('-----STILL EXTRACTING DATA...')
        print('-----STILL EXTRACTING DATA...')
        print('-----------')
        continue
    if cmd == 'Lilly' :
        print('VALID KEY')
        continue
    if cmd == 'Dani' :
        print('VALID KEY')
        continue
    if cmd == 'McCord' :
        print('VALID KEY')
        continue
    if cmd == 'Karrynn' :
        print('VALID KEY')
        continue
    if cmd == 'Carston' :
        print('----------')
        print('-----WORKS AT SEVEN-PEAKS')
        print('-----HAS CURLY HAIR')
        print('-----NEEDS A WATCH')
        print('-----HAS GLASSES')
        print('-----WEARS BRACES')
        print('----------')
        continue
    if cmd == 'Kennon' :
        print('----------')
        print('-----LIKES TO CROCHET')
        print('-----LOVES MATH')
        print('-----ENJOYS CHOIR')
        print('-----LIKES TO COOK')
        print('-----------')
        continue
    if cmd == 'Serena' :
        print('VALID KEY')
        continue
    if cmd == 'Cynthia' :
        print('VALID KEY')
        continue
    if cmd == 'exit()' :
        exit()
    else :
        print('NOT ALLOWED')
        continue
input("PRESS <ENTER> WHEN DONE: ")

