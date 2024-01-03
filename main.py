from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QFont
import pandas as pd
import sys
class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.loadMovies()
        self.initialize()

    def initialize(self):
        self.setGeometry(200,200, 600, 600)
        self.setWindowTitle("Random Movie Picker")
        self.displayWidgets()

    def displayWidgets(self):
        self.btn = QPushButton(self)
        self.btn.resize(400, 100)
        self.btn.move(100, 350)
        self.btn.setText("Pick a movie!")
        self.btn.clicked.connect(self.pickMovie)

        self.title_label = QLabel(self)
        self.year_label = QLabel(self)
        self.url_label = QLabel(self)
        self.title_label.resize(600, 200)
        self.year_label.resize(600, 200)
        self.url_label.resize(600, 200)
        self.title_label.move(50, 50)
        self.year_label.move(50, 120)
        self.url_label.move(50, 190)
        self.title_label.setWordWrap(True)

    def loadMovies(self):
        file = 'movies.csv'
        self.movies_df = pd.read_csv(file)

    def pickMovie(self):
        random_movie = self.movies_df.sample()
        titulo = random_movie['Name'].iloc[0]
        ano = int(random_movie['Year'].iloc[0])
        url = random_movie['Letterboxd URI'].iloc[0]

        # Update labels with new movie information
        self.title_label.setText(f"Title: {titulo}")
        self.title_label.setFont(QFont('Arial', 20))
        self.year_label.setText(f"Year: {ano}")
        self.year_label.setFont(QFont('Arial', 20))
        self.url_label.setText(f"<a href='{url}'>Letterboxd</a>")
        self.url_label.setFont(QFont('Arial', 20))
        self.url_label.setOpenExternalLinks(True)

        # Update button text and position
        self.btn.setText("Pick another movie!")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())