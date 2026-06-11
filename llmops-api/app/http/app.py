#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time      : 2026/6/11 19:26
@Author    : Ethan
@File      : app.py
"""
from injector import Injector

from router import Router
from server.http import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
