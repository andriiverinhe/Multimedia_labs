from PIL import Image, ImageDraw
def phoro_subteaction_photo_1(ph, ph_1, height, weight):

    image = Image.new(mode="RGB", size=(int(height), int(weight)))
    draw = ImageDraw.Draw(image)

    img2 = ph.load()
    img1 = ph_1.load()
    for i in range(height):
        for j in range(weight):
            K1 = img1[i, j][0] - img2[i, j][0]
            K2 = img1[i, j][1] - img2[i, j][1]
            K3 = img1[i, j][2] - img2[i, j][2]
            draw.point((i, j), (K1, K2, K3))

    return image