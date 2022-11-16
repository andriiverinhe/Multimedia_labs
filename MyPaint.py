from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600

        icon = "icons/icon.png"

        self.setWindowTitle("Paint Application")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction((saveAction))
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
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

        fillAction = QAction(QIcon("icons/fill.png"), "Fill", self)
        brushMenu.addAction((fillAction))



        RubberAction = QAction(QIcon("icons/clear.png"), "Rubber", self)
        RubberAction.setShortcut("Ctrl+P")
        brushColor.addAction(RubberAction)
        RubberAction.triggered.connect(self.rubberColor)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        greyAction = QAction(QIcon("icons/grey.jpg"), "Grey", self)
        brushColor.addAction(greyAction)
        greyAction.triggered.connect(self.greyColor)





    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

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

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(.png);;JPEG(.jpeg);;JPG(.jpg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def px_3(self):
        self.brushSize = 3

    def px_5(self):
        self.brushSize = 5

    def px_7(self):
        self.brushSize = 7

    def px_9(self):
        self.brushSize = 9

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