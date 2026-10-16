import glob, os, sys
import pandas as pd

def load(
    fp:str,
    verbose=True, 
    clean:bool=True
    ) -> pd.DataFrame:

    print(f"--> Loading {fp}")
    dtypes = {
    "id": "int32",
    "v": "float32",
    "p": "float32",
    "t": "float32",
    "c": "float32",
    "soc": "float32"
    }
    df = pd.read_csv(
        fp,
        index_col='id',
        dtype=dtypes,
        low_memory=False,
        on_bad_lines="warn",
    )
    print(f"--> Loaded {fp}")

    if verbose: 
        print(f"Info:")
        print(df.info(memory_usage=True, verbose=verbose), '\n')
    if clean:
        df.dropna(inplace=True)

    return df

def visualize(df):
    

"""
def export():
    DataFrame.to_parquet(path=None, *, engine='auto', compression='snappy',
     index=None, partition_cols=None, storage_options=None, filesystem=None, **kwargs)
"""

def pipe(fp:str=None):
    if fp is None:
        raise ValueError("pipe() expects a csv file path.")
        
    df = load(fp, verbose=True, clean=True)
    #visualize(df) 
    #export(df)

def run_pipe():
    if len(sys.argv) < 2:
        raise ValueError("Expecting path to the csv files directory")
    files = []
    for path in sys.argv[1:]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Directory: {path} not found")
        for file in glob.glob(f'{path}/*.csv'):
            files.append(file)
    for file in files:
        pipe(fp=file)
