import click
from .commands import *

@click.group()
def klipperctl():
    pass

@click.command()
def version():
    click.echo("klippyctl 0.0.1")

klipperctl.add_command(version)
klipperctl.add_command(ping)

if __name__ == '__main__':
    klipperctl()
