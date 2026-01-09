import typer

app = typer.Typer(
    add_completion=False,
    help="EventOps CLI: herramientas de operaciones y eventos.",
)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """
    Punto de entrada principal de EventOps.
    """
    if ctx.invoked_subcommand is None:
        typer.echo("EventOps CLI inicializada correctamente.")
