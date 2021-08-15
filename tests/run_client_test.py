from unittest import TestCase
from unittest.mock import AsyncMock, Mock
import asyncio

from gcloud.aio.run import RunClient


def async_test(f):
  def wrapper(*args, **kwargs):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(f(*args, **kwargs))
    return result

  return wrapper


class RunClientTest(TestCase):
  def _given_response(self, response):
    token = Mock(name="token")
    token.get = AsyncMock(name="token.get", side_effect="token_value")
    resp = AsyncMock(name="resp")
    resp.json = AsyncMock(name="resp.json", return_value=response)
    session = Mock(name="session")
    session.get = AsyncMock(name="session.get", return_value=resp)
    self.client = RunClient(token=token)
    self.client.session = session

  @async_test
  async def test_lists_services(self):
    self._given_response({
      'kind': 'ServiceList',
      "items": [
        {"metadata": {"name": "service0"},
         "status": {"address": {"url": "url-service0"}}},
        {"metadata": {"name": "service1"},
         "status": {
           "address": {"url": "url-service1"}}}]})
    services = await self.client.list_services("project", "region")
    self.assertEqual([(s.name, s.url) for s in services],
                     [("service0", "url-service0"),
                      ("service1", "url-service1"), ])

  @async_test
  async def test_empty_items(self):
    self._given_response({'kind': 'ServiceList'})
    services = await self.client.list_services("project", "region")
    self.assertEqual([], services)

  @async_test
  async def test_no_kind(self):
    self._given_response({})
    with self.assertRaises(ValueError) as ctx:
      await self.client.list_services("project", "region")
