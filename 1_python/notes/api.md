# API

## Definitions

- An API (Application Programming Interface) is a set of rules, functions, or tools that lets one piece of software talk to another - without needing to know how the other works internally.
- An API is created to give us access to data, to provide us with an abstraction of the implementation

Analogy: A restaurant menu
- Menu (API)
- Names of the dishes (API methods)
- Placing the order (make a request)
- The kitchen (internal code) prepares food (response)
- We don't need to know how the food is made - just use the menu

## Type of APIs

- Programming language APIs - build-in functions/methods
- Operating system APIs - let a program access system resources (e.g file handling)
- Web-based APIs (most common) - let apps talk over the internet (e.g weather, maps)
- Library/framework APIs - extend app functionality (e.g numpy, pytorch, react)

Examples:

```python
# String APi
"hello".upper()

# File system API
with open("foo.txt", "w") as f:
    f.write("Bar")

# Web API
r = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = r.json()
joke["setup"], joke["punchline"]
```

## How web APIs work

1. **Request**: A client sends an HTTP request to an API URL (endpoint) using a method (GET, POST)
2. **Processing**: The server receives and processes the request
3. **Response**: The server sends back data (usually in JSON format)
4. **Delivery**: The API returns this data to the client

- Protocol used: HTTP
- Request components: URL, method, headers, body (optional)
- Response: status code, headers, body

[HTTP header fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

[HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

### REST API

REST (Representational State Transfer) -> common architecture for web APIs with key principles:
- client-server: separation of fe and be
- stateless: each request is dependent, no session stored on server
- cacheable: responses can be cached for performance
- uniform interface: standardized method of interaction (URLs, HTTP methods, etc)
- layered system: APIs can be managed across multiple layers

> Since REST is stateless, clients must send all necessary data (e.g auth tokens) with every requests
