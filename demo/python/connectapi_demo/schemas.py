"""
Auto generated file, DO NOT EDIT!
"""

from typing import List

__all__ = ['HTTPValidationError', 'ValidationError', ]


class HTTPValidationError:
    def __init__(self, detail: List = None, ):
        self.detail = detail
        
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

