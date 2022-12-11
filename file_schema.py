from pandera import DataFrameSchema, Column, Check

file_schema = DataFrameSchema( columns={
    'age': Column(int, Check(lambda x:  0 < x < 120, error='Invalid age')),
    'division_name': Column(str),
    'department_name': Column(str),
    'class_name': Column(str),
    'clothing_id': Column(int),
    'rating': Column(int),
    'recommend_index ': Column(int)

})