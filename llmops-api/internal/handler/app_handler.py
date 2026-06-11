#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time      : 2026/6/11 19:02
@Author    : Ethan
@File      : app_handler.py
"""
from flask import request
from openai import OpenAI


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1、提取从接口中获取的收入，POST
        query = request.json.get("query")

        # 2、构建OpenAI客户端，并发起请求
        client = OpenAI("", "", )

        # 3、得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(model="gpt-3.5-turbo-16k", messages=[
            {"role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
            {"role": "user", "content": query}])

        content = completion.choices[0].message.content

        return content

    def ping(self):
        return {"ping": "pong"}
