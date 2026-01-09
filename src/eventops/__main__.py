from .cli import app
git rm -r --cached src/eventops.egg-info src/eventops/__pycache__ || true
def main() -> None:
    app()

if __name__ == "__main__":
    main()
