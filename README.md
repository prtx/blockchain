# blockchain
A simple blockchain implementation.

# installation

```
$ git clone https://github.com/prtx/blockchain
$ cd blockchain
$ virtualenv venv -p /usr/bin/python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# run it

```$ python3 node_server.py -p port_number```

# tests
Run node_server on ports 3000, 4000, 5000. Then following.
```$ python3 tests.py```