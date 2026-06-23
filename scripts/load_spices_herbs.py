"""Simple loader for the processed spices & herbs compliance CSV.

Usage:
    python scripts/load_spices_herbs.py
"""

import pandas as pd
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / 'data' / 'processed' / 'spices_herbs_compliance_2023.csv'
    if not csv_path.exists():
        print(f'Missing file: {csv_path}')
        return
    df = pd.read_csv(csv_path)
    print(f'Loaded {csv_path} — shape: {df.shape}')
    print('\nFirst 10 rows:')
    print(df.head(10).to_string(index=False))
    print('\nSummary (numeric columns):')
    print(df.describe())


if __name__ == '__main__':
    main()
