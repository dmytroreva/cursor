from flask import Flask, render_template


app = Flask(__name__)


@app.route('/calc/<int:x>/<int:y>/<string:func>')
def calc(x,y,func):
    if func == 'div':
        if y == 0:
            return render_template('index.html', y=y)
        else:
            return render_template('index.html', x=x, y=y, func = "÷", result = x / y)
    elif func == 'sum':
        return render_template('index.html', x=x, y=y, func = "+", result = x + y)
    elif func == 'dif':
        return render_template('index.html', x=x, y=y, func = "-",result = x - y)
    elif func == 'mult':
        return render_template('index.html', x=x, y=y, func = "*",result = x * y)
    else:
        return render_template('index.html', func="None")


@app.route('/')
def hello():
    return 'Hello, in Flask!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)