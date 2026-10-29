from .utils import load, export
import glob, os, sys

def run_pipe(verbose:bool=True, drop_nulls:bool=True):

    """
    run_pipe()

    - Checks for two directory paths expected as command line arguments.
        sys.argv[1]: path to the csv files directory.
        sys.argv[2]: path for storing the parquet files

    - If argv[1] is not found, FileNotFoundError() is raised
    - Stores datasets as .parquet files in sys.argv[2]

    """

    if len(sys.argv) != 3:
        raise ValueError(""" Expecting 2 command line arguments: path to the csv files directory
        and path for storing the parquet files """)
    files = []
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError(f"Directory: '{sys.argv[1]}' not found")
    for file in glob.glob(f'{sys.argv[1]}/*.csv'):
        files.append(file)
    for file in files:
        df, name = load(
            file,
            verbose=verbose,
            drop_nulls=drop_nulls,
        )
        export(df, sys.argv[2], name)
