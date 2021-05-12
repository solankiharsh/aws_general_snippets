import pandas as pd
import uuid
def write_parquet_file():
    df = pd.read_csv('/home/ubuntu/data_applicats_sample.csv')
    df.to_parquet(f'/home/ubuntu/s3_parquet_read/s3_csv_file_path_{uuid.uuid4()}.parquet')
write_parquet_file()
print('converted a csv to parquet')

