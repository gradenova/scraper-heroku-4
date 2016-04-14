# -*- coding:utf-8 -*-
from flask.ext.assets import Bundle, Environment
from .. import app

bundles = {
    'app_css': Bundle(
        'css/lib/pure.min.css',
        'css/app/scraper/*',
        output='gen/app.css',
        filters='cssmin'),

    'app_js': Bundle(
        'js/lib/jquery-2.1.4.min.js',
        'js/lib/lodash.min.js',
        'js/app/*',
        output='gen/app.js',
        filters='jsmin'),
}

assets = Environment(app)

assets.register(bundles)
