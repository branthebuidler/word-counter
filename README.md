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

## Docs
Docs provided by Swagger. After running, navigate to:
 
http://127.0.0.1:5000/

## Running the tests

E2E tests can be run using pytest. Run:
```
py.test
```

## Author

* [Aviv Sugarman](https://github.com/avivsugarman)

