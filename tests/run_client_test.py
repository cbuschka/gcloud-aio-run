from unittest import TestCase
from unittest.mock import AsyncMock, Mock
import asyncio

from gcloud.aio.run import RunClient


def async_test(f):
  def wrapper(*args, **kwargs):
    coro = asyncio.coroutine(f)
    future = coro(*args, **kwargs)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(future)

  return wrapper


class RunClientTest(TestCase):
  def setUp(self) -> None:
    token = Mock(name="token")
    token.get = AsyncMock(name="token.get", side_effect="token_value")
    resp = AsyncMock(name="resp")
    resp.json = AsyncMock(name="resp.json",
                          return_value={
                            "items": [
                              {"metadata": {"name": "service0"},
                               "status": {"address": {"url": "url-service0"}}},
                              {"metadata": {"name": "service1"},
                               "status": {
                                 "address": {"url": "url-service1"}}}]})
    session = Mock(name="session")
    session.get = AsyncMock(name="session.get", return_value=resp)
    self.client = RunClient(token=token)
    self.client.session = session

  @async_test
  async def test_lists_services(self):
    services = await self.client.list_services("project", "region")
    self.assertEqual([(s.name, s.url) for s in services],
                     [("service0", "url-service0"),
                      ("service1", "url-service1"), ])
