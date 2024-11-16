from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
        "-i",
        "--input",
        default="input.in",
        type=str,
        help=(
            "The instance file."
        ),
    )
parser.add_argument(
    "-o",
    "--output",
    default="formula.cnf",
    type=str,
    help=(
        "Output file for the DIMACS format (i.e. the CNF formula)."
    ),
)
parser.add_argument(
    "-s",
    "--solver",
    default="./win_solver/glucose-syrup.exe",
    type=str,
    help=(
        "The SAT solver to be used."
    ),
)
parser.add_argument(
    "-v",
    "--verb",
    default=1,
    type=int,
    choices=range(0,2),
    help=(
        "Verbosity of the SAT solver used."
    ),
)
