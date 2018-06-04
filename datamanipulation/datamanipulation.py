# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:45:19 2018

@author: justinxin
"""

'''extract hour day weekday of a datatime column'''
train_df['hour'] = pd.to_datetime(train_df.click_time).dt.hour.astype('uint8')
train_df['day'] = pd.to_datetime(train_df.click_time).dt.day.astype('uint8')
train_df['wday']  = pd.to_datetime(train_df.click_time).dt.dayofweek.astype('uint8')

#extract hour as a feature

'''https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns'''
train_smp['click_hour']=train_smp['click_time'].dt.hour

#set click_time and attributed_time as timeseries
'''https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns'''
train['click_time'] = pd.to_datetime(train['click_time'])
train['attributed_time'] = pd.to_datetime(train['attributed_time'])
test['click_time'] = pd.to_datetime(test['click_time'])

#set as_attributed in train as a categorical

'''https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns'''
train['is_attributed']=train['is_attributed'].astype('category')

#round the time to nearest hour

'''https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns'''
train_smp['click_rnd']=train_smp['click_time'].dt.round('H')  


#check for hourly patterns
train_smp[['click_rnd','is_attributed']].groupby(['click_rnd'], as_index=True).count().plot()
plt.title('HOURLY CLICK FREQUENCY');
plt.ylabel('Number of Clicks');

''' group by reset index to create a summary matrix '''
gp = train_df[['ip','day','hour','channel']].groupby(by=['ip','day','hour'])[['channel']].count().reset_index().rename(index=str, columns={'channel': 'qty'})


''' set low cardinality numeric variables as categorical '''
'''https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns'''
variables = ['ip', 'app', 'device', 'os', 'channel']
for v in variables:
    train[v] = train[v].astype('category')
    test[v]=test[v].astype('category')
    
    
'''calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher, 
        Journal of the Korean Statistical Society 42 (2013): 323-328'''
#https://stackoverflow.com/questions/20892799/using-pandas-calculate-cram%C3%A9rs-coefficient-matrix/39266194
def cramers_corrected_stat(confusion_matrix):
    """ calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher, 
        Journal of the Korean Statistical Society 42 (2013): 323-328
    """
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))