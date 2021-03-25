import boto3

# Initialize interfaces
boto3.setup_default_session(profile_name='cloudguru')
s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')

#TODO - change bucket name
bucket = 'mystack02-pkbucketpbs31-1x7od7ysm5qe9'


# Create byte string to send to our bucket
putMessage = b'Hi! I came from Boto3!'

# put_object
response = s3Client.put_object(
    Body = putMessage,
    Bucket = bucket,
    Key = 'boto3put.txt'
)

print(response)

# copy
toCopy = {
    'Bucket': bucket,
    'Key': 'boto3put.txt'
}

s3Resource.meta.client.copy(toCopy, bucket, 'boto3copy.txt')

# copy_object
response = s3Client.copy_object(
    Bucket = bucket,
    CopySource = '/'+bucket+'/boto3put.txt',
    Key = 'boto3copyobject.txt'
)

print(response)

# upload_file
boto3Upload = 'boto3upload.txt'

s3Resource.meta.client.upload_file(boto3Upload, bucket, boto3Upload)

# upload_fileobj
with open(boto3Upload, 'rb') as fileObj:
    response = s3Client.upload_fileobj(fileObj, bucket, 'boto3uploadobj.txt')
    print(response)

'''
response = s3Client.put_bucket_accelerate_configuration(
    Bucket=bucket,
    AccelerateConfiguration={
        'Status': 'Enabled'
    }
)

print(response)
'''