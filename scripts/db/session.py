from pathlib import Path

from dotenv import dotenv_values
from sqlalchemy import create_engine, engine, URL
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent


def get_engine(
        dotenv_file: str = f"{BASE_DIR}/db/.env"
    ) -> engine.Engine:
    """
    データベース接続のためのEngineを作成する。

    Parameters
    ----------
    dotenv_file : str, default f"{BASE_DIR}/db/.env"
        .envファイルのパスおよびファイル名
    
    Returns
    -------
    engine.Engine
        データベース接続のためのEngine
    """
    config = dotenv_values(dotenv_file)

    url_object = URL.create(
        "postgresql+psycopg",
        username=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],  # plain (unescaped) text
        host=config.get("POSTGRES_HOST", "postgres"),
        port=config.get("POSTGRES_PORT", "5432"),
        database=config.get("POSTGRES_DB", "postgres"),
        query={"options": f"-c search_path={config.get('POSTGRES_SCHEMA', 'public')}"},
    )

    return create_engine(url_object)


def get_session(
        dotenv_file: str = f"{BASE_DIR}/db/.env"
    ) -> sessionmaker:
    """
    データベース接続のためのSessionを作成する。

    Parameters
    ----------
    dotenv_file : str, default f"{BASE_DIR}/db/.env"
        .envファイルのパスおよびファイル名
    
    Returns
    -------
    sessionmaker
        データベース接続のためのSession
    """
    engine = get_engine(dotenv_file)
    return sessionmaker(engine)
