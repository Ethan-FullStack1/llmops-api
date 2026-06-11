#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time      : 2026/6/11 19:05
@Author    : Ethan
@File      : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    apphandler = AppHandler()

    def register(self, app: Flask):
        """注册路由"""
        # 1、创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2、讲url与对应的控制器方法绑定
        bp.add_url_rule("/ping", view_func=self.apphandler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.apphandler.completion)

        # 3、在应用上去注册蓝图
        app.register_blueprint(bp)
