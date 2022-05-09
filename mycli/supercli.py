import click
import pkg_resources
from rich.console import Console
from rich.markdown import Markdown

from pathlib import Path
script_path = Path( __file__ ).absolute()

from rich.tree import Tree
from rich import print
from rich.panel import Panel


def command_tree(obj):
    if isinstance(obj, click.Group):
        return {name
                for name, value in obj.commands.items()}

class af_help(click.Group):
    def format_help(self, ctx, formatter):
        with open(script_path.parent.joinpath("README.md"))as md:
            MARKDOWN = Markdown(md.read())
            console = Console()
            console.print(MARKDOWN,justify="left")
            tree = Tree("af")
            for sc in command_tree(af):
                tree.add(sc)
            print(Panel(tree))

@click.group(cls=af_help)
def af():
    pass

@af.command()
def init():
    click.secho("Initialize tasks")

@af.command()
def docs():
    click.launch("https://click.palletsprojects.com/")


@af.command()
def version():
    version = pkg_resources.get_distribution('mycli').version
    click.echo(version)
