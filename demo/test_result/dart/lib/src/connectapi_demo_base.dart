"""
Auto generated file, DO NOT EDIT!
"""

import 'abstract/client.dart';
import 'schemas.dart';


class Demo{
    AbstractClient client;
    String servicePrefix = '/demo';

    Future<dynamic> sumTowNumbers(int a, int b, {}) {
        String path = '/math/sum'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> multiplyTowNumbers(int a, int b, {}) {
        String path = '/math/mul'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> randomIntFromRange(int a, int b, {}) {
        String path = '/random/range'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> randomString(int n, {}) {
        String path = '/random/secure'.format();
        Map<String, dynamic> query = {'n': n, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }