import time

import pandas as pd
import sqlalchemy
import sqlalchemy.types
from sqlalchemy import Text


class ReadWrite:
    def __init__(self):
        self.file = '/home/lovkesh/Downloads/cd_excel.xlsx'
        self.engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/learning')

        # read sql
        dff = pd.read_sql("test", self.engine, columns=['Name_of_the_University', 'Short_Name'])
        # print(dff)

        # read excel
        self.df = pd.read_excel(self.file)

        self.df.rename(columns={
            'Name': 'Name_of_the_University',
            'Short Name': 'Short_Name',
            'Establishment Year': 'Establishment_Year'
        }, inplace=True)

    # read file
    def read(self):
        data = self.df[self.df['Name_of_the_University'].apply(lambda x: isinstance(x, str))]

        print(data)
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))

    def update(self):
        string = self.df[self.df['Name_of_the_University'].apply(lambda x: isinstance(x, int))]
        # string = self.df[pd.to_numeric(self.df.Name_of_the_University, errors='coerce').notnull()]
        print(string)
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    Rd = ReadWrite()

    Rd.update()
