#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import (
    send_from_directory,
)


def orders(filename):
    if not filename.startswith('order') or not os.path.isfile(filename):
        return 'wrong file name'
    return send_from_directory('.', filename, as_attachment=True)
