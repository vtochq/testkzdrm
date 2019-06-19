##### Tasks
GET http://127.0.0.1:8000/tasks/
GET http://127.0.0.1:8000/tasks/1/
POST http://127.0.0.1:8000/tasks/
~~~~
{
    "name": "New task",
    "tag": [
        1,
        2
    ],
    "descr": "some task description"
}
~~~~

##### Tags
GET http://127.0.0.1:8000/tags/
GET http://127.0.0.1:8000/tags/1/
POST http://127.0.0.1:8000/tags/
~~~~
{
    "name": "new tag",
}
~~~~


See comments in serializers.py if you want more data in get queries