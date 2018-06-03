# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
%matplotlib inline
color = sns.color_palette()
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 200)
from sklearn.base import TransformerMixin
from scipy.stats import skew
import xgboost as xgb
from sklearn.cross_validation import KFold
import sklearn as sklearn
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
import gc





