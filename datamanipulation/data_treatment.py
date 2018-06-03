# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:46:35 2018

@author: justinxin
"""





''' identify feature column data types '''



''' removing low vairance features '''


low_variance=[x for x in nums_cat_columns  if comcast[x].std()==0]  
comcast.drop(columns=low_variance,inplace=True)




''' drop high missing rate columns '''


def find_missing(data):
    # number of missing values
    count_missing = data.isnull().sum().values
    # total records
    total = data.shape[0]
    # percentage of missing
    ratio_missing = count_missing/total
    # return a dataframe to show: feature name, # of missing and % of missing
    return pd.DataFrame(data={'missing_count':count_missing, 'missing_ratio':ratio_missing}, index=data.columns.values)
miss_feat_df=find_missing(comcast)
missing_features = miss_feat_df[miss_feat_df.missing_ratio > 0.80].index
comcast.drop(missing_features, axis=1, inplace=True)
comcast.shape



def missing_data(data):
    ''' variables ranked by missing rate'''
    '''https://www.kaggle.com/gpreda/home-credit-default-risk-extensive-eda'''
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])




''' missing imputation '''


class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.
        Columns of categorical columns are imputed with the most frequent value 
        in column.
        Other columns are imputed with mean of column.
        """
    def fit(self, X, y=None):
        self.fill = pd.Series([X[c].value_counts().index[0]
            if c in character_columns or c in nums_cat_columns else X[c].mean() for c in X],
            index=X.columns)
        return self
    def transform(self, X, y=None):
        return X.fillna(self.fill)

comcast = DataFrameImputer().fit_transform(comcast)



''' one hot encoding '''


categorical_columns=list(character_columns)+nums_cat_columns
dummy_columns=[x for x in categorical_columns if x in comcast.columns]

comcast=pd.get_dummies(comcast,columns=dummy_columns)



''' remove outlies'''

'''https://www.kaggle.com/gpreda/home-credit-default-risk-extensive-eda'''

def is_outlier(points, thresh=3.5):
    """
    Returns a boolean array with True if points are outliers and False 
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor. 
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh





