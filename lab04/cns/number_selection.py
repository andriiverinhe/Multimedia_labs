def z(photo_processing):
    close = True
    while close:
        try:
            locale_close = True
            while locale_close:
                print('Деление на маску == 1')
                print('Умножение на маску == 2')
                print('Сложение двух фотографий == 3')
                print('Вычетание двух фотографий  == 4')
                print('Умножение двух фотографий == 5')
                print('Деление двух фотографий == 6')


                number = int(input('Ведите из перечисленого цифру: '))

                if number == 1:
                    photo_processing = number
                    locale_close = False
                    close = False
                elif number == 2:
                    photo_processing = number
                    locale_close = False
                    close = False
                elif number == 3:
                    photo_processing = number
                    locale_close = False
                    close = False
                elif number == 4:
                    photo_processing = number
                    locale_close = False
                    close = False
                elif number == 5:
                    photo_processing = number
                    locale_close = False
                    close = False
                elif number == 6:
                    photo_processing = number
                    locale_close = False
                    close = False
        except ValueError:
            print("неправильное значение")

    return photo_processing