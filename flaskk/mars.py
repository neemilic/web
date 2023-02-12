from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def a():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести     +!</h1>"


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    return """<title>HELLO, Марс!</title>
    <h1>AAAAAAAAAAAAAAЖди нас, Марс!</h1>
    <<img src="/static/img/mars.png">
    """


@app.route('/promotion_image')
def promotion_image():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>MARS</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link href="static/css/style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Жди нас, Марс!</h1>
	<img src="static/img/mars.png">
      <div class="alert alert-primary" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-secondary" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-success" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-danger" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-warning" role="alert">
  Присоединяйся!
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
</html>"""

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
