import pandas as pd
import os

def load(
    fp:str,
    verbose:bool=True, 
    drop_nulls:bool=True
    ) -> pd.DataFrame:

    print(f"--> Loading {fp}")
    df = pd.read_csv(fp)
    print(f"--> Loaded {fp}")

    if verbose: 
        print(f"Info:")
        print(df.info(memory_usage=verbose, verbose=verbose), '\n')
    if drop_nulls:
        df.dropna(inplace=True)

    return df

def export(
    df:pd.DataFrame,
    path:str,
    verbose:bool=True
    ):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The parquet files path: '{path}' could not be found")

    df.to_parquet(
        path=path,
        engine='auto',
        compression='snappy',
        index=None, 
        partition_cols=None, 
        storage_options=None, 
        filesystem=None
    )
