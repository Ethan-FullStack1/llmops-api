#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time      : 2026/6/11 18:55
@Author    : Ethan
@File      : test.py
"""
from injector import inject, Injector


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A的name:{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
