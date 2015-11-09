from flask import Flask
from application.weixin import weixin
app = Flask(__name__)
app.debug = True
app.register_blueprint(weixin)
if __name__ == '__main__':
    app.run()
