from flask import Flask, render_template, request, flash
import csv
import random

app = Flask(__name__)
app.secret_key = "FU321C31jkh2KY32hkj1OU321bit33hj21chnipllesfakhjlkj312glkjglkj321ot321852345$&^$^&$^&$"

def get_random_row(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        row = random.choice(rows)
        return row

def get_random_values(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        values = list(reader)
        return random.choice(values)[0]

def sort_into_three_categories(a, b, c):
    list = [a, b, c]
    random.shuffle(list)
    return list

@app.route('/')
def index():
    with open('db.csv', 'r') as f:
        row = get_random_row('db.csv')
        incor = [get_random_values('db.csv'),get_random_values('db.csv')]
        img = row[1]
        answer = row[0]
        answerletter =''
        list=sort_into_three_categories(row[0],incor[0],incor[1])
        if list[0] == answer:
            answerletter= "A"
        elif list[1] == answer:
            answerletter= "B"
        elif list[2] == answer:
            answerletter= "C"
    return render_template('index.html', img=img,answer=list,answerletter=answerletter)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)