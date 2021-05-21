# Mindmap

Mindmap is a web service that provides REST API endpoints to create a mind map and store its data in files.

# How to use this API

## Installation
* Clone this repository
* Change directory to `mindmap`
* Run `./bin/run.sh`. This will
    * Install the pyhton module `virtualenv` on your system
    * Create a virtual environment called `.venv`
    * Activate `.venv`
    * Install all the required modules
    * Launch the web app at this address http://127.0.0.1:5000/

## Exposed endpoints
### Create a mind map.

```bash
$ curl -X POST http://localhost:5000/mindmap  -H 'content-type: application/json' -d '{"id": "root_id"}'
```

### Add a leaf (path) to the map.

```bash
$ curl -X POST http://127.0.0.1:5000/leaf/root_id \
  -H 'content-type: application/json' \
  -d '{
    "path" : "I/like/potatoes",
    "text" : "Because reasons"
}'

```
### Read a leaf (path) of the map.

```bash
$ curl -X GET http://127.0.0.1:5000/leaf/root_id \
  -H 'content-type: application/json' \
  -d '{
    "path": "I/like/potatoes"
}'


Expected response:
{
    "path": "i/like/potatoes",
    "text": "Because reasons"
}
```

### Pretty print the whole tree of the mind map.

```bash
$ curl -X GET http://localhost:5000/mindmap  -H 'content-type: application/json' -d '{"id": "root_id"}'

Expected output:
root/
    i/
        like/
            potatoes
        eat/
            tomatoes
```

## Unit test coverage
A unit test coverage report can be obtained using the following commands:
```bash
coverage run --include=mindma*.py -m pytest ./test/
coverage report
```