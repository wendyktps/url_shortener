import pyshorteners
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='../templates')
shortener = pyshorteners.Shortener()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_the_page()
    if request.method == 'POST':
        return shorten_link()


def show_the_page():
    return render_template('index.html')


def shorten_link():
    full_url = request.form['url']

    if request.form['shortener'] == 'tinyurl':
        short_url = shortener.tinyurl.short(full_url)
    elif request.form['shortener'] == 'chilpit':
        short_url = shortener.chilpit.short(full_url)
    elif request.form['shortener'] == 'clckru':
        short_url = shortener.clckru.short(full_url)
    else:
        short_url = ""

    return render_template('index.html', full_url=full_url, url=short_url)


if __name__ == '__main__':
    app.run(debug=True)
