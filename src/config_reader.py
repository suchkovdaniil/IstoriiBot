from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr

    # Начиная со второй версии pydantic, настройки класса настроек задаются
    # через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан
    # с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


# При импорте файла сразу создастся
# и провалидируется объект конфига,
# который можно далее импортировать из разных мест
config = Settings()

default = DefaultBotProperties(parse_mode='HTML')
bot = Bot(token=config.bot_token.get_secret_value(), default=default)
dp = Dispatcher()