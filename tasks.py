from pathlib import Path

from invoke import task

PROJECT_DIR = Path(__file__).parent


@task
def compile_test_proto(ctx):
    for path in (PROJECT_DIR / "tests").glob("**/*.proto"):
        ctx.run(
            f"protoc "
            f"-I={str(path.parent)} "
            f"--python_out={str(path.parent)} "
            f"{str(path)}",
            echo=True,
        )
