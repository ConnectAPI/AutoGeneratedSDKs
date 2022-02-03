from connectapi_core import Client
from connectapi_demo import Demo
from connectapi_demo import (
    BodyFileOptional,
    BodyFile,
    BodyFormOptional,
    BodyForm,
    HTTPValidationError,
    Nested,
    TestIn,
    ValidationError,
    )



Client.set_url("https://example.com")
Client.set_token("<TOKEN>")

service = Demo(client=Client())

result = service.query_optional_test(a=42, b="lorem", c=True, d=0.6, )
print(result)