# CSV to .parquet pipeline 

Convert data in CSVs to .parquet files with a simple pipeline

## Requirements 
Set up the environment with UV (or your preferred package manager)
```bash
    uv sync
```

## Usage 
```python
    if __name__ == "__main__":
        from preprocessing import topqt_pipeline
        topqt_pipeline.run_pipe()
```
