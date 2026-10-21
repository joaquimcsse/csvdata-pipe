# csv to parquet pipeline 

#### Purpose - to extract the data in a folder of csv files as Pandas DataFrames and store them as parquet files  
#### Options:  
####    - To get information about the data  
####    - To drop any null values

# Disclaimer

#### Fully manually/human written computer code and documentation.   
#### Goal: practice of scripting and digital data manipulation
#### Author - joaquimcsse

## Environment
Set up the environment with UV (or your preferred project manager)
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
