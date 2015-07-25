#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import (
    Flask,
    send_from_directory
)


def create_app():
    app = Flask(__name__)
    app.debug = True
    return app

app = create_app()


@app.route('/download/<path:filename>')
def download(filename):
    if not filename.startswith('order') or not os.path.isfile(filename):
        return 'wrong file name'
    return send_from_directory('.', filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9095)
