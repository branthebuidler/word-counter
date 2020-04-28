# Word Counter

Simple persistent word frequency service built using Flask. Exposes an API which provides frequency lookup and can process text delivered from a remote endpoint, file (stored on local machine) or as argument.

## Installing
Install dependencies:
```
pip install -r requirements.txt
```
Run dev server:
```
python manager.py run
```

Persistence defaults to /tmp/persistence_file, but this can be customized in config.py. 

## Docs
Docs provided by Swagger. After running, navigate to:
 
http://127.0.0.1:5000/

API examples:
Process simple string text:
```
curl -X POST "http://127.0.0.1:5000/api/words/counter" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"type\": \"string\", \"data\": \"string\"}"
```
Process simple string text:
```
curl -X POST "http://127.0.0.1:5000/api/words/counter" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"type\": \"string\", \"data\": \"string\"}"
```
Process file text:
```
curl -X POST "http://127.0.0.1:5000/api/words/counter" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"type\": \"file\", \"data\": \"/tmp/file\"}"
```
Process endpoint text:
```
curl -X POST "http://127.0.0.1:5000/api/words/counter" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"type\": \"url\", \"data\": \"http://www.google.com\"}"
```

## Running the tests

E2E tests can be run using pytest. Run:
```
py.test
```

## Author

* [Aviv Sugarman](https://github.com/avivsugarman)

