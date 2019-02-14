import jinja2
from flask import Flask

from app.controller.IndexAction import IndexAction

application = Flask(__name__)

application.jinja_loader = jinja2.ChoiceLoader([
    application.jinja_loader,
    jinja2.FileSystemLoader(['app/ui/views'])
])

@application.route('/', methods=('GET',))
def index():
    return IndexAction().handle()

if __name__ == "__main__":
    application.run(host='0.0.0.0')