from PIL import Image, ImageDraw

def photo_division_mask(ph, height, weight):

    global K1, K2, K3
    image_masck = Image.new(mode="RGB", size=(int(height), int(weight)))
    draw = ImageDraw.Draw(image_masck)

    print("Введём начало маски по координатам:\n x - координата покиселя по горизонтале\n y - координата покиселя по вертикалe ")
    print('x(maxsimum): ', image_masck.size[0])
    print('y(maxsimum): ', image_masck.size[1])
    print('0 <= x <= x(maxsimum) and 0 <= y <= y(maxsimum)')
    x = -1
    while x < 0 or x >= image_masck.size[0]:
        try:
            print("Введите x: 0 <= x и х < ", image_masck.size[0], ':')
            x = int(input())
        except ValueError:
            print('x - not True')
    y = -1
    while y < 0 or y >= image_masck.size[1]:
        try:
            print(("Введите y: 0 <= y и y < :", image_masck.size[1]),':')
            y = int(input())
        except ValueError:
            print('y - not True')
    l = -1
    while l <= x or l > image_masck.size[0]:
        try:
            print('Введите верхние правое значемие маски.\n Оно больше ', x,'и меньше или равно', image_masck.size[0],':')
            l = int(input())
        except ValueError:
            print('y - not True')
    h = -1
    while h <= y or h > image_masck.size[1]:
        try:
            print('Введите нижнее левое значемие маски.\n Оно больше ', y,'и меньше или равно', image_masck.size[1],':')
            h = int(input())
        except ValueError:
            print('not true')


    for i in range(height):
        for j in range(weight):
            if x <= i <= l:
                if y <= j <= h:
                    K1 = 0
                    K2 = 0
                    K3 = 0
                    draw.point((i, j), (K1, K2, K3))
                else:
                    K1 = 255
                    K2 = 255
                    K3 = 255
                    draw.point((i, j), (K1, K2, K3))
            else:
                K1 = 255
                K2 = 255
                K3 = 255
                draw.point((i, j), (K1, K2, K3))

    img1 = ph.load()
    img2 = image_masck.load()

    image = Image.new(mode="RGB", size=(int(height), int(weight)))
    draw = ImageDraw.Draw(image)

    for i in range(height):
        for j in range(weight):

            if img2[i, j][0] != 0:
                K1 = img1[i, j][0] // img2[i, j][0]
            elif img2[i, j][0] == 0:
                K1 = img1[i, j][0]

            if img2[i, j][1] != 0:
                K2 = img1[i, j][1] // img2[i, j][1]
            elif img2[i, j][1] == 0:
                K2 = img1[i, j][1]

            if img2[i, j][2] != 0:
                K3 = img1[i, j][2] // img2[i, j][2]
            elif img2[i, j][2] == 0:
                K3 = img1[i, j][2]
            draw.point((i, j), (K1, K2, K3))

    return image