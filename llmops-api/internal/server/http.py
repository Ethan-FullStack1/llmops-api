#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time      : 2026/6/11 19:21
@Author    : Ethan
@File      : http.py
"""
from flask import Flask

from router import Router


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register(self)
