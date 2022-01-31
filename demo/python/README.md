# demo Service
A plugin SDK for the ConnectAPI backend architecture

> Demo service for the ConnectAPI marketplace and development cycle.


### Install
```
pip install connectapi_demo
```


### Methods
| Name         | Arguments |
---|---
 sum_two_numbers |  a (integer), b (integer),
 multiply_two_numbers |  a (integer), b (integer),
 random_int_from_range |  a (integer), b (integer),
 random_string |  n (integer),
 get_test | 
 post_test | 
 put_test | 
 delete_test_test | 
 options_test | 
 head_test | 
 query_test |  a (integer), b (string), c (boolean), d (number),
 query_optional_test |  a (integer), b (string), c (boolean), d (number),
 body_test | 
 body_optional_test | 
 headers_test |  a (string),
 headers_optional_test |  a (string),
 form_test | 
 form_optional_test | 
 cookies_test |  a (string),
 cookies_optional_test |  a (string),
 file_test | 
 file_optional_test | 
 path_test |  a (string), b (integer), c (number),
 r_test_str | 
 r_test_int | 
 r_test_none | 
 r_test_float | 
 r_test_array | 
 r_test_dict | 
 r_test_no_200 | 
 r_test_3xx | 
 r_test_redirect | 



### Schemas
| Name  | Attributes |
---|---
BodyFileOptional |  a (string), 
BodyFile |  a (string), 
BodyFormOptional |  a (string), 
BodyForm |  a (string), 
HTTPValidationError |  detail (array), 
Nested |  a (integer), 
TestIn |  a (integer),  a_o (integer),  b (string),  b_o (string),  c (boolean),  c_o (boolean),  d (number),  d_o (number),  e (object),  e_o (object),  f (array),  f_o (array),  g (),  g_o (), 
ValidationError |  loc (array),  msg (string),  type (string), 
