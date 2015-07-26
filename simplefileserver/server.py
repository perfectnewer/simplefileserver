#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from flask import (
    Flask,
)

from .dispatcher import init_dispatcher


def create_app():
    app = Flask(__name__)
    app.debug = True
    init_dispatcher(app)
    return app

def runserver():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', default=9095)
    args = parser.parse_args()
    app = create_app()
    app.run(host=args.host, port=int(args.port))


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=9095)
