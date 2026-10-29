import pyarrow
import pandas as pd
import re, os

def getFileName(fp):
    name = re.search('[\w]+?(?=\.)', fp)
    return name.group()

def load(
    fp:str,
    verbose:bool=True, 
    drop_nulls:bool=True
    ) -> pd.DataFrame:

    name = getFileName(fp)

    print(f"--> Loading {name}")
    df = pd.read_csv(fp, engine='python')
    print(f"--> Loaded {name}")

    if verbose: 
        print(f"Info:")
        print(df.info(memory_usage=verbose, verbose=verbose), '\n')
    if drop_nulls:
        df.dropna(inplace=True)

    return df, name

def export(
    df:pd.DataFrame,
    path:str,
    name:str,
    verbose:bool=True
    ):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The parquet files path: '{path}' could not be found")

    df.to_parquet(
        path=os.path.join(path, f"{name}.parquet"),
        engine='auto',
        compression='snappy',
        index=None, 
        partition_cols=None, 
        storage_options=None, 
        filesystem=None
    )
