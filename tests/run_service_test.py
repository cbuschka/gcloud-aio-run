import unittest

from run import RunService


class RunServiceTest(unittest.TestCase):
  def setUp(self) -> None:
    self.service = RunService(raw={"metadata":
      {
        "name": "service-name"
      },
      "status": {
        "address": {
          "url": "the-url"
        }
      }}
    )

  def test_name_is_accessible(self):
    self.assertEqual(self.service.name, "service-name")

  def test_url_is_accessible(self):
    self.assertEqual(self.service.url, "the-url")
