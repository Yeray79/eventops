from typer.testing import CliRunner

from eventops.cli import app

runner = CliRunner()

def test_cli_root_runs():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "EventOps CLI inicializada correctamente." in result.stdout
