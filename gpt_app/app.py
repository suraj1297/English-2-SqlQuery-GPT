import click
from db import connect_to_db, execute_query
from openai_util import generate_sql

@click.command()
@click.option('--query', help='What kind of data would you like to fetch from database ?')
@click.option('--model', default=0, help='1: Trained only on order database schema. 2: Trained on spider dataset')
def generate_query_and_fetch_data(query, model):
    sql_query = generate_sql(query, model)
    conn = connect_to_db()
    data = execute_query(conn, sql_query)
    conn.close()

    if len(data) == 0:
        click.echo(click.style(f"No data found'", fg="red", bold=True))
    else:
        for row in data:
            click.echo(row)

    click.echo(click.style('****************************************************************', fg="yellow"))
    click.echo(click.style(f'SQL Query ->   {sql_query}', fg="green", bold=True))
    
if __name__ == '__main__':
    generate_query_and_fetch_data()
