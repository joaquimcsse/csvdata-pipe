import pandas as pd

def load(fp:str) -> pd.DataFrame:
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
        dtype=dtypes,
        low_memory=False,
        on_bad_lines="warn",
    )
    print(f"--> Loaded {fp}")
    return df

def inspect(df:pd.DataFrame, fp:str, verbose:bool=True):
    print(f"--> {fp} head 3:")
    df.head(3)
    print(f"--> {fp} info:")
    df.info(verbose=verbose, memory_usage=True)

"""
def clean():

def select():

def transform():

def analyze():

def visualize():

def export():
    DataFrame.to_parquet(path=None, *, engine='auto', compression='snappy',
     index=None, partition_cols=None, storage_options=None, filesystem=None, **kwargs)
"""
def pipe(fp:str=None):
    if fp is None:
        raise ValueError("pipe() expects a csv file path.")
        
    df = load(fp)
    inspect(df, fp, verbose=True)
