#!/usr/bin/env python3

import os
import tempfile
import pytest
import flaskr

from sqlalchemy import create_engine


@pytest.fixture
def client():
    app = flaskr.create_app()

    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    # setup the db here
    app.db = create_engine(f"sqlite:///{app.config['DATABASE']}")

    # initialize the database
    exec = [
        'DROP TABLE IF EXISTS admins',
        '\n\nCREATE TABLE IF NOT EXISTS admins (\n    id INT PRIMARY KEY,\n    email TEXT NOT NULL,\n    password TEXT,\n    session TEXT\n)',
        "\n\nINSERT INTO admins VALUES \n    (0, 'admin@ns.agency', 'bernie_sanders_4_president', '76f46c14b962e97feeea194630efa1196f474e7bd53daa873be5a3fb3df9e2f0')"
    ]

    for statement in exec:
        app.db.execute(statement)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_sqli(client):
    client.set_cookie('localhost', 'session', "' or 1=1--")
    rv = client.get('/')
    print(rv.data)
    assert (b'IF_I_SEE_THIS_THIS_AINT_PATCHED' not in rv.data)
