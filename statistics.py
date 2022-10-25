# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : YuDong Wang 
# Created Date: 25/07/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" 
Package for the statistics and hypothesis test
"""  

import pandas as pd

def check_clinical_data_type(df, categorical_max_num=10):
    data_types = {'numerical_discrete':[], 'numerical_continuous':[], 'categorical_ordinal':[], 'categorical_norminal':[],'pid':[]}
    max_num = min([categorical_max_num, len(df)//10])
    for col_name, col in df.iteritems():
        count = len(col.value_counts())
        if col.dtype == 'O':
            if count <= 2:
                data_types['categorical_norminal'].append(col_name)
            elif count <= 10:
                data_types['categorical_ordinal'].append(col_name)
        elif col.dtype == 'int64':
            if count == len(df):
                data_types['pid'].append(col_name)
            elif count <= 2:
                data_types['categorical_norminal'].append(col_name)
            elif count <= max_num:
                data_types['numerical_discrete'].append(col_name)
            else:
                data_types['numerical_continuous'].append(col_name)
        else:
            data_types['numerical_continuous'].append(col_name)
    return data_types
