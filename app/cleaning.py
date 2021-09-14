#import libraries
import pandas as pd

def select_column(df,input_data="name",labels="tag_id",date_time="publication_date"):
    df[['input_data','labels','date_time']]=df[[input_data,labels,date_time]]
    return df[['input_data','labels','date_time']]

#croping datetime:
def crop_data(df,starting_date=None,ending_date=None):
    df['date_time'] = df.date_time.apply(lambda a: pd.to_datetime(a).date())
    if (ending_date==None):
        start_date = pd.to_datetime(starting_date, utc=True)
        df = df.loc[(df['date_time'] > start_date)]
    elif (starting_date==None):
        end_date = pd.to_datetime(ending_date, utc=True)
        df = df.loc[(df['date_time'] < end_date)]
    else:
        start_date = pd.to_datetime(starting_date, utc=True)
        end_date = pd.to_datetime(ending_date, utc=True)
        df = df.loc[(df['date_time'] > start_date)]
        df = df.loc[(df['date_time'] < end_date)]

    return df

def select_labels(df,labels):
    # remove none tagged job offers
    df.dropna(subset=['labels'], inplace=True)
    df.drop_duplicates(subset=['input_data'])
    df=df.loc[df['labels'].isin(list(labels))]
    return df


if __name__ == "__main__":

    LABELS = {27: 'Human Resources', 18: 'Customer Service', 23: 'Product', 19: 'Software Development',
              30: 'Sales', 32: 'Writing', 33: 'Business', 24: 'Data', 28: 'Marketing', 25: 'DevOps/sysadmin',
              21: 'Design', 26: 'Finance/ Legal', 29: 'QA'}

    #import dataframe and select the columns needed
    df=select_column(df= pd.read_csv('../Data/job_export.csv'),
                     input_data="name",labels="tag_id",
                     date_time="publication_date")

    #crop data if needed according to timeline
    df=crop_data(df,starting_date='2020-12-30')

    #drop the categories that we dont need and the NAN
    df=select_labels(df,labels=LABELS)

    df.to_csv('../Data/data_cleaned.csv', index=False)