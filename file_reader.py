import attr
import pandas as pd
import numpy as np
from base import MainReader
from file_schema import file_schema

@attr.s
class FileReader(MainReader):
    file_name = attr.ib(default='input')
    file_path = attr.ib(default='input.csv')
    validation_schema = attr.ib(default=file_schema)

    def process_file(self):
        data = self.df.copy()
        
        data = (data
        .fillna({'division_name': 'Not_Known',
               'department_name': 'Not_Known',
               'class_name': 'Not_Known'})
       .rename(columns={'recommend_index ': 'recommend_index'})
       .assign(age_group=lambda x: pd.cut(data['age'], 
                                        bins=(0,19,29,39,49,59,69,100), 
                                        labels=['Teen', '20-29', '30-39', '40-49', '50-59', '60-69', 'Above 70'])
        ))

        return data
