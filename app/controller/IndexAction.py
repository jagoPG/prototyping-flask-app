from flask import render_template

class IndexAction:
    def handle(self):
        return render_template('index.html')
