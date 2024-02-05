
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

from src.data_collection.data_collection import create_connection, load_sales_data, load_stock_levels, load_temperature_data
from src.data_collection.data_collection import create_connection, load_sales_data, load_stock_levels, load_temperature_data
from src.data_preprocessing.data_preprocessing import preprocess_data
from src.data_transformation.data_transformation import transform_data

def evaluate_model(model, X_train, X_test, y_train, y_test):

    """
    Evaluate the model by calculating performance metrics using the training and test sets.

    Parameters:
    model (sklearn.ensemble.RandomForestRegressor): The final model.
    X_train (pd.DataFrame): The training set.
    X_test (pd.DataFrame): The test set.
    y_train (pd.Series): The target variable for the training set.
    y_test (pd.Series): The target variable for the test set.

    Returns:
    pd.DataFrame, np.ndarray: The evaluation report and the predicted values.
    """
    # Your evaluation code here
    metrics = ['RMSE', 'MAE', 'R2']
    report = pd.DataFrame(index=[type(model).__name__], columns=metrics)
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_test_pred, squared=False)
    mae = mean_absolute_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)
    report.loc[type(model).__name__] = [rmse, mae, r2]
    return report



# if __name__ == "__main__":
#     connection_engine = create_connection()
#     df_sales = load_sales_data(connection_engine)
#     df_stock_levels = load_stock_levels(connection_engine)
#     df_temperature = load_temperature_data(connection_engine)
#     merged_df = preprocess_data(df_sales, df_stock_levels, df_temperature)

#     X_train, X_test, y_train, y_test = transform_data(merged_df)

#     final_model = train_final_model(final_model, X_train, y_train)

#     report = evaluate_model(final_model, X_train, X_test, y_train, y_test)

#     print(report)



