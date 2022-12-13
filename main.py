from PIL import Image, ImageDraw
from cns import number_selection
from cns import saave
from cns import closed
from proces import addition
from proces import subtraction
from proces import multiplication
from proces import division
from proces import masck_division
from proces import masck_multiplicarion


close = True
while close:
    number_proces = number_selection.z('')
    print("Вы выбрали процес", number_proces)

    if number_proces == 1 or number_proces == 2:
        cl = True
        photo_mask = 1
        while cl:
            try:
                photo_mask = Image.open(input('Ведите название фотографии  + тип файла: '))
                cl = False
            except FileNotFoundError:
                print('!!! Неверное имя фотографии !!!')
        height_mask = photo_mask.size[0]
        weight_mask = photo_mask.size[1]

        if number_proces == 1:
            photo_prcessed = masck_division.photo_division_mask(photo_mask, height_mask, weight_mask)
            photo_prcessed.show()
            photo_save = saave.preservation(photo_prcessed)
        elif number_proces == 2:
            photo_prcessed = masck_multiplicarion.photo_mult_mask(photo_mask, height_mask, weight_mask)
            photo_prcessed.show()
            photo_save = saave.preservation(photo_prcessed)
        close = closed.closedd(closed)
    else:

        _end = True
        while _end:
            photo = 1
            photo1 = 1
            end = True

            while end:
                try:
                    photo = Image.open(input('Ведите название первой фотографии: '))
                    end = False
                except FileNotFoundError:
                    print('!!! Неверное имя фотографии !!!')
            height = photo.size[0]
            weight = photo.size[1]
            end = True

            while end:
                try:
                    photo1 = Image.open(input('Ведите название второй фотографии: '))
                    end = False
                except FileNotFoundError:
                    print('!!! Неверное имя фотографии !!!')
            height_1 = photo1.size[0]
            weight_1 = photo1.size[1]


            if height_1 == height and weight_1 == weight:
                if number_proces == 3:
                    photo_prcessed = addition.phoro_add_photo_1(photo, photo1, height, weight)
                    photo_prcessed.show()
                    photo_save = saave.preservation(photo_prcessed)
                elif number_proces == 4:
                    photo_prcessed = subtraction.phoro_subteaction_photo_1(photo, photo1, height, weight)
                    photo_prcessed.show()
                    photo_save = saave.preservation(photo_prcessed)
                elif number_proces == 5:
                    photo_prcessed = multiplication.phoro_multiplication_photo_1(photo, photo1, height, weight)
                    photo_prcessed.show()
                    photo_save = saave.preservation(photo_prcessed)
                elif number_proces == 6:
                    photo_prcessed = division.phoro_div_photo_1(photo, photo1, height, weight)
                    photo_prcessed.show()
                    photo_save = saave.preservation(photo_prcessed)
                close = closed.closedd(closed)
                _end = False
            else:
                print("Вы ввели фотографии разных размеров")