import typer

app = typer.Typer()

@app.callback()
def show():
    typer.secho("""
            CLI DOCS
            - help
            """)


def default_callback():
    typer.echo("Running a users command")


users_app = typer.Typer(callback=default_callback)
app.add_typer(users_app, name="users")


@users_app.callback()
def user_callback():
    typer.echo("Callback override, running users command")


@users_app.command(no_args_is_help=True)
def create(name: str):
    typer.echo(f"Creating user: {name}")


if __name__ == "__main__":
    app()
