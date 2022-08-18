def generate_html_table_from_df(df, filename):
    """
    Generates an HTML table from a Pandas DataFrame.
    """

    filename = filename.replace(".sql", "")

    html_table = f"""
    <div class="row">
        <h1>{filename}</h1>
        <hr>
        <div class="col-1"></div>
        <div class="col-10">
    """

    html_table += "\n"
    html_table += df.to_html(index=False)
    html_table = html_table.replace(
        '<table border="1" class="dataframe">', f'<table class="table table-striped table-bordered" id="{filename}">'
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
        <div class="col-1"></div>
    """

    return html_table
