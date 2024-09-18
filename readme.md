## Config.yaml

rename config.yaml.template to config.yaml

## Format the Code

```
ruff check .
ruff format .
```

## Security Vulnerability Scanner

**pip install bandit**

```
bandit app.py
bandit db_config.py
bandit -r .
```

## Run the Web app

```
poerty run python app.py
```

## Open Browser

```
http://127.0.0.1:8000/
```

**First time will load from MySQL**

```
http://127.0.0.1:8000/film/1
```

**Subsequent load will be from Redis**

```
http://127.0.0.1:8000/film/1
```

### Unit Test

Remember to invoke it from redis_mysql_demo folder

```
python3 -m unittest discover -s tests
```

## Redis Commands

```
hgetall film:1

hget film:1 title
```

**Get list of Actors who acted in film 2 along with other films they acted**
```
http://127.0.0.1:8000/film/2/actors
```

## Redis Commands

```
get film_2_actors

```
