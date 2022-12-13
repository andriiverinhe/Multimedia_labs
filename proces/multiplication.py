from PIL import Image, ImageDraw

def phoro_multiplication_photo_1(ph, ph_1, height, weight):

    image = Image.new(mode="RGB", size=(int(height), int(weight)))
    draw = ImageDraw.Draw(image)

    img1 = ph.load()
    img2 = ph_1.load()


    for i in range(height):
        for j in range(weight):
            K1 = img1[i, j][0] * img2[i, j][0] // 255
            if K1 > 255:
                K1 = 255
            elif K1 < 0:
                K1 = 0
            K2 = img1[i, j][1] * img2[i, j][1] // 255
            if K2 > 255:
                K2 = 255
            elif K2 < 0:
                K2 = 0
            K3 = img1[i, j][2] * img2[i, j][2] // 255
            if K3 > 255:
                K3 = 255
            elif K3 < 0:
                K3 = 0

            draw.point((i, j), (K1, K2, K3))

    return image