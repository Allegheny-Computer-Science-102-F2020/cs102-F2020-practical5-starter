"""Define the command-line interface for the fibonaccicreator program."""

import typer


from fibonaccicreator import fibonacci

FIBONACCI_FUNCTION_BASE = "fibonacci"
UNDERSCORE = "_"


def main(container: str = typer.Option(...), number: int = typer.Option(...)):
    """Create the list of Fibonacci values in a specified container."""
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo(f"The chosen type of container is the {container}! 🗃")
    typer.echo("")
    typer.echo(f"The program will compute up to the {number}th Fibonacci number! 🔢")
    typer.echo("")
    # TODO: construct the full name of the function to call
    # TODO: construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    # TODO: call the constructed function and capture the result
    # display debugging information with the function's output
    typer.echo(f"  This is the output from the {container} function:")
    typer.echo("")
    # TODO: display the output from the computation
    # display a final message and some extra spacing, asking a question
    # about the efficiency of the approach to computing the number sequence
    typer.echo(
        "So, was this an efficient container for storing the Fibonacci sequence? 🤷"
    )
    typer.echo("")


if __name__ == "__main__":
    typer.run(main)
