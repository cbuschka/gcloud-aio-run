from pkg_resources import get_distribution

__version__ = get_distribution('gcloud-aio-run').version

from gcloud.aio.run.run_client import RunClient
from gcloud.aio.run.run_service import RunService

__all__ = ['__version__', 'RunClient', 'RunService']
