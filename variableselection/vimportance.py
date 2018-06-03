# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 23:06:30 2018

@author: justinxin
"""

''' feature importance '''


feat_importance_et=pd.DataFrame(list(zip(x_train.columns.values,et.clf.feature_importances_)),columns=['feature','importance'])
feat_importance_et.sort_values(by=['importance'],ascending=False,inplace=True)



'''The feature importances are MinMax scaled, put into a DataFrame, and finally plotted ordered by the mean feature importance.'''
'''standardize feature importance '''

'''https://www.kaggle.com/nanomathias/feature-engineering-importance-testing'''

from sklearn import preprocessing

# Get xgBoost importances
importance_dict = {}
for import_type in ['weight', 'gain', 'cover']:
    importance_dict['xgBoost-'+import_type] = clf_xgBoost.get_booster().get_score(importance_type=import_type)
    
# MinMax scale all importances
importance_df = pd.DataFrame(importance_dict).fillna(0)
importance_df = pd.DataFrame(
    preprocessing.MinMaxScaler().fit_transform(importance_df),
    columns=importance_df.columns,
    index=importance_df.index
)

# Create mean column
importance_df['mean'] = importance_df.mean(axis=1)

# Plot the feature importances
importance_df.sort_values('mean').plot(kind='bar', figsize=(20, 7))