from file_reader import FileReader

class FileCleansing:
    FileReaderObj = FileReader()
    output = FileReaderObj.process()
    
    output.to_csv(path_or_buf = 'output.csv', index=False)