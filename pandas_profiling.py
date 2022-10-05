# Pandas Profiling package can generate report of any data
# in just a few minutes(according to the dataset size)
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('Colon.csv', engine='python')
# taking the last 10 columns only
cols = df.columns[0:1990]
df.drop(cols, axis=1, inplace=True)
df

# Generating Report as an HTML File

ProfileReport(df).to_file(output_file="colonAnalysis.html")
