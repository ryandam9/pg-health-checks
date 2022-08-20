from tabulate import tabulate


def generate_html_table_from_df(df, filename):
    """
    Generates a HTML table from a Pandas DataFrame.

    Parameters
    ----------
    df : Pandas DataFrame
        The DataFrame to be converted to an HTML table.

    filename : str
        SQL query file name. It is used as the "ID" of the html
        table.

    Returns
    -------
        html_table : str
    """

    filename = filename.replace(".sql", "")

    html_table = f"""
    <div class="p-5 mb-4 bg-light rounded-3">
    <h3>{filename}</h3>
        <div class="container-fluid py-4">
            <div class="row">
                <div>
    """

    html_table += "\n"
    html_table += df.to_html(index=False)
    html_table = html_table.replace(
        '<table border="1" class="dataframe">',
        f'<table class="table table-striped table-bordered" id="{filename}">',
    )
    html_table = html_table.replace("<thead>", '<thead class="thead-dark">')
    html_table = html_table.replace('<tr style="text-align: right;">', "<tr>")

    html_table += """
            </div>
        </div>
     </div>

     <div class="alert alert-primary" role="alert">
          Observation:
     </div>

    </div>    
    """

    return html_table


def print_messages(messages, headers):
    """
    Prints the messages in the input list.

    :param messages: List of Lists
    :param headers: List of strings
    :return: None
    """

    print(
        tabulate(
            messages,
            headers=headers,
            tablefmt="fancy_grid",
        )
    )
