from sklearn.metrics import (
    accuracy_score,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)
import numpy as np

def evaluate(model, X_test, y_test, problem_type):
    y_pred = model.predict(X_test)
    result = {}

    if problem_type == 'classification':
        result['accuracy'] = round(accuracy_score(y_test, y_pred) * 100, 2)
        
        cm = confusion_matrix(y_test, y_pred)
        result['confusion_matrix'] = cm.tolist()
        
        report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
        result['classification_report'] = report
        
        result['predictions'] = y_pred.tolist()
        result['actual'] = y_test.tolist()

    elif problem_type == 'regression':
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        result['mse'] = round(mse, 4)
        result['mae'] = round(mae, 4)
        result['rmse'] = round(np.sqrt(mse), 4)
        result['r2'] = round(r2_score(y_test, y_pred), 4)
        
        result['predictions'] = [round(p, 2) for p in y_pred.tolist()]
        result['actual'] = y_test.tolist()

    return result