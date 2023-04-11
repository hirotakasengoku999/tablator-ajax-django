import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, Boolean, MetaData, DateTime, update

def readcsv(file):
    usecols = ['カルテ番号等',
        '氏名',
        '_date',
        '診療科名',
        '算定項目名称',
        '算定漏れ確率',
        '算定実績',
        '算定漏れ根拠_1',
        '算定漏れ根拠_2',
        '算定漏れ根拠_3',
        '算定漏れ根拠_4',
        '算定漏れ根拠_5']
    df = pd.read_csv(file, engine='python', encoding='cp932', usecols=usecols, dtype={'カルテ番号等':'object'})
    return(df)

def main(in_dir):
    l = []
    for file in in_dir.glob('**/*.csv'):
        l.append(readcsv(file))
    df = pd.concat(l)
    rename_dict = {'カルテ番号等': 'PATIENT_ID', '氏名': 'PATIENT_NAME', '_date': 'MEDICALCARE_DATE', '診療科名': 'DEPT', '算定項目名称': 'ITEM_NAME',
     '算定漏れ確率': 'PREDICT_PROBA', '算定実績': 'CALCULATION_BOOL', '算定漏れ根拠_1':'BASIS_1', '算定漏れ根拠_2':'BASIS_2','算定漏れ根拠_3':'BASIS_3',
    '算定漏れ根拠_4':'BASIS_4','算定漏れ根拠_5':'BASIS_5'}
    df = df.rename(columns = rename_dict)
    df['USER_CHECK'] = '未'
    df['NOTE'] = ''
    df['PATIENT_ID'] = df['PATIENT_ID'].str.zfill(8)
    con = create_engine('mysql://root:administrator@127.0.0.1/ajaxdb?charset=utf8')
    df.to_sql('post_result', con=con, if_exists='append', index=None)

def get_results(request_sql):
    con = create_engine('mysql://root:administrator@127.0.0.1/ajaxdb?charset=utf8')
    return pd.read_sql(request_sql, con)

def update_results(primary_key, value_list):
    con = create_engine('mysql://root:administrator@127.0.0.1/ajaxdb?charset=utf8')
    metadata = MetaData()

    result = Table('post_result', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('USER_CHECK', String),
                  Column('PATIENT_ID', String),
                  Column('PATIENT_NAME', String),
                  Column('MEDICALCARE_DATE', String),
                  Column('DEPT', String),
                  Column('ITEM_NAME', String),
                  Column('PREDICT_PROBA', Float),
                  Column('CALCULATION_BOOL', Boolean),
                  Column('BASIS_1', String),
                  Column('BASIS_2', String),
                  Column('BASIS_3', String),
                  Column('BASIS_4', String),
                  Column('BASIS_5', String),
                  Column('NOTE', String),
                  )
    if value_list[0] == 'USER_CHECK':
        stmt = result.update().where(result.c.id == primary_key).values(USER_CHECK=value_list[1])
    elif value_list[0] == 'NOTE':
        stmt = result.update().where(result.c.id == primary_key).values(NOTE=value_list[1])
    with con.connect() as conn:
        conn.execute(stmt)

if __name__ == '__main__':
    # in_dir = Path(r'C:\Users\user\work\aireceipt\iseikai\data_\patientname_conversion\result\iseikai')
    # main(in_dir)
    request_sql = "SELECT * FROM post_result"
    df = get_results(request_sql)
    print(df)