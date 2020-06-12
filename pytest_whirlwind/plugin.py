import pytest

import tornado.testing


@pytest.fixture
def http_server():
    pass


@pytest.fixture
def http_server():
    pass


@pytest.fixture
def ws_server():
    pass


@pytest.fixture
def ws_client():
    pass


@pytest.fixture
def tcp_server():
    pass


@pytest.fixture
def tcp_client():
    pass


@pytest.fixture
def tls_server():
    pass


@pytest.fixture
def tls_client():
    pass


async def test_foo(tcp_server):
    server = await tcp_server(my_server).start()
    client = await server.client()

    await client.send(b"foo\n") 

    assert await client.read_until(b"\n") == b"foo"
