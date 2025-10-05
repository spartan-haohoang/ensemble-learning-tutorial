#!/usr/bin/env python3
"""
Data validation script for the ensemble learning project
"""

import pandas as pd
import numpy as np
from pathlib import Path
import argparse
import sys


def validate_csv_data(file_path: str) -> bool:
    """Validate CSV data file"""
    try:
        df = pd.read_csv(file_path)
        
        print(f"📊 Validating {file_path}")
        print(f"   Shape: {df.shape}")
        print(f"   Columns: {list(df.columns)}")
        print(f"   Data types: {df.dtypes.to_dict()}")
        
        # Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.any():
            print(f"   ⚠️  Missing values: {missing_values[missing_values > 0].to_dict()}")
        else:
            print(f"   ✅ No missing values")
        
        # Check for duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"   ⚠️  Duplicate rows: {duplicates}")
        else:
            print(f"   ✅ No duplicate rows")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error validating {file_path}: {e}")
        return False


def validate_parquet_data(file_path: str) -> bool:
    """Validate Parquet data file"""
    try:
        df = pd.read_parquet(file_path)
        
        print(f"📊 Validating {file_path}")
        print(f"   Shape: {df.shape}")
        print(f"   Columns: {list(df.columns)}")
        print(f"   Data types: {df.dtypes.to_dict()}")
        
        # Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.any():
            print(f"   ⚠️  Missing values: {missing_values[missing_values > 0].to_dict()}")
        else:
            print(f"   ✅ No missing values")
        
        # Check for duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"   ⚠️  Duplicate rows: {duplicates}")
        else:
            print(f"   ✅ No duplicate rows")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error validating {file_path}: {e}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate data files")
    parser.add_argument(
        "--data-dir", 
        default="data",
        help="Directory containing data files (default: data)"
    )
    
    args = parser.parse_args()
    
    data_dir = Path(args.data_dir)
    
    if not data_dir.exists():
        print(f"❌ Data directory not found: {data_dir}")
        sys.exit(1)
    
    print("🔍 Validating data files...")
    print("=" * 50)
    
    all_valid = True
    
    # Validate CSV files
    csv_files = list(data_dir.glob("*.csv"))
    for csv_file in csv_files:
        if not validate_csv_data(str(csv_file)):
            all_valid = False
        print()
    
    # Validate Parquet files
    parquet_files = list(data_dir.glob("*.parquet"))
    for parquet_file in parquet_files:
        if not validate_parquet_data(str(parquet_file)):
            all_valid = False
        print()
    
    if all_valid:
        print("✅ All data files are valid!")
        sys.exit(0)
    else:
        print("❌ Some data files have issues!")
        sys.exit(1)


if __name__ == "__main__":
    main()
