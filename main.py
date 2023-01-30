from PyQt5 import QtWidgets, QtGui
from PIL import Image, ImageDraw, ImageOps

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ... create widgets and layout

        # add a label to show the border size
        self.borderSizeLabel = QtWidgets.QLabel(self)
        self.borderSizeLabel.setText("Border Size")
        self.borderSizeLabel.move(10, 10)
        self.borderSizeLabel.resize(100, 30)

        # add a input box to get the border size
        self.borderSize = QtWidgets.QLineEdit(self)
        self.borderSize.move(10, 40)
        self.borderSize.resize(100, 30)

        self.openButton = QtWidgets.QPushButton('Open Image', self)
        self.openButton.clicked.connect(self.openImage)
        self.openButton.move(10, 100)
        self.openButton.resize(100, 30)

        self.imageLabel = QtWidgets.QLabel(self)
        self.imageLabel.move(10, 150)
        self.imageLabel.resize(500, 500)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Image Viewer')

    def openImage(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if fileName:
            # Add input box to get the border size
            border_width = int(self.borderSize.text())
            img = Image.open(fileName)
            width, height = img.size
            
            for i in range(border_width):
                # Border color
                border_color = (57, 180, 142)
                # Draw the border
                draw = ImageDraw.Draw(img)
                draw.rectangle((i, i, width - i - 1, height - i - 1), outline=border_color)
                            # Gradient background color
            gradient = Image.new("L", (width, height), 0)
            draw_gradient = ImageDraw.Draw(gradient)
            draw_gradient.rectangle((0, 0, width, height), fill=255)
            gradient = gradient.resize((width, height), Image.ANTIALIAS)
            gradient = ImageOps.colorize(gradient, (0, 0, 0), (0, height, 0))
            background = Image.alpha_composite(gradient.convert("RGBA"), img)

            # Save the image
            background.save("screenshot_with_border_and_gradient.png")

            # Display the image in the image view
            self.imageLabel.setPixmap(QtGui.QPixmap(fileName))

app = QtWidgets.QApplication([])
window = MyWindow()
window.show()
app.exec_()

