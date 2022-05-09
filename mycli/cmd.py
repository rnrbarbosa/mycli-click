import click
import pkg_resources
from rich.console import Console
from rich.markdown import Markdown



MARKDOWN = """
# Azure Factory CLI tool
_Getting Started_ 🌱

- init       Initializes your project
- docs        Open the link for docs.

_Develop_ ✨

- app       Commands for applications.
			Applications are a collection of services and environments.
- env       Commands for environments.
            Environments are deployment stages
- job       Commands for jobs.
            Jobs are tasks that are triggered by events.

_Release_ 🚀

- pipeline    Commands for pipelines.
                Continuous delivery pipelines to release services.
- deploy      Deploy a Blueprint to a specific environment

_Extend_ 🧸

- collection Commands to for Ansible Collections
- roles      Commands to for Ansible Roles
                Secrets are sensitive information that you need in your application.

_Settings_ ⚙️

- version     Print the version number.
- completion  Output shell completion code.

 *Flags*

-h, --help      help for af-cli

-v, --version   version for af-cli

_Examples_

  Displays the help menu for the "init" command.

  ```$ af init --help```

"""

md = Markdown(MARKDOWN)

class af_help(click.Group):
    def format_help(self, ctx, formatter):
        console = Console()
        console.print(md,justify="left")

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
