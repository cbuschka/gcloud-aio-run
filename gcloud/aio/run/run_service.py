class RunService(object):
  def __init__(self, raw):
    self.raw = raw

  def __getattr__(self, item):
    if item == 'name':
      return self.raw["metadata"]["name"]
    if item == 'url':
      return self.raw["status"]["address"]["url"]

    raise AttributeError
