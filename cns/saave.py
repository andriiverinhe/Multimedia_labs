from PIL import ImageFilter
from PIL import Image
from PIL import ImageEnhance

def preservation(photo_save):
    close = True
    while close:
        try:
            factor = int(input('Если хотите сохранить напишите 1 а если нет 0: '))
            if factor == 1:
                photo_out = input('Ведите имя фото: ')
                photo_save.save('C:/Users/User/Desktop/Multimedia/lab04/save_photo/' + photo_out + '.jpeg')
                close = False
            elif factor == 0:
                close = False

        except ValueError:
            print("неправильное значение")
    return
