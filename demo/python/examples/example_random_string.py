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

result = service.random_string(n=42, )
print(result)