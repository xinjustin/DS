# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:32:28 2018

@author: justinxin
"""


'''group by key columns to create the frequency distribution as features '''
'''https://www.kaggle.com/nanomathias/feature-engineering-importance-testing'''

'''There are a lot of groupby -> count()/var()/mean() etc. feature engineering in the kernels I've checked out, so of course those have to be added as well :)'''






''' time until '''

'''Time till next click
It might be interesting to know e.g. how long it takes for a given ip-app-channel before they perform the next click. So I'll create some features for these as well. **'''

'''https://www.kaggle.com/nanomathias/feature-engineering-importance-testing'''


GROUP_BY_NEXT_CLICKS = [
    
    # V1
    {'groupby': ['ip']},
    {'groupby': ['ip', 'app']},
    {'groupby': ['ip', 'channel']},
    {'groupby': ['ip', 'os']},
    
    # V3
    {'groupby': ['ip', 'app', 'device', 'os', 'channel']},
    {'groupby': ['ip', 'os', 'device']},
    {'groupby': ['ip', 'os', 'device', 'app']}
]

# Calculate the time to next click for each group
for spec in GROUP_BY_NEXT_CLICKS:
    
    # Name of new feature
    new_feature = '{}_nextClick'.format('_'.join(spec['groupby']))    
    
    # Unique list of features to select
    all_features = spec['groupby'] + ['click_time']
    
    # Run calculation
    print(f">> Grouping by {spec['groupby']}, and saving time to next click in: {new_feature}")
    X_train[new_feature] = X_train[all_features].groupby(spec['groupby']).click_time.transform(lambda x: x.diff().shift(-1)).dt.seconds
    
X_train.head()


