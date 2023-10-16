import boto3

s3_client = boto3.client('s3',
                         aws_access_key_id='****************',
                         aws_secret_access_key='*********************')

try:
    # Upload file to S3
    s3_client.upload_file('/Users/nikhilgudupalli/Desktop/prices_clean.csv','bigdata-practice-nikhilr7', 'prices_clean.csv')
    print(f"File '/Users/nikhilgudupalli/Desktop/prices_clean.csv' uploaded to 'bigdata-practice-nikhilr7' as 'prices_clean.csv'.")
except Exception as e:
    print(f"Error uploading file: {e}")
