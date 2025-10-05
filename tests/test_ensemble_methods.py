"""
Tests for ensemble learning methods
"""

import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import xgboost as xgb
from typing import Tuple


class TestRandomForest:
    """Test Random Forest ensemble methods"""
    
    def test_random_forest_classifier(self, sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test Random Forest classifier"""
        X, y = sample_classification_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        rf = RandomForestClassifier(n_estimators=10, random_state=42)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        assert accuracy > 0.5  # Should perform better than random
        
    def test_random_forest_regressor(self, sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test Random Forest regressor"""
        X, y = sample_regression_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        rf = RandomForestRegressor(n_estimators=10, random_state=42)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        assert mse < np.var(y_test)  # Should perform better than baseline


class TestAdaBoost:
    """Test AdaBoost ensemble methods"""
    
    def test_adaboost_classifier(self, sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test AdaBoost classifier"""
        X, y = sample_classification_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        ada = AdaBoostClassifier(n_estimators=10, random_state=42)
        ada.fit(X_train, y_train)
        y_pred = ada.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        assert accuracy > 0.5  # Should perform better than random
        
    def test_adaboost_regressor(self, sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test AdaBoost regressor"""
        X, y = sample_regression_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        ada = AdaBoostRegressor(n_estimators=10, random_state=42)
        ada.fit(X_train, y_train)
        y_pred = ada.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        assert mse < np.var(y_test)  # Should perform better than baseline


class TestGradientBoosting:
    """Test Gradient Boosting ensemble methods"""
    
    def test_gradient_boosting_classifier(self, sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test Gradient Boosting classifier"""
        X, y = sample_classification_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        gb = GradientBoostingClassifier(n_estimators=10, random_state=42)
        gb.fit(X_train, y_train)
        y_pred = gb.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        assert accuracy > 0.5  # Should perform better than random
        
    def test_gradient_boosting_regressor(self, sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test Gradient Boosting regressor"""
        X, y = sample_regression_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        gb = GradientBoostingRegressor(n_estimators=10, random_state=42)
        gb.fit(X_train, y_train)
        y_pred = gb.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        assert mse < np.var(y_test)  # Should perform better than baseline


class TestXGBoost:
    """Test XGBoost ensemble methods"""
    
    def test_xgboost_classifier(self, sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test XGBoost classifier"""
        X, y = sample_classification_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        xgb_clf = xgb.XGBClassifier(n_estimators=10, random_state=42)
        xgb_clf.fit(X_train, y_train)
        y_pred = xgb_clf.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        assert accuracy > 0.5  # Should perform better than random
        
    def test_xgboost_regressor(self, sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test XGBoost regressor"""
        X, y = sample_regression_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        xgb_reg = xgb.XGBRegressor(n_estimators=10, random_state=42)
        xgb_reg.fit(X_train, y_train)
        y_pred = xgb_reg.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        assert mse < np.var(y_test)  # Should perform better than baseline


class TestEnsembleComparison:
    """Test ensemble method comparisons"""
    
    def test_ensemble_vs_single_model_classification(self, sample_classification_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test that ensemble performs better than single model for classification"""
        X, y = sample_classification_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Single decision tree
        from sklearn.tree import DecisionTreeClassifier
        single_tree = DecisionTreeClassifier(random_state=42)
        single_tree.fit(X_train, y_train)
        single_pred = single_tree.predict(X_test)
        single_accuracy = accuracy_score(y_test, single_pred)
        
        # Random Forest (ensemble)
        rf = RandomForestClassifier(n_estimators=10, random_state=42)
        rf.fit(X_train, y_train)
        ensemble_pred = rf.predict(X_test)
        ensemble_accuracy = accuracy_score(y_test, ensemble_pred)
        
        # Ensemble should perform at least as well as single model
        assert ensemble_accuracy >= single_accuracy * 0.9  # Allow some tolerance
        
    def test_ensemble_vs_single_model_regression(self, sample_regression_data: Tuple[np.ndarray, np.ndarray]) -> None:
        """Test that ensemble performs better than single model for regression"""
        X, y = sample_regression_data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Single decision tree
        from sklearn.tree import DecisionTreeRegressor
        single_tree = DecisionTreeRegressor(random_state=42)
        single_tree.fit(X_train, y_train)
        single_pred = single_tree.predict(X_test)
        single_mse = mean_squared_error(y_test, single_pred)
        
        # Random Forest (ensemble)
        rf = RandomForestRegressor(n_estimators=10, random_state=42)
        rf.fit(X_train, y_train)
        ensemble_pred = rf.predict(X_test)
        ensemble_mse = mean_squared_error(y_test, ensemble_pred)
        
        # Ensemble should perform at least as well as single model
        assert ensemble_mse <= single_mse * 1.1  # Allow some tolerance
