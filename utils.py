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
    html_table = html_table.replace("<th>", '<th class="th-sm">')
    html_table = html_table.replace("<td>", '<td class="td-sm">')
    html_table = html_table.replace('<th scope="col"', '<th class="th-sm"')
    html_table = html_table.replace('<td scope="col"', '<td class="td-sm"')
    html_table = html_table.replace('<th scope="row"', '<th class="th-sm"')
    html_table = html_table.replace('<td scope="row"', '<td class="td-sm"')
    html_table = html_table.replace('<th scope="col"', '<th class="th-sm"')
    html_table = html_table.replace('<td scope="col"', '<td class="td-sm"')
    html_table = html_table.replace('<th scope="row"', '<th class="th-sm"')
    html_table = html_table.replace('<td scope="row"', '<td class="td-sm"')
    html_table = html_table.replace('<th scope="col"', '<th class="th-sm"')
    html_table = html_table.replace('<td scope="col"', '<td class="td-sm"')
    html_table = html_table.replace('<th scope="row"', '<th class="th-sm"')

    html_table += """
            </div>
        </div>
     </div>
    </div>    
    """

    return html_table
