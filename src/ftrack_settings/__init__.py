from typing import Optional, Union, List

from pydantic import BaseSettings, AnyHttpUrl, validator, SecretStr


class FtrackSettings(BaseSettings):
    FTRACK_SERVER: Optional[AnyHttpUrl]
    FTRACK_API_USER: Optional[str]
    FTRACK_API_KEY: Optional[SecretStr]
    FTRACK_APIKEY: Optional[str]
    FTRACK_EVENT_PLUGIN_PATH: Optional[Union[List, str]]
    FTRACK_API_SCHEMA_CACHE_PATH: Optional[str]
    HTTP_PROXY: Optional[AnyHttpUrl]
    HTTP_PROXY: Optional[AnyHttpUrl]

    @validator('FTRACK_EVENT_PLUGIN_PATH', pre=True)
    def split_str_to_list(cls, v, config, field):
        if isinstance(v, str):
            v = v.split(':')
        return v

    class Config:
        env_file = 'ftrack_secret.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'
