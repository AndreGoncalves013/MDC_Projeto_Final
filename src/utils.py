import numpy as np
import pandas as pd

# Função que filtra os elementos de um dataframe se ele é treino, validação ou teste
def get_features_target_data(df_original, indexes_path):

    df = df_original.copy()
    indexes = pd.read_csv(indexes_path)

    df['filename'] = df.filename.apply(lambda x: x.replace('.', '')[:-3])
    indexes['filename'] = indexes.filename.apply(lambda x: x.replace('.', '')[:-3])

    filtered_df = df.set_index('filename').join(indexes[['filename']].set_index('filename'), how = 'inner').reset_index()

    X = filtered_df.drop(columns= 'label')
    y = filtered_df['label']

    return X, y

# Função que imprime os shapes dos conjuntos de X e y
def print_shape(X, y, label):
    print(f'-- {label} --')
    print('X (shape): ', X.shape)
    print('y: ', len(y))

# Função que retorna os conjuntos de dados de treino, validação e teste dos arquivos CSV gerados pelo notebook data_split.ipynb
def get_train_val_set_data(df_original):

    X_train, y_train = get_features_target_data(df_original, '../dataset/Data/train_indexes.csv')
    print_shape(X_train, y_train, 'Treino')

    X_val, y_val = get_features_target_data(df_original, '../dataset/Data/val_indexes.csv')
    print_shape(X_val, y_val, 'Validação')
    
    X_test, y_test = get_features_target_data(df_original, '../dataset/Data/test_indexes.csv')
    print_shape(X_test, y_test, 'Teste')

    return X_train, y_train, X_val, y_val, X_test, y_test