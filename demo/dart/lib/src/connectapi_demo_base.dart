"""
Auto generated file, DO NOT EDIT!
"""

import 'abstract/client.dart';
import 'schemas.dart';


class Demo{
    AbstractClient client;
    String servicePrefix = '/demo';

    Future<dynamic> sumTwoNumbers(int a, int b, {}) {
        String path = '/math/sum'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> multiplyTwoNumbers(int a, int b, {}) {
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
        String path = '/random/string'.format();
        Map<String, dynamic> query = {'n': n, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> getTest({}) {
        String path = '/test/get_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> postTest({}) {
        String path = '/test/post_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> putTest({}) {
        String path = '/test/put_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('put', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> deleteTestTest({}) {
        String path = '/test/delete_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('delete', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> optionsTest({}) {
        String path = '/test/options_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('options', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> headTest({}) {
        String path = '/test/head_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('head', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> queryTest(int a, String b, bool c, double d, {}) {
        String path = '/test/query_test'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, 'c': c, 'd': d, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> queryOptionalTest({int a,String b,bool c,double d,}) {
        String path = '/test/query_optional_test'.format();
        Map<String, dynamic> query = {'a': a, 'b': b, 'c': c, 'd': d, };
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> bodyTest(TestIn body, {}) {
        String path = '/test/body_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = body.to_dict();
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> bodyOptionalTest({TestIn body}) {
        String path = '/test/body_optional_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = body.to_dict();
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> headersTest(String a, {}) {
        String path = '/test/headers_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {'a': a, };
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> headersOptionalTest({String a,}) {
        String path = '/test/headers_optional_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {'a': a, };
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> formTest({}) {
        String path = '/test/form_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> formOptionalTest({}) {
        String path = '/test/form_optional_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> cookiesTest(String a, {}) {
        String path = '/test/cookies_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> cookiesOptionalTest({String a,}) {
        String path = '/test/cookies_optional_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('post', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> fileTest({}) {
        String path = '/test/file_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('put', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> fileOptionalTest({}) {
        String path = '/test/file_optional_test'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('put', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> pathTest(String a, int b, double c, {}) {
        String path = '/test/path_test/{a}/{b}/{c}'.format(a=a, b=b, c=c, );
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('put', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestStr({}) {
        String path = '/test/r_test_str'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestInt({}) {
        String path = '/test/r_test_int'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestNone({}) {
        String path = '/test/r_test_none'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestFloat({}) {
        String path = '/test/r_test_float'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestArray({}) {
        String path = '/test/r_test_array'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestDict({}) {
        String path = '/test/r_test_dict'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestNo200({}) {
        String path = '/test/r_test_no_200'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTest3xx({}) {
        String path = '/test/r_test_3xx'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }

    Future<dynamic> rTestRedirect({}) {
        String path = '/test/r_test_redirect'.format();
        Map<String, dynamic> query = {};
        Map<String, dynamic> headers = {};
        Map<String, dynamic> body = {};
        var response = this.client.request('get', this.service_prefix, path, query, body, headers);
        return response;
    }