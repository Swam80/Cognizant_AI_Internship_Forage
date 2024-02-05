import pandas as pd
import numpy as np
import joblib

from src.data_collection.data_collection import create_connection, load_sales_data, load_stock_levels, load_temperature_data
from src.data_preprocessing.data_preprocessing import preprocess_data
from src.data_transformation.data_transformation import transform_data
from src.model_evaluation.evaluation import  evaluate_model


def main():
    # Load data
    connection_engine = create_connection()

    df_sales = load_sales_data(connection_engine)

    df_stock_levels = load_stock_levels(connection_engine)

    df_temperature = load_temperature_data(connection_engine)

    # Preprocess data
    merged_df = preprocess_data(df_sales, df_stock_levels, df_temperature)

    # Transform data
    X_train, X_test, y_train, y_test = transform_data(merged_df)

    # Loading pkl files

    final_model = joblib.load('final_model.pkl')

    # Evaluate final model
    report = evaluate_model(final_model, X_train, X_test, y_train, y_test)
    print(report)


if __name__ == "__main__":
    main()

