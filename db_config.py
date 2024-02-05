import pymysql
import redis
import yaml


def load_config():
    """Load configuration from the YAML file.

    Returns:
        dict: Configuration data.
    """
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


config = load_config()

# def get_redis_connection():
#     """Create a Redis connection using the configuration.

#     Returns:
#         Redis: Redis connection object.
#     """
#     return redis.Redis(
#         host=config["redis-upstash"]["host"],
#         port=config["redis-upstash"]["port"],
#         db=0,
#         decode_responses=True,
#         username=config["redis-upstash"]["user"],
#         password=config["redis-upstash"]["password"],
#         ssl=True,
#     )

def get_redis_connection():
    """Create a Redis connection using the configuration.

    Returns:
        Redis: Redis connection object.
    """
    return redis.Redis(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=0,
        decode_responses=True,
        username=config["redis"]["user"],
        password=config["redis"]["password"],
    )


def get_mysql_connection():
    """Create a MySQL connection using the configuration.

    Returns:
        Connection: MySQL connection object.
    """
    return pymysql.connect(
        host=config["mysql"]["host"],
        port=config["mysql"]["port"],
        user=config["mysql"]["user"],
        password=config["mysql"]["password"],
        db="dbworldgc_mysql",
    )
