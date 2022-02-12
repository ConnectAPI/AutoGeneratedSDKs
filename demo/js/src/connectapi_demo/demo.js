
// Auto generated file, DO NOT EDIT!


import * as schemas from './schemas';


class Demo{
    constructor(client){
        this.client = client;
        this.service_prefix = '/demo';
    }

    sum_two_numbers(a, b, ){
        let path = '/math/sum'.format();
        let query = {'a': a, 'b': b, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    multiply_two_numbers(a, b, ){
        let path = '/math/mul'.format();
        let query = {'a': a, 'b': b, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    random_int_from_range(a, b, ){
        let path = '/random/range'.format();
        let query = {'a': a, 'b': b, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    random_string(n, ){
        let path = '/random/string'.format();
        let query = {'n': n, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    get_test(){
        let path = '/test/get_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    post_test(){
        let path = '/test/post_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    put_test(){
        let path = '/test/put_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('put', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    delete_test_test(){
        let path = '/test/delete_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('delete', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    options_test(){
        let path = '/test/options_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('options', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    head_test(){
        let path = '/test/head_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('head', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    query_test(a, b, c, d, ){
        let path = '/test/query_test'.format();
        let query = {'a': a, 'b': b, 'c': c, 'd': d, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    query_optional_test(a=null, b=null, c=null, d=null, ){
        let path = '/test/query_optional_test'.format();
        let query = {'a': a, 'b': b, 'c': c, 'd': d, };
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    body_test(body, ){
        let path = '/test/body_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    body_optional_test(body=null){
        let path = '/test/body_optional_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    headers_test(a, ){
        let path = '/test/headers_test'.format();
        let query = {};
        let headers = {'a': a, };
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    headers_optional_test(a=null, ){
        let path = '/test/headers_optional_test'.format();
        let query = {};
        let headers = {'a': a, };
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    form_test(body, ){
        let path = '/test/form_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/x-www-form-urlencoded");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    form_optional_test(body=null){
        let path = '/test/form_optional_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/x-www-form-urlencoded");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    cookies_test(a, ){
        let path = '/test/cookies_test'.format();
        let query = {};
        let headers = {};
        let cookies = {'a': a, };
        let body = {};
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    cookies_optional_test(a=null, ){
        let path = '/test/cookies_optional_test'.format();
        let query = {};
        let headers = {};
        let cookies = {'a': a, };
        let body = {};
        
        let response = this.client.request('post', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    file_test(body, ){
        let path = '/test/file_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('put', this.service_prefix, path, query, body, headers, cookies, content_type="multipart/form-data");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    file_optional_test(body=null){
        let path = '/test/file_optional_test'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = body;
        
        let response = this.client.request('put', this.service_prefix, path, query, body, headers, cookies, content_type="multipart/form-data");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    path_test(a, b, c, ){
        let path = '/test/path_test/{a}/{b}/{c}'.format(a=a, b=b, c=c, );
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('put', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        if (response.status_code == 422){
            // Validation Error
            if (response.headers["Content-Type"] == "application/json"){
                return schemas.HTTPValidationError.from_dict(response.json());
            }
        }
        return response;
    }

    r_test_str(){
        let path = '/test/r_test_str'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_int(){
        let path = '/test/r_test_int'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_none(){
        let path = '/test/r_test_none'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_float(){
        let path = '/test/r_test_float'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_array(){
        let path = '/test/r_test_array'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_dict(){
        let path = '/test/r_test_dict'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_no_200(){
        let path = '/test/r_test_no_200'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 201){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_3xx(){
        let path = '/test/r_test_3xx'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 300){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

    r_test_redirect(){
        let path = '/test/r_test_redirect'.format();
        let query = {};
        let headers = {};
        let cookies = {};
        let body = {};
        
        let response = this.client.request('get', this.service_prefix, path, query, body, headers, cookies, content_type="application/json");
        if (response.status_code == 200){
            // Successful Response
            if (response.headers["Content-Type"] == "application/json"){
                return response.json();
            }
        }
        return response;
    }

}

export default Demo;