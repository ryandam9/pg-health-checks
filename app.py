import glob
import os
from datetime import datetime

from config import database, host, password, port, user
from database.execute_query import postgres_execute_query_sqlalchemy
from utils import generate_html_table_from_df

sql_files = []
queries_directory = "./queries"

db_config = {
    "host": host,
    "port": port,
    "database": database,
    "user": user,
    "password": password,
}

# Read all the sql file names
for file_name in glob.glob(f"{queries_directory}/*.sql"):
    sql_files.append(os.path.basename(file_name))

sql_files.sort(key=lambda x: int(x.split("_")[0]))

html_table_string = ""
data_tables = ""

for file_no, file_name in enumerate(sql_files):
    with open(f"{queries_directory}/" + file_name) as query_file:
        query = query_file.read()
        query = query.replace(";", " ")

        print(f"Executing query: {file_name}")
        print("-" * 100)

        print(query)

        # Execute the query
        df = postgres_execute_query_sqlalchemy(db_config, query, None)

        print(df)
        print("")

        if df is not None:
            html_table = generate_html_table_from_df(df, file_name)

            html_table_string += "<br>"
            html_table_string += html_table

            data_tables += "\n" + "$('#" + file_name.replace(".sql", "") + "').DataTable();"

print(data_tables)

# Read HTML template file
html_template = ""
with open("./templates/health_check_template.html", "r") as f:
    html_template = f.read()

html_template = html_template.replace("[data-placeholder]", html_table_string)
html_template = html_template.replace("[dynamic_tables]", data_tables)

ts = datetime.now().strftime("%Y_%m_%d %H:%M").replace(" ", "_").replace(":", "_")

with open(f"./health_check_{ts}.html", "w") as f:
    f.write(html_template)
