# -*- coding:utf-8 -*-
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.compress import Compress

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')
Compress(app)

toolbar = DebugToolbarExtension(app)

import src.views

from .utils import assets

if __name__ == '__main__':
    app.run()
