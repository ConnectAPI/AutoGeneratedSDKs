"""
Auto generated file, DO NOT EDIT!
"""
from typing import List, Any

from .schemas import (
    HTTPValidationError,
    ValidationError,
    )


class Demo:
    def __init__(self, client):
        self.client = client
        self.service_prefix = '/demo'

    def sum_tow_numbers(self, a: int, b: int, ):
        path = '/math/sum'.format()
        query = {'a': a, 'b': b, }
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def multiply_tow_numbers(self, a: int, b: int, ):
        path = '/math/mul'.format()
        query = {'a': a, 'b': b, }
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def random_int_from_range(self, a: int, b: int, ):
        path = '/random/range'.format()
        query = {'a': a, 'b': b, }
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def random_string(self, n: int, ):
        path = '/random/secure'.format()
        query = {'n': n, }
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response
