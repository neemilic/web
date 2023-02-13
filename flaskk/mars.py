from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def a():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('base.html', **param)

@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def index1(prof):
    return render_template('train.html', title='training', prof=prof)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')