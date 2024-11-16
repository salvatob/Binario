from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
        "-i",
        "--input",
        default="puzzle_instances/solvable_6x6.txt",
        type=str,
        help=(
            "The instance file."
        ),
    )
parser.add_argument(
    "-o",
    "--output",
    default="out/output.txt",
    type=str,
    help=(
        "Output file for the DIMACS format (i.e. the CNF formula)."
    ),
)
parser.add_argument(
    "-s",
    "--system",
    default="win",
    type=str,
    help=(
        "Current OS used to specify which glucose solver binary to use."
    ),
)
parser.add_argument(
    "-v",
    "--verb",
    default=2,
    type=int,
    choices=range(0,3),
    help=(
        "Verbosity of the SAT solver used."
    ),
)
