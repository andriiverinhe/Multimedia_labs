def closedd(closed):
    cld = closed
    close = True
    while close:
        try:
            cl = int(input('Если хотите выйти нажмите 1 если нет 0: '))
            if cl == 1:
                cld = False
                close = False
            elif cl == 0:
                cld = True
                close = False
        except ValueError:
            print("НЕПРАВИЛЬНО")
            print('нужно 1 либо 0')

    return cld