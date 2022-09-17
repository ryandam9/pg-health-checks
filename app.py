import glob
import os
import sys
from datetime import datetime

from config import database, port, user
from database.execute_query import postgres_execute_query_sqlalchemy
from utils import generate_html_table_from_df, print_messages

requested_query = 0

if len(sys.argv) == 2:
    requested_query = int(sys.argv[1])

sql_files = []
queries_directory = "./queries"

# User's home directory.
home_directory = os.path.expanduser("~")

# Read DB hostname & password from User's home directory.
try:
    with open(home_directory + "/.pgpass", "r") as pgpass_file:
        for line in pgpass_file:
            if line.startswith("host"):
                host = line.split("=")[1].strip()
            elif line.startswith("password"):
                password = line.split("=")[1].strip()
except Exception as error:
    print(f"Unable to read {home_directory}/.pgpass file.\n" + str(error))
    print(f"Create {home_directory}/.pgpass file with the following contents:")
    print("host = <host>")
    print("password = <password>")
    sys.exit(1)


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
    file_no += 1

    if requested_query != 0 and file_no != requested_query:
        continue

    with open(f"{queries_directory}/" + file_name) as query_file:
        query = query_file.read()
        query = query.replace(";", " ")

        print_messages([[query]], headers=[file_name])

        # Execute the query
        df = postgres_execute_query_sqlalchemy(db_config, query, None)

        print(df)
        print("")

        if df is not None:
            html_table = generate_html_table_from_df(df, file_name)

            html_table_string += "<br>"
            html_table_string += html_table

            # Make the HTML table a DataTable
            data_tables += "\n" + "$('#" + file_name.replace(".sql", "") + "').DataTable();"


# Read HTML template file
html_template = ""
with open("./templates/health_check_template.html", "r") as f:
    html_template = f.read()

ts = datetime.now().strftime("%Y_%m_%d %H:%M")

# The following Data placeholders are going to be replaced:
#    1. HTML tables.
#    2. Javascript to initialize the data tables.
html_template = html_template.replace("[data_placeholder]", html_table_string)
html_template = html_template.replace("[db_endpoint]", host)
html_template = html_template.replace("[db_name]", database)
html_template = html_template.replace("[db_user]", user)
html_template = html_template.replace("[rundate]", ts)

# This is where JS Data tables are created.
html_template = html_template.replace("[dynamic_tables]", data_tables)

ts = ts.replace(" ", "_").replace(":", "_")

with open(f"./reports/health_check_{ts}.html", "w") as f:
    f.write(html_template)
