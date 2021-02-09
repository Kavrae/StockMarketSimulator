import click
from flask.cli import with_appcontext


@click.group()
def cli():
    """Main entry point"""


@cli.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from StockMarketApi.extensions import db
    from StockMarketApi.models import User

    click.echo("create user")
    user = User(username="kavrae", email="croberts.business@gmail.com", password="Parahuman89", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
