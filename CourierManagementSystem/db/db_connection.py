
import configparser, pathlib, mysql.connector, mysql.connector.errors

_prop = pathlib.Path(__file__).with_name("db.properties")
cfg   = configparser.ConfigParser()
cfg.read(_prop)

def get_connection():
    try:
        params = dict(cfg["mysql"])
        params["port"] = int(params.get("port", 3306))
        return mysql.connector.connect(**params)
    except mysql.connector.Error as e:
        print("DB connection failed:", e)
        raise
