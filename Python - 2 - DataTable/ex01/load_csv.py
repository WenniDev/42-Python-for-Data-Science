import pandas as pd
from pathlib import Path


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a dictionary."""

    if not Path(path).is_file():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.endswith('.csv'):
        raise ValueError(f"Invalid file format: {path}")

    data = pd.read_csv(path)

    print(f"Loading dataset of dimensions {data.shape}")
    return data
