from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QScrollArea
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        top = 0
        left = 0
        width = 1300
        height = 700

        icon = "icons/icon.png"

        self.setWindowTitle("My Paint")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.fill = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Файл")
        brushMenu = mainMenu.addMenu("Размер кисти")
        brushColor = mainMenu.addMenu("Цвет")

        openActtion = QAction(QIcon("icons/open_file.png"), "Open File", self)
        fileMenu.addAction(openActtion)
        openActtion.triggered.connect(self.open)

        saveAction = QAction(QIcon("icons/save.png"), "Сохранить", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction((saveAction))
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Очистить холст", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction((clearAction))
        clearAction.triggered.connect(self.clear)

        px_3Action = QAction(QIcon("icons/px_3.png"), "3 px", self)
        px_3Action.setShortcut("Ctrl+3")
        brushMenu.addAction((px_3Action))
        px_3Action.triggered.connect(self.px_3)

        px_5Action = QAction(QIcon("icons/px_5.png"), "5 px", self)
        px_5Action.setShortcut("Ctrl+5")
        brushMenu.addAction((px_5Action))
        px_5Action.triggered.connect(self.px_5)

        px_7Action = QAction(QIcon("icons/px_7.png"), "7 px", self)
        px_7Action.setShortcut("Ctrl+7")
        brushMenu.addAction((px_7Action))
        px_7Action.triggered.connect(self.px_7)

        px_9Action = QAction(QIcon("icons/px_9.png"), "9 px", self)
        px_9Action.setShortcut("Ctrl+9")
        brushMenu.addAction((px_9Action))
        px_9Action.triggered.connect(self.px_9)

        fillAction = QAction(QIcon("icons/fill.png"), "Заливка", self)
        brushMenu.addAction((fillAction))
        fillAction.triggered.connect(self.set_fill)



        RubberAction = QAction(QIcon("icons/clear.png"), "Ластик", self)
        brushColor.addAction(RubberAction)
        RubberAction.triggered.connect(self.rubberColor)

        blackAction = QAction(QIcon("icons/black.png"), "Чёрный", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        redAction = QAction(QIcon("icons/red.png"), "Красный", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/green.png"), "Зелёный", self)
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Жолтый", self)
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        greyAction = QAction(QIcon("icons/grey.jpg"), "Серый", self)
        brushColor.addAction(greyAction)
        greyAction.triggered.connect(self.greyColor)






    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.fill:
            self.drawing = True
            self.lastPoint = event.pos()
        elif event.button() == Qt.LeftButton and self.fill:
            self.fill_fanction(event)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def set_fill(self):
        self.fill = True

    def fill_fanction(self, event):
        image = self.image
        w, h = image.width(), image.height()
        x, y = event.x(), event.y()
        # Get our target color from origin.
        target_color = image.pixel(x, y)

        have_seen = set()
        queue = [(x, y)]
        def get_cardinal_points(have_seen, center_pos):
            points = []
            cx, cy = center_pos
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = cx + x, cy + y
                if (xx >= 0 and xx < w and
                        yy >= 0 and yy < h and
                        (xx, yy) not in have_seen):
                            points.append((xx, yy))
                            have_seen.add((xx, yy))
            return points
            # Now perform the search and fill.
        p = QPainter(self.image)
        p.setPen(QPen(self.brushColor))

        while queue:
            x, y = queue.pop()
            if image.pixel(x, y) == target_color:
                p.drawPoint(QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))

        self.update()



    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())


    def open(self):
        filePath= QFileDialog.getOpenFileNames(self, "Open Image", "", "ALL Files(*.*)")
        print(filePath)
        if filePath == "":
            return
        self.image.load(filePath[0][0])


    def save(self):
        filePath,_= QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(.png);;JPEG(.jpeg);;JPG(.jpg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)


    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def px_3(self):
        self.brushSize = 3
        self.fill = False


    def px_5(self):
        self.brushSize = 5
        self.fill = False

    def px_7(self):
        self.brushSize = 7
        self.fill = False

    def px_9(self):
        self.brushSize = 9
        self.fill = False

    def blackColor(self):
        self.brushColor = Qt.black

    def rubberColor(self):
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def blueColor(self):
        self.brushColor = Qt.blue

    def greyColor(self):
        self.brushColor = Qt.gray




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()