from pathlib import Path

import typer

from eventops.services.excel import ExcelError, summarize_excel

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

@app.command("import-excel")
def import_excel( 
    file: Path = typer.Option(..., "--file", "-f", exists=False, help="Ruta al Excel .xlsx"), # noqa: B008
    sheet: str | None = typer.Option(None, "--sheet", "-s", help="Nombre de hoja (opcional)"), # noqa: B008
    preview_rows: int = typer.Option(5, "--preview", "-p", min=1, max=20, help="Filas de preview"), # noqa: B008
) -> None:
    """
    Importa un Excel (.xlsx) y muestra un resumen.
    """
    try:
        summary = summarize_excel(file_path=file, sheet=sheet, preview_rows=preview_rows)
    except ExcelError as exc:
        raise typer.Exit(code=2) from exc

    typer.echo(f"Archivo: {summary.file}")
    typer.echo(f"Hojas: {', '.join(summary.sheet_names)}")
    typer.echo(f"Hoja usada: {summary.sheet_used}")
    typer.echo(f"Dimensiones: {summary.rows} filas x {summary.cols} columnas")
    typer.echo("Columnas (fila 1):")
    for i, col in enumerate(summary.columns, start=1):
        typer.echo(f"  {i:02d}. {col}")

    typer.echo("")
    typer.echo("Preview (incluye cabecera):")
    for row in summary.preview:
        typer.echo(" | ".join(row))
