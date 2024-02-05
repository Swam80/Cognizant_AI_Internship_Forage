import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

from src.data_collection.data_collection import create_connection, load_sales_data, load_stock_levels, load_temperature_data
from src.data_preprocessing.data_preprocessing import preprocess_data



def transform_data(merged_df):
    # Split data into features and target variable
    X = merged_df.drop('estimated_stock_pct', axis=1)
    y = merged_df['estimated_stock_pct']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize StandardScaler and OneHotEncoder
    sc = StandardScaler()
    ohe = OneHotEncoder()

    # Get numerical and categorical columns
    num_col = [col for col in X.columns if X[col].dtype != 'O']
    cat_col = [col for col in X.columns if col not in num_col]

    # Define preprocessing transformer
    preprocessing_transformer = ColumnTransformer(
        transformers=[
            ('ohe', ohe, cat_col),
            ('standard_scaler', sc, num_col)
        ]
    )

    # Define pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessing_transformer)]) 
    


    # Transform training and test sets
    X_train_processed = pipeline.fit_transform(X_train).toarray()
    X_test_processed = pipeline.transform(X_test).toarray()

    # Saving the transformation pipeline in pkl file
    joblib.dump(pipeline,"transform_pipeline.pkl") #-------------------------------#


    # Get column names
    column_names = list(pipeline.named_steps['preprocessor'].named_transformers_['ohe'].get_feature_names_out(cat_col)) + list(num_col)

    # Convert arrays to dataframes
    X_train_processed = pd.DataFrame(X_train_processed, columns=column_names)
    X_test_processed = pd.DataFrame(X_test_processed, columns=column_names)



    return X_train_processed, X_test_processed, y_train, y_test

# if __name__ == "__main__":
#     connection_engine = create_connection()
#     df_sales = load_sales_data(connection_engine)
#     df_stock_levels = load_stock_levels(connection_engine)
#     df_temperature = load_temperature_data(connection_engine)
#     merged_df = preprocess_data(df_sales, df_stock_levels, df_temperature)

#     X_train_processed, X_test_processed, y_train, y_test = transform_data(merged_df)
#     print(X_train_processed)