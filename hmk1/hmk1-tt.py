import pandas as pd

# Q1 a)
def read_data(path):
    """
    input : filepath
    return: DataFrame
    """
    df = pd.read_csv(path)
    return df

path = 'train.csv'
df = read_data(path)
print(df)
#df.describe()