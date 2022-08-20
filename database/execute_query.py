import sys
import warnings

import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import exc as sa_exc
from sqlalchemy.exc import SQLAlchemyError


def postgres_get_connection(config):
    """
    Creates a connection to the PostgreSQL database.
    """
    host = config["host"]
    port = config["port"]
    database = config["database"]
    user = config["user"]
    password = config["password"]

    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )

        return connection
    except Exception as exception:
        msg1 = "Error getting DB connection: {}".format(exception)
        print(msg1)
        sys.exit(1)


def postgres_execute_query_sqlalchemy(config, query, params):
    """
    Executes given SQL query.
    """
    host = config["host"]
    port = config["port"]
    database = config["database"]
    user = config["user"]
    password = config["password"]

    # Formats query so that special characters are escaped.
    query = sqlalchemy.text(query)

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

            engine = sqlalchemy.create_engine(
                f"postgresql://{user}:{password}@{host}:{port}/{database}", echo=False
            )

            if params is None:
                df = pd.read_sql(query, engine)
                return df
            else:
                df = pd.read_sql(query, engine, params=params)
                return df
    except SQLAlchemyError as e:
        print(e)


def postgres_execute_query(config, query, parameters):
    """
    Executes given SQL query.
    :return  A List of lists, where each list is a record. First list is the column names.
    """
    connection = postgres_get_connection(config)

    records = []  # Query results
    try:
        cur = connection.cursor()

        if parameters is None:
            cur.execute(query)
        else:
            cur.execute(query, parameters)

        # Get Column names
        field_names = [i[0].upper() for i in cur.description]
        records.append(field_names)

        # Process all the records
        for record in cur:
            rec = []

            for i in range(len(record)):
                string_value = ""
                try:
                    string_value = str(record[i]) if record[i] is not None else ""
                except Exception as error:
                    print(
                        "Unable to convert value to String; value: {}".format(record[i])
                    )

                rec.append(string_value)
            records.append(rec)
        cur.close()
    except Exception as err:
        print(err)
        records.append("Exception: " + str(err))
    finally:
        connection.close()

    return records
