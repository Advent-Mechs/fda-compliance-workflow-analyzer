Dataset: spices_herbs_compliance_2023.csv

Path: data/processed/spices_herbs_compliance_2023.csv

Description:
- Processed extraction of FDA pesticide residue monitoring results for spices and herbs (FY2023).
- Each row corresponds to a product-country-pesticide measurement summary (aggregated across samples).

Columns (as in CSV header):
- Year
- Country
- ProdCode
- ProdName
- ResName
- Spls.
- Spls%
- Pos.
- Pos%
- Vio.
- Vio%
- Trace.
- Mean
- Minimum
- Median
- 90th
- Maximum

Usage (Python):

import pandas as pd
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'data' / 'processed' / 'spices_herbs_compliance_2023.csv'
df = pd.read_csv(p)
print(df.shape)
print(df.head())

Notes:
- Values are as provided by the processed pipeline; numeric fields may contain 0. or 0.0 placeholders for missing/zero values.
- Confirm licensing/source before external redistribution.
