# ftrack-settings

More friendly setting object
for [Ftrack Python API](https://ftrack-python-api.readthedocs.io/en/master/environment_variables.html). Support
environments, env file, and init override, all powered by Pydantic BaseSetting.

# Why need this?

- **Safty first**! Writing secret API keys in codes is **EXTREMELY** unacceptable!
- **Flexibility**. environment variable or env file can be changed quickly. eg, switch between production and debug.
- **Easy to remember**. Support IDE auto-completion.

# How to use?

Just init a `FtrackSettings` instance, and use it as object anywhere.

```python
import ftrack_api
from ftrack_settings import FtrackSettings

settings = FtrackSettings(_env_file='production.env')
# settings = FtrackSettings(_env_file='debug.env')

session = ftrack_api.Session(server_url=settings.FTRACK_SERVER,
                             api_key=settings.FTRACK_API_KEY,
                             api_user=settings.FTRACK_API_USER)
```

# More details

You can also use `FtrackEnvironmentVariableEnum` to get Ftrack env var keys. Let IDE auto-completion, prevent from typo
errors.

```python
import os
from ftrack_settings.enums import FtrackEnvironmentVariableEnum

print(os.environ[FtrackEnvironmentVariableEnum.FTRACK_EVENT_PLUGIN_PATH.value])
```

You can also override some settings temporarily for purpose.

```python
from ftrack_settings import FtrackSettings

settings = FtrackSettings(FTRACK_API_USER='mock_user@company.com')
```