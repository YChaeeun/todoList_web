from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    html = render_template('index.html')
    return html

if __name__ == '__main__' :
    app.run(debug=True)

