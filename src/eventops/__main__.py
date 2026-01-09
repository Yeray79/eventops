import typer

app = typer.Typer(add_completion=False, help="EventOps CLI: herramientas de operaciones y eventos.")

@app.command()
def greet(name: str = typer.Option(..., "--name", "-n", help="Nombre a saludar")) -> None:
    """
    Comando de prueba para validar que la CLI funciona correctamente.
    """
    typer.echo(f"Hola, {name}. EventOps está listo.")

def main() -> None:
    app()

if __name__ == "__main__":
    main()
