# csv to parquet pipeline 

#### The idea is to extract the data in a folder of csv files as Pandas DataFrames and store them as parquet files (using the original file names)
#### The advantage is in the nature of storing digital data as parquet files - although not human-readable or editable, they are fast to transport and to be read by digital tools
#### Extra options:  
####    - To get information about the data  
####    - To drop any null values in the data

# Disclaimer

#### Fully manually/human written computer code AND documentation.   
#### Goal: practice of scripting and digital data manipulation concepts
#### Author - joaquimcsse (https://github.com/joaquimcsse)

## Environment
This is a Python project, so set up the environment with UV (or your preferred package manager!)
```bash
    uv sync
```

## Usage - importing
```python
    from csvtoparquet import pipeline

    pipeline.run_pipe(
            verbose=True,
            drop_nulls=True
            )
```
