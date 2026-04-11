import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

def load_dataset(file_path):
    return pd.read_csv(file_path)

def get_column_info(df):
    columns = []
    for col in df.columns:
        col_type = 'numeric' if pd.api.types.is_numeric_dtype(df[col]) else 'categorical'
        columns.append({
            'name': col,
            'type': col_type,
            'missing': int(df[col].isnull().sum())
        })
    return columns

def preprocess(df, target_column, test_size=0.2, random_state=42, scale_features=False):
    """
    Preprocess the dataset for ML training.
    
    Args:
        df: pandas DataFrame
        target_column: name of target column
        test_size: float between 0 and 1
        random_state: int or None (None for randomization)
        scale_features: bool (True for KNN and Logistic Regression)
    
    Returns:
        X_train, X_test, y_train, y_test, encoders, scaler, feature_names
    """
    df = df.copy()
    
    # Handle missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')
    
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Store original feature names before encoding
    original_features = X.columns.tolist()
    
    # Encode target if categorical (for classification)
    target_encoder = None
    if not pd.api.types.is_numeric_dtype(y):
        target_encoder = LabelEncoder()
        y = target_encoder.fit_transform(y.astype(str))
    
    # One-Hot Encode categorical features (NOT LabelEncoder)
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    
    if categorical_cols:
        X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Get final feature names after encoding
    feature_names = X.columns.tolist()
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Feature Scaling (only if needed)
    scaler = None
    if scale_features:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    
    encoders = {
        'target_encoder': target_encoder,
        'categorical_cols': categorical_cols,
        'original_features': original_features
    }
    
    return X_train, X_test, y_train, y_test, encoders, scaler, feature_names