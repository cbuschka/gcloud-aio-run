# asyncio Python Client for Google Cloud Run

[![Sources](https://img.shields.io/badge/sources-github-blue)](https://github.com/cbuschka/gcloud-aio-run) ![Written in Python](https://img.shields.io/badge/python-3.8,%203.9-blue.svg) [![PyPI](https://img.shields.io/pypi/v/gcloud-aio-run)](https://pypi.org/project/gcloud-aio-run/) [![Build](https://github.com/cbuschka/gcloud-aio-run/workflows/build/badge.svg)](https://github.com/cbuschka/gcloud-aio-run/actions) [![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/cbuschka/gcloud-aio-run/blob/master/license.txt)

## Installation

```
pip install gcloud-aio-run
```

## Usage

### List Cloud Run Services

```python
import aiohttp
from gcloud.aio.run import RunClient


async def print_services(project, region):
  async with aiohttp.ClientSession() as session:
    async with RunClient(session=session) as client:
      services = await client.list_services(project, region=region)
      for service in services:
        print(service.name)
```

## License

Copyright (c) 2021 by [Cornelius Buschka](https://github.com/cbuschka).

[Apache License, Version 2.0](./license.txt)