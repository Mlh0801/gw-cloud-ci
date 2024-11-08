import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="gw_cloud_ci",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="gw_cloud_ci_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from gw_cloud_ci.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export gw_cloud_ci_KEY=value
export gw_cloud_ci_KEY="@int 42"
export gw_cloud_ci_KEY="@jinja {{ this.db.uri }}"
export gw_cloud_ci_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
gw_cloud_ci_ENV=production gw_cloud_ci run
```

Read more on https://dynaconf.com
"""
