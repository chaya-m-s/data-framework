import attr
import pandas as pd
from abc import abstractmethod
import logging

log = logging.getLogger(__name__)

@attr.s
class MainReader:
    format = attr.ib(default='csv')
    file_name = attr.ib(default=None)
    file_path =  attr.ib(default=None)
    df =  attr.ib(default=pd.DataFrame())
    validation_schema = attr.ib(default=None)

    @abstractmethod
    def process_file(self):
        pass

    def load(self, format='csv'):
        if format != 'csv':
            raise Exception(f'Currently not supporting {format} files. Please provide csv format')

        if self.file_path:
            data = pd.read_csv(self.file_path)
        else:
            raise FileNotFoundError('File not present')

        return data

    def validate(self):
        if self.validation_schema:
            try:
                self.validation_schema.validate(self.df)
            except Exception:
                log.warning('Validation failed, Check the file')
        else:
            log.info('File not validated: Validation schema not present')

    def process(self):
        self.df = self.load()
        self.validate()
        processed = self.process_file()
        return processed
