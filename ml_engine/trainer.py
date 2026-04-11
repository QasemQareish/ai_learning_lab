from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

def get_model(algorithm, problem_type):
    """Get ML model with proper configurations"""
    models = {
        ('linear_regression', 'regression'): LinearRegression(),
        ('logistic_regression', 'classification'): LogisticRegression(
            max_iter=1000, 
            solver='lbfgs',
            random_state=42
        ),
        ('decision_tree', 'classification'): DecisionTreeClassifier(random_state=42),
        ('decision_tree', 'regression'): DecisionTreeRegressor(random_state=42),
        ('knn', 'classification'): KNeighborsClassifier(n_neighbors=5),
        ('knn', 'regression'): KNeighborsRegressor(n_neighbors=5),
    }
    return models.get((algorithm, problem_type))

def train(X_train, y_train, algorithm, problem_type):
    """Train model with proper configurations"""
    model = get_model(algorithm, problem_type)
    if model is None:
        raise ValueError(f"No model found for {algorithm} + {problem_type}")
    model.fit(X_train, y_train)
    return model