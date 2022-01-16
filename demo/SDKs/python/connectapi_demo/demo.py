"""
Auto generated file, DO NOT EDIT!
"""
from typing import List, Any

from .schemas import (
    BodyFileOptional,
    BodyFile,
    BodyFormOptional,
    BodyForm,
    HTTPValidationError,
    Nested,
    TestIn,
    ValidationError,
    )


class Demo:
    def __init__(self, client):
        self.client = client
        self.service_prefix = '/demo'

    def sum_two_numbers(self, a: int, b: int, ):
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

    def multiply_two_numbers(self, a: int, b: int, ):
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
        path = '/random/string'.format()
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

    def get_test(self, ):
        path = '/test/get_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def post_test(self, ):
        path = '/test/post_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def put_test(self, ):
        path = '/test/put_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('put', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def delete_test_test(self, ):
        path = '/test/delete_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('delete', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def options_test(self, ):
        path = '/test/options_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('options', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def head_test(self, ):
        path = '/test/head_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('head', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def query_test(self, a: int, b: str, c: bool, d: None, ):
        path = '/test/query_test'.format()
        query = {'a': a, 'b': b, 'c': c, 'd': d, }
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

    def query_optional_test(self, a: int = None, b: str = None, c: bool = None, d: None = None, ):
        path = '/test/query_optional_test'.format()
        query = {'a': a, 'b': b, 'c': c, 'd': d, }
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

    def body_test(self, body: TestIn, ):
        path = '/test/body_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def body_optional_test(self, body: None = None):
        path = '/test/body_optional_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def headers_test(self, a: str, ):
        path = '/test/headers_test'.format()
        query = {}
        headers = {'a': a, }
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

    def headers_optional_test(self, a: str = None, ):
        path = '/test/headers_optional_test'.format()
        query = {}
        headers = {'a': a, }
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

    def form_test(self, body: BodyForm, ):
        path = '/test/form_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def form_optional_test(self, body: BodyFormOptional = None):
        path = '/test/form_optional_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def cookies_test(self, a: str, ):
        path = '/test/cookies_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def cookies_optional_test(self, a: str = None, ):
        path = '/test/cookies_optional_test'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('post', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def file_test(self, body: BodyFile, ):
        path = '/test/file_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('put', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def file_optional_test(self, body: BodyFileOptional = None):
        path = '/test/file_optional_test'.format()
        query = {}
        headers = {}
        body = body.to_dict()
        response = self.client.request('put', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def path_test(self, a: str, b: int, c: None, ):
        path = '/test/path_test/{a}/{b}/{c}'.format(a=a, b=b, c=c, )
        query = {}
        headers = {}
        body = {}
        response = self.client.request('put', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        if response.status_code == 422:
            """Validation Error"""
            if response.headers.get("Content-Type", None) == "application/json":
                return HTTPValidationError.from_dict(response.json())
        return response

    def r_test_str(self, ):
        path = '/test/r_test_str'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_int(self, ):
        path = '/test/r_test_int'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_none(self, ):
        path = '/test/r_test_none'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_float(self, ):
        path = '/test/r_test_float'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_array(self, ):
        path = '/test/r_test_array'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_dict(self, ):
        path = '/test/r_test_dict'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_no_200(self, ):
        path = '/test/r_test_no_200'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 201:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_3xx(self, ):
        path = '/test/r_test_3xx'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 300:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response

    def r_test_redirect(self, ):
        path = '/test/r_test_redirect'.format()
        query = {}
        headers = {}
        body = {}
        response = self.client.request('get', self.service_prefix, path, query, body, headers)
        if response.status_code == 200:
            """Successful Response"""
            if response.headers.get("Content-Type", None) == "application/json":
                return response.json()
        return response
