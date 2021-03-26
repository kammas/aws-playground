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