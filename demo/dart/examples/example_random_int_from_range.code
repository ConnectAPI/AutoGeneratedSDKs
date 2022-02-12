import 'connectapi_core/connectapi_core.dart';
import 'connectapi_demo/connectapi_demo.dart';

void main(){
    Client.set_url("https://example.com");
    Client.set_token("<TOKEN>");

    var service = Demo(client=Client());

    var result = service.random_int_from_range(a=42, b=42, );
    print(result);
}