import 'connectapi_core/connectapi_core.dart';
import 'connectapi_demo/connectapi_demo.dart';

void main(){
    Client.set_url("https://example.com");
    Client.set_token("<TOKEN>");

    var service = Demo(client=Client());

    var result = service.body_optional_test(body=TestIn());
    print(result);
}