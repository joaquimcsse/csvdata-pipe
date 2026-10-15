from .datapipe import pipe
import glob, os, sys

def find_csv_paths(power_path:str='', cr_path:str='') -> dict:

    if not os.path.exists(power_path):
        raise FileNotFoundError(f"file: {power_path} not found")
    elif not os.path.exists(cr_path):
        raise FileNotFoundError(f"file: {cr_path} not found")

    power_data = glob.glob(f'{power_path}/*.csv')
    cr_data = glob.glob(f'{cr_path}/*.csv')
    return {"power-files": power_data, "cr-files":cr_data}

def load_all_files(power_path:str='', cr_path:str=''):
    try:
        all_paths = find_csv_paths(power_path=power_path, cr_path=cr_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit('exiting interpreter')

    power_files = all_paths["power-files"]
    cr_files = all_paths["cr-files"]

    for file in power_files:
        pipe(fp=file)

    for file in cr_files:
        pipe(fp=file)
