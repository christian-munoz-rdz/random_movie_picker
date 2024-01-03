from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QFileDialog, QMessageBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
import pandas as pd
import sys


class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        #Banderas para saber si se ha cargado el archivo
        self.file_open = False
        self.initialize()

    def initialize(self):
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("Random Movie Picker")
        self.setWindowIcon(QIcon("movie.ico"))
        self.displayWidgets()

    def displayWidgets(self):
        #Definicion de los botones
        #Boton para elegir una pelicula
        self.btn_pick = QPushButton(self)
        self.btn_pick.resize(200, 100)
        self.btn_pick.move(100, 350)
        self.btn_pick.setText("Pick a movie!")
        #Conectamos el boton a la funcion pickMovie
        self.btn_pick.clicked.connect(self.pickMovie)

        #Boton para cargar el archivo csv
        self.btn_load = QPushButton(self)
        self.btn_load.resize(200, 100)
        self.btn_load.move(350, 350)
        self.btn_load.setText("Load movies")
        #Conectamos el boton a la funcion loadMovies
        self.btn_load.clicked.connect(self.loadMovies)

        hlyt_buttons = QHBoxLayout()
        hlyt_buttons.addWidget(self.btn_pick)
        hlyt_buttons.addWidget(self.btn_load)

        #Definicion de los labels
        self.title_label = QLabel(self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.year_label = QLabel(self)
        self.year_label.setAlignment(Qt.AlignCenter)
        self.url_label = QLabel(self)
        self.url_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(600, 200)
        self.year_label.resize(600, 200)
        self.url_label.resize(600, 200)
        self.title_label.move(50, 50)
        self.year_label.move(50, 120)
        self.url_label.move(50, 190)
        self.title_label.setWordWrap(True)

        vlyt_principal = QVBoxLayout()
        vlyt_principal.addWidget(self.title_label)
        vlyt_principal.addWidget(self.year_label)
        vlyt_principal.addWidget(self.url_label)
        vlyt_principal.addLayout(hlyt_buttons)
        self.setLayout(vlyt_principal)


    def loadMovies(self):
        #Abrir el archivo csv con los datos de las peliculas
        file_name = QFileDialog.getOpenFileName(self,"Abrir archivos", "../../", "CSV(*.csv)")
        if file_name[0] == "":
            QMessageBox.warning(self, "Advertencia", "No ha seleccionado ningun archivo")
        else:
            QMessageBox.information(self, "Datos cargados", "Datos cargados correctamente")
            self.movies_df = pd.read_csv(file_name[0])
            self.file_open = True

    def pickMovie(self):
        if self.file_open == False:
            QMessageBox.warning(self, "Advertencia", "No hay datos cargados")
        else:
            random_movie = self.movies_df.sample()
            titulo = random_movie['Name'].iloc[0]
            ano = int(random_movie['Year'].iloc[0])
            url = random_movie['Letterboxd URI'].iloc[0]
            # Actualizar el texto de los labels
            self.title_label.setText(f"Title: {titulo}")
            self.title_label.setFont(QFont('Arial', 20))
            self.year_label.setText(f"Year: {ano}")
            self.year_label.setFont(QFont('Arial', 20))
            self.url_label.setText(f"<a href='{url}'>Letterboxd</a>")
            self.url_label.setFont(QFont('Arial', 20))
            self.url_label.setOpenExternalLinks(True)
            self.btn_pick.setText("Pick another movie!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())