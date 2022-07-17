from pydantic import BaseSettings

from enums import EnvEnum


class ServerSettings(BaseSettings):
    app_name: str = "Fast API Server"
    app_version: str = "0.0.1"
    app_env: EnvEnum = EnvEnum.DEV


server_settings = ServerSettings()
