import 'package:http/http.dart' as http;


abstract class AbstractClient {
    Future<http.Response> request(
        String method,
        String service_prefix,
        String path,
        {
            Map<String, dynamic> query = {},
            Map<String, dynamic> body = {},
            Map<String, dynamic> headers = {},
            Map<String, dynamic> cookies = {},
        }
    ) async {}
}