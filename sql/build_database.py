import sqlite3
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "processed" / "spices_herbs_compliance_2023.csv"
DB_PATH = BASE_DIR / "sql" / "compliance.db"
def load_data():
    df = pd.read_csv(CSV_PATH)
    return df
def create_database(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compliance_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            country TEXT,
            prod_code TEXT,
            prod_name TEXT,
            res_name TEXT,
            samples INTEGER,
            samples_pct REAL,
            positive INTEGER,
            positive_pct REAL,
            violations INTEGER,
            violations_pct REAL,
            trace INTEGER,
            mean REAL,
            minimum REAL,
            median REAL,
            percentile_90th REAL,
            maximum REAL
        )
    """)
    conn.commit()
def insert_data(conn, df):
        df.columns = [
            'year', 'country', 'prod_code', 'prod_name', 'res_name', 'samples',
            'samples_pct', 'positive', 'positive_pct', 'violations', 'violations_pct',
            'trace', 'mean', 'minimum', 'median', 'percentile_90th', 'maximum'
        ]
        df.to_sql('compliance_results', conn, if_exists='append', index=False)
        print(f"Inserted {len(df)} rows into compliance_results table")
if __name__ == "__main__":
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} rows")
    
    print("Creating database...")
    conn = sqlite3.connect(DB_PATH)
    create_database(conn)
    
    print("Inserting data...")
    insert_data(conn, df)
    
    conn.close()
    print("Done. Database created at:", DB_PATH)