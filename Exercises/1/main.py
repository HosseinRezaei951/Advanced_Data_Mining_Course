import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

result_path = 'results/'
if os.path.isdir(result_path) == False:
    os.mkdir(result_path) 

### Q1:
data = pd.read_csv (r'data/data.csv')
print(data.info())
print("\nNumber of features(Columns): ", len(data.columns)-1)

### Q2:
sample_data = data.sample(frac = 0.8, replace=False)
sample_data = sample_data.sort_index()
print("\nSampling 80% of data: \n", sample_data)

### Q3:
for i in range(len(data.columns)-1, len(data.columns)-10, -1):
    column_name = str(data.columns[i])
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].title.set_text('Boxplot')
    axes[1].title.set_text('Histogram(by count) with KDE')
    fig.suptitle(column_name + ' (Original Vs Sample)')
    tmp_df = pd.DataFrame({'Original':data[column_name], 'Sample':sample_data[column_name]})
    sns.boxplot(data=tmp_df, width=0.2, linewidth=2.5, ax=axes[0])
    sns.histplot(data=tmp_df, kde=True, ax=axes[1])
    plt.tight_layout(pad=2)
    plt.savefig(result_path + column_name + ' (Original Vs Sample)' + ".jpeg")
    plt.close()

### Q4:
nRows, nCols = np.shape(sample_data)
for j in range(1, nCols):
    column_name = sample_data.columns[j]
    sample_data[column_name] = preprocessing.normalize([np.array(sample_data[column_name])])[0]

    # Create the Scaler object
    scaler = preprocessing.MinMaxScaler()
    sample_data[column_name] = scaler.fit_transform(sample_data[[column_name]]).T[0]*100
   
    sample_data = sample_data.sort_values(by=column_name)

    _min = math.floor(sample_data[column_name].min())
    _max = math.ceil(sample_data[column_name].max())
    
    _labels = list(range(_min, _max+1))
    _bins = len(_labels)
    
    cut_series, cut_intervals = pd.cut(sample_data[column_name], bins=_bins, labels=_labels, retbins=True)
  
    tmp_df = pd.DataFrame({'Original':sample_data[column_name], 'Discretized':list(cut_series)})
    
    ### plot result
    if j >= nCols-9:
        fig, axes = plt.subplots(nrows=1, ncols=2)
        sns.boxplot(data=tmp_df, width=0.2, linewidth=2.5, ax=axes[0])
        axes[0].title.set_text('Boxplot')
        axes[1].title.set_text('Histogram(by count) with KDE')
        fig.suptitle(column_name + ' (Original Vs Discretized)')
        sns.histplot(data=tmp_df, kde=True, ax=axes[1])
        plt.tight_layout(pad=2)
        plt.savefig(result_path + column_name + ' (Original Vs Discretized)' + ".jpeg")
        plt.close()
        
    sample_data[column_name] = list(cut_series)
  
sample_data = sample_data.sort_index()
print("\nDiscretizing sample_data: \n", sample_data)


### Q5:
sample_data.columns.values[0] = ''
sample_data.to_csv(result_path + 'data_disc.csv', index=False)

