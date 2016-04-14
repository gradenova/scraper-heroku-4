# -*- coding:utf-8 -*-
from flask import render_template, request
from src import app
from src.lib.scraper import Scraper


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scraper_list/')
def scraper_list():
    return render_template('scraper/list.html')


@app.route('/scraper_detail/')
def scraper_detail():
    return render_template('scraper/detail.html')


@app.route('/scraper_list/result/', methods=['POST'])
def scraper_list__result():
    params = {
        'base_url':        request.form.get('base_url'),
        'box_selector':    request.form.get('box_selector'),
        'key_selector':    request.form.get('key_selector'),
        'scrape_selector': request.form.get('scrape_selector'),
    }

    scraper = Scraper()

    return scraper.scrape_list(params)


@app.route('/scraper_detail/result/', methods=['POST'])
def scraper_detail__result():
    params = {
        'base_url':        request.form.get('base_url'),
        'box_selector':    request.form.get('box_selector'),
        'key_selector':    request.form.get('key_selector'),
        'link_selector':   request.form.get('link_selector'),
        'scrape_selector': request.form.get('scrape_selector'),
    }

    scraper = Scraper()

    return scraper.scrape_detail(params)
