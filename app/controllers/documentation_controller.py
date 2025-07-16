from flask import render_template


def documentation():
    return render_template('index.html')