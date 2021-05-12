import s3fs
import pyarrow.parquet as pq
fs = s3fs.S3FileSystem()

bucket = 'my-aws-ccp-demo-bucket'
path = 'data/converted.parquet' #if its a directory omit the traling /
bucket_uri = f's3://{bucket}/{path}'
print(bucket_uri)
#'s3://your-bucket-name/directory_name'

dataset = pq.ParquetDataset(bucket_uri, filesystem=fs)
table = dataset.read()
df = table.to_pandas() 
print(df)
