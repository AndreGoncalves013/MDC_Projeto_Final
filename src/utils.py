import numpy as np
import pandas as pd

def get_features_target_data(df, indexes_path):

    indexes = pd.read_csv(indexes_path)

    filtered_df = df.set_index('filename').join(indexes[['filename']].set_index('filename'), how = 'inner').reset_index()

    X = filtered_df.drop(columns= 'label')
    y = filtered_df['label']

    return X, y

def get_train_val_set_data(df):

    X_train, y_train = get_features_target_data(df, '../dataset/Data/train_indexes.csv')
    X_val, y_val = get_features_target_data(df, '../dataset/Data/val_indexes.csv')
    X_test, y_test = get_features_target_data(df, '../dataset/Data/test_indexes.csv')

    return X_train, y_train, X_val, y_val, X_test, y_test