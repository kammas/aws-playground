## Architecture
![image](data_analytics_1.png)

## Deploying the full infrastructure via CLI 
```shell
aws configure --profile cloudguru
aws configure list --profile cloudguru
aws s3 ls --profile cloudguru
```

## Create Main Stack
```shell
PROFILE=cloudguru
STACKNAME=mystack02
REGION=us-east-1
aws cloudformation create-stack \
  --stack-name $STACKNAME \
  --template-body file://./template.yaml \
  --stack-policy-body file://./stack-policy.json \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
  --region $REGION \
  --profile $PROFILE
```

## Deploy Main Stack changes.
```shell
PROFILE=cloudguru
STACKNAME=mystack02
REGION=us-east-1
aws cloudformation deploy \
  --stack-name $STACKNAME \
  --template-file test.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --region $REGION \
  --profile $PROFILE
```

**CLI commands used:**

--upload file to s3
aws s3 cp cli.txt s3://mystack02-pkbucketpbs31-1x7od7ysm5qe9 --profile $PROFILE

--move file to s3
aws s3 mv movemeCLI.txt s3://mystack02-pkbucketpbs31-1x7od7ysm5qe9 --profile $PROFILE

--sync from local to S3
aws s3 sync . s3://mystack02-pkbucketpbs31-1x7od7ysm5qe9 --profile $PROFILE

--upload file using boto3
python3 boto3actions.py

--upload file using multipartupload using boto3
--creating a sample file first
dd if=/dev/urandom of=file.txt bs=1048576 count=100
python3 multipartupload.py -f file.txt -b mystack02-pkbucketpbs31-1x7od7ysm5qe9 -cs 20

--apply a lifecycle policy for logs/ moving data to IA after 30 days, Deep Archive after 120 days and Delete data after 2555 days
aws s3api put-bucket-lifecycle-configuration --bucket mystack02-pkbucketpbs31-1x7od7ysm5qe9 --lifecycle-configuration file://ArchivePolicy.json --profile $PROFILE