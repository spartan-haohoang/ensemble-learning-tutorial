"""
Tests for data validation functionality
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple


def test_sample_data_structure(sample_data: pd.DataFrame) -> None:
    """Test that sample data has the expected structure"""
    assert isinstance(sample_data, pd.DataFrame)
    assert sample_data.shape[0] > 0
    assert 'target' in sample_data.columns
    assert len(sample_data.columns) >= 3


def test_sample_data_no_missing_values(sample_data: pd.DataFrame) -> None:
    """Test that sample data has no missing values"""
    assert not sample_data.isnull().any().any()


def test_sample_classification_data(sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
    """Test sample classification data"""
    X, y = sample_classification_data
    
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 2  # Two features
    assert len(np.unique(y)) == 2  # Binary classification
    assert X.shape[0] == 200  # Expected number of samples


def test_sample_regression_data(sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
    """Test sample regression data"""
    X, y = sample_regression_data
    
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 3  # Three features
    assert len(y.shape) == 1  # Single target variable
    assert X.shape[0] == 100  # Expected number of samples


def test_data_directory_exists(data_dir: Path) -> None:
    """Test that data directory exists"""
    assert data_dir.exists()
    assert data_dir.is_dir()


def test_data_files_exist(data_dir: Path) -> None:
    """Test that expected data files exist"""
    expected_files = ['adult.parquet', 'simple.csv']
    
    for file_name in expected_files:
        file_path = data_dir / file_name
        assert file_path.exists(), f"Expected file {file_name} not found"


def test_csv_data_loading(data_dir: Path) -> None:
    """Test loading CSV data"""
    csv_file = data_dir / 'simple.csv'
    if csv_file.exists():
        df = pd.read_csv(csv_file)
        assert isinstance(df, pd.DataFrame)
        assert df.shape[0] > 0


def test_parquet_data_loading(data_dir: Path) -> None:
    """Test loading Parquet data"""
    parquet_file = data_dir / 'adult.parquet'
    if parquet_file.exists():
        df = pd.read_parquet(parquet_file)
        assert isinstance(df, pd.DataFrame)
        assert df.shape[0] > 0


def test_data_quality_checks(sample_data: pd.DataFrame) -> None:
    """Test data quality checks"""
    # Test for duplicates
    assert sample_data.duplicated().sum() == 0
    
    # Test for infinite values
    assert not np.isinf(sample_data.select_dtypes(include=[np.number])).any().any()
    
    # Test data types
    assert sample_data.dtypes.apply(lambda x: x.name).notna().all()
