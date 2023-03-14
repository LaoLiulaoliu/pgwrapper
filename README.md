# pgwrapper

*A simple, fast way to access postgresql in python.*


### Description

* It is a postgresql python connection pool at lower layer.

* It is a mongo-like query formula system upper layer.

* It is a new version to access postgresql in python3.


### Install
pip install pgwrapper


### Issue

```Error: pg_config executable not found.```
If you meet this following error when installing psycopg2, you may need to install extra library.

In Ubuntu:
```sudo apt install libpq-dev```

In macOs:
```brew install postgresql```
