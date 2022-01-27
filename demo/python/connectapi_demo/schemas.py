"""
Auto generated file, DO NOT EDIT!
"""

from typing import List

__all__ = ['BodyFileOptional', 'BodyFile', 'BodyFormOptional', 'BodyForm', 'HTTPValidationError', 'Nested', 'TestIn', 'ValidationError', ]


class BodyFileOptional:
    def __init__(self, a: str = None, ):
        self.a = a
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class BodyFile:
    def __init__(self, a: str, ):
        self.a = a
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class BodyFormOptional:
    def __init__(self, a: str = None, ):
        self.a = a
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class BodyForm:
    def __init__(self, a: str, ):
        self.a = a
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class HTTPValidationError:
    def __init__(self, detail: List = None, ):
        self.detail = detail
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class Nested:
    def __init__(self, a: int = None, ):
        self.a = a
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class TestIn:
    def __init__(self, a: int, b: str, c: bool, d: float, e: dict, f: List, g, a_o: int = None, b_o: str = None, c_o: bool = None, d_o: float = None, e_o: dict = None, f_o: List = None, g_o=None, ):
        self.a = a
        self.a_o = a_o
        self.b = b
        self.b_o = b_o
        self.c = c
        self.c_o = c_o
        self.d = d
        self.d_o = d_o
        self.e = e
        self.e_o = e_o
        self.f = f
        self.f_o = f_o
        self.g = g
        self.g_o = g_o
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


class ValidationError:
    def __init__(self, loc: List, msg: str, type: str, ):
        self.loc = loc
        self.msg = msg
        self.type = type
        
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

