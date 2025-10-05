"""
Pytest configuration and fixtures
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Generator


@pytest.fixture
def sample_data() -> pd.DataFrame:
    """Create sample data for testing"""
    np.random.seed(42)
    n_samples = 100
    
    data = {
        'feature_1': np.random.normal(0, 1, n_samples),
        'feature_2': np.random.normal(0, 1, n_samples),
        'feature_3': np.random.normal(0, 1, n_samples),
        'target': np.random.randint(0, 2, n_samples)
    }
    
    return pd.DataFrame(data)


@pytest.fixture
def sample_classification_data() -> Tuple[np.ndarray, np.ndarray]:
    """Create sample classification data"""
    np.random.seed(42)
    n_samples = 200
    
    # Create two classes with different distributions
    class_0 = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], n_samples // 2)
    class_1 = np.random.multivariate_normal([2, 2], [[1, -0.5], [-0.5, 1]], n_samples // 2)
    
    X = np.vstack([class_0, class_1])
    y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)])
    
    return X, y


@pytest.fixture
def sample_regression_data() -> Tuple[np.ndarray, np.ndarray]:
    """Create sample regression data"""
    np.random.seed(42)
    n_samples = 100
    
    X = np.random.normal(0, 1, (n_samples, 3))
    y = 2 * X[:, 0] + 3 * X[:, 1] - X[:, 2] + np.random.normal(0, 0.1, n_samples)
    
    return X, y


@pytest.fixture
def data_dir() -> Path:
    """Get the data directory path"""
    return Path(__file__).parent.parent / "data"


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for testing"""
    return tmp_path
