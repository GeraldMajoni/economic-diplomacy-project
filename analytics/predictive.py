import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import mlflow
import mlflow.sklearn
from datetime import datetime

# Set the MLflow tracking URI to your running MLflow server
mlflow.set_tracking_uri('http://localhost:5000')

def train_inflation_model(df):
    # Features and target for predicting USD YoY Inflation
    X = df[['central_bank_rate', 'reserve_money', 'broad_money_m3', 'official_exchange_rate', 'parallel_exchange_rate']]
    y = df['usd_yoy_inflation']
    
    # Create a pipeline with scaling and XGBRegressor
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('xgb', XGBRegressor(objective='reg:squarederror', random_state=42))
    ])
    
    # Define hyperparameter grid for tuning
    param_grid = {
        'xgb__n_estimators': [50, 100, 150],
        'xgb__max_depth': [3, 5, 7],
        'xgb__learning_rate': [0.01, 0.1, 0.2],
    }
    
    with mlflow.start_run():
        grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='neg_mean_absolute_error', verbose=1)
        grid_search.fit(X, y)
        best_model = grid_search.best_estimator_
        predictions = best_model.predict(X)
        mae = mean_absolute_error(y, predictions)
        mse = mean_squared_error(y, predictions)
        
        # Log parameters and metrics to MLflow
        mlflow.log_params(grid_search.best_params_)
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("MSE", mse)
        
        # Save the best model with a timestamp in the filename
        model_path = save_model(best_model, "analytics/models/best_inflation_model")
        mlflow.log_artifact(model_path)
        
        return best_model, grid_search.best_params_, mae, mse

def train_exchange_rate_model(df):
    # Features and target for predicting Official Exchange Rate
    X = df[['broad_money_m3', 'reserve_money', 'monthly_trade_balance', 'zwg_mom_inflation', 'usd_yoy_inflation']]
    y = df['official_exchange_rate']
    
    # Create a pipeline with scaling and ElasticNet regression
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('elastic', ElasticNet(random_state=42))
    ])
    
    # Define hyperparameter grid for ElasticNet
    param_grid = {
        'elastic__alpha': [0.1, 1.0, 10.0],
        'elastic__l1_ratio': [0.1, 0.5, 0.9],
    }
    
    with mlflow.start_run():
        grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='neg_mean_absolute_error', verbose=1)
        grid_search.fit(X, y)
        best_model = grid_search.best_estimator_
        predictions = best_model.predict(X)
        mae = mean_absolute_error(y, predictions)
        mse = mean_squared_error(y, predictions)
        
        mlflow.log_params(grid_search.best_params_)
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("MSE", mse)
        
        # Save the best model with a timestamp in the filename
        model_path = save_model(best_model, "analytics/models/best_exchange_rate_model")
        mlflow.log_artifact(model_path)
        
        return best_model, grid_search.best_params_, mae, mse

def save_model(model, filename_prefix):
    """
    Save the model with a filename that includes a timestamp.
    Returns the full path to the saved model.
    """
    import os
    # Generate a timestamp string, e.g., 20250211_193045
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Create a filename using the prefix and timestamp
    filename = f"{filename_prefix}_{timestamp}.joblib"
    # Ensure the directory exists
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Save the model
    joblib.dump(model, filename)
    return filename
