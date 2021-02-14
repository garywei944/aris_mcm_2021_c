import pandas as pd
import numpy as np

import os
import datetime

TODAY = datetime.date(2020, 1, 1)


def diff_from_origin_date(d):
    if d == 0:
        return 0
    d = pd.Timestamp(d).to_pydatetime().date()
    return (d - TODAY).days


def preprocess(df):
    df['Lab Status'] = df['Lab Status'].map({
        'Negative ID': 0,
        'Positive ID': 1,
        'Unverified': 2
    }).fillna(value=2)

    df['Detection Date'] = pd.to_datetime(df['Detection Date'], errors='coerce')
    df['Submission Date'] = pd.to_datetime(df['Submission Date'], errors='coerce')
    df = df.fillna(0)
    df['Detection Date'] = np.vectorize(diff_from_origin_date)(df['Detection Date'])
    df['Submission Date'] = np.vectorize(diff_from_origin_date)(df['Submission Date'])
    return df


def get_file_name(files):
    return os.path.splitext(files)[0]


def load_and_process():
    data = pd.read_excel('2021_MCM_Problem_C_Data/2021MCMProblemC_DataSet.xlsx', index_col=0)
    image_id = pd.read_excel('2021_MCM_Problem_C_Data/2021MCM_ProblemC_ Images_by_GlobalID.xlsx', index_col=1)

    data = preprocess(data)
    image_id = image_id.iloc[:, :-1]
    image_id['FileName'] = np.vectorize(get_file_name)(image_id['FileName'])

    return data, image_id
