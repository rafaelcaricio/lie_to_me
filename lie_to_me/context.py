#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lie_to_me pyvows mock library
# https://github.com/rafaelcaricio/lie_to_me/

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Rafael Caricio rafael@caricio.com

from pyvows import Vows, expect

class MockedObject(object):

    class Mock(object):
        def __init__(self, return_value):
            self.return_value = return_value
            self.calls = []

        def __call__(self, *args, **kwargs):
            self.calls.append({"args": args, "kwargs": kwargs })
            return self.return_value

    def __init__(self, _class, arguments):
        self.should_be_mocked = {}
        self.arguments = arguments
        self._class = _class
        self.obj = _class(*arguments[0], **arguments[1])

    def __getattr__(self, attr_name):
        if attr_name in self.should_be_mocked:
            return self.should_be_mocked[attr_name]

        class Wrapper(self._class):
            def __getattribute__(s, an):
                return self.__getattr__(an)

        def wrapper(*args, **kwargs):
            return getattr(self._class, attr_name)(Wrapper(*self.arguments[0], **self.arguments[1]), *args, **kwargs)
        return wrapper

    def mock_method(self, method_name, return_value):
        self.should_be_mocked[method_name] = MockedObject.Mock(return_value)

class LieContext(Vows.Context):

    def _get_obj(self):
        if hasattr(self, 'parent') and self.parent:
            return self.parent._get_obj()
        else:
            return MockedObject(self._class(), self._arguments())

    def _arguments(self):
        return (), {}

    def _class(self):
        raise NotImplementedError

