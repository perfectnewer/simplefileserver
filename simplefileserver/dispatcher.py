#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib

from flask import (
    Blueprint,
)

dispatchers= {
    'download':[
        ('orders', ['GET'], '/ownload/<path:filename>')
    ]
}

dispatcher = Blueprint('dispatcher', __name__)

def init_dispatcher(app):
    for handler_name, routes in dispatchers.iteritems():
        handler = importlib.import_module(name='.'+handler_name,
                                          package='simplefileserver.handler')
        for route in routes:
            func_name, methods, rule = route
            func = getattr(handler, func_name)
            dispatcher.add_url_rule(rule=rule,
                                    endpoint=func_name,
                                    view_func=func,
                                    methods=methods)
    app.register_blueprint(dispatcher)
