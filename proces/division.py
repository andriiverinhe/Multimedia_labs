from PIL import Image, ImageDraw

def phoro_div_photo_1(ph, ph_1, height, weight):

    global K1, K2, K3
    image = Image.new(mode="RGB", size=(int(height), int(weight)))
    draw = ImageDraw.Draw(image)

    img2 = ph.load()
    img1 = ph_1.load()

    for i in range(height):
        for j in range(weight):

            if img2[i, j][0] != 0:
                K1 = img1[i, j][0] // img2[i, j][0]
                if K1 > 255:
                    K1 = 255
                elif K1 < 0:
                    K1 = 0
            elif img2[i, j][0] == 0:
                K1 = img1[i, j][0]

            if img2[i, j][1] != 0:
                K2 = img1[i, j][1] // img2[i, j][1]
                if K2 > 255:
                    K2 = 255
                elif K2 < 0:
                    K2 = 0
            elif img2[i, j][1] == 0:
                K1 = img1[i, j][1]

            if img2[i, j][2] != 0:
                K3 = img1[i, j][2] // img2[i, j][2]
                if K3 > 255:
                    K3 = 255
                elif K3 < 0:
                    K3 = 0
            elif img2[i, j][2] == 0:
                K1 = img1[i, j][2]

            draw.point((i, j), (K1, K2, K3))



    return image
