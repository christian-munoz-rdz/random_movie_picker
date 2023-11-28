import csv
import random
import webbrowser
import os

with open('watchlist.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

def selectMovie():
    movie = data[random.randint(0,len(data))]
    return movie

def main():
    while True:
        movie = selectMovie()
        print(f"""
                Title: {movie[1]}
                Year: {movie[2]}""")
        webbrowser.open(movie[3])
        answer = input("Another movie? y/n >>>")
        if answer == "n" or answer == "N":
            break

if __name__ == "__main__":
    main()
    os.system("pause")