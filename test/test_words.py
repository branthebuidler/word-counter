import tempfile


def test_query_word(client):
    rep = client.get("/api/words/stats/example")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'example'
    assert data["counter"] == 0


def test_url(client):
    rep = client.post("/api/words/counter", json={
        "type": "url",
        "data": "http://httpbin.org/stream/20"
    })
    assert rep.status_code == 200
    rep = client.get("/api/words/stats/url")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'url'
    assert data["counter"] == 20


def test_file(client):
    tf = tempfile.mktemp()
    with open(tf, 'w') as fh:
        fh.write('Wow ma9n a SUPER sentence *(man')
    rep = client.post("/api/words/counter", json={
        "type": "file",
        "data": tf
    })
    assert rep.status_code == 200
    rep = client.get("/api/words/stats/man")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'man'
    assert data["counter"] == 2
    rep = client.get("/api/words/stats/super")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'super'
    assert data["counter"] == 1


def test_string(client):
    rep = client.post("/api/words/counter", json={
        "type": "string",
        "data": "I7 am an& ugLy- senteNCe yes I am)"
    })
    assert rep.status_code == 200
    rep = client.get("/api/words/stats/sentence")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'sentence'
    assert data["counter"] == 1
    rep = client.get("/api/words/stats/am")
    assert rep.status_code == 200
    data = rep.get_json()
    assert data["word"] == 'am'
    assert data["counter"] == 2
