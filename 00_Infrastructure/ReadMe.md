### Deploying the full infrastructure via CLI 
aws configure --profile cloudguru
aws configure list --profile cloudguru
aws s3 ls --profile cloudguru

R53DOMAIN=test.cmcloudlab520.info
R53HOSTEDZONEID=Z07146542VPODC5DKZYB9


# Create Main Stack
```shell
PROFILE=cloudguru
STACKNAME=myinfrastructure
REGION=us-east-1
aws cloudformation create-stack \
  --stack-name $STACKNAME \
  --template-body file://./infrastructure_v5.yaml \
  --stack-policy-body file://./stack-policy.json \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
  --parameters ParameterKey=route53DomainName,ParameterValue=$R53DOMAIN ParameterKey=route53HostedZoneId,ParameterValue=$R53HOSTEDZONEID  \
  --region $REGION \
  --profile $PROFILE
```

# Deploy Main Stack changes
```shell
PROFILE=cloudguru
STACKNAME=mytestinfrastructure
REGION=us-east-1
aws cloudformation deploy \
  --stack-name $STACKNAME \
  --template-file infrastructure_v5.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides route53DomainName=$R53DOMAIN route53HostedZoneId=$R53HOSTEDZONEID \
  --region $REGION \
  --profile $PROFILE
```

# Create Test Stack
```shell
PROFILE=cloudguru
STACKNAME=mytestinfrastructure
REGION=us-east-1
aws cloudformation create-stack \
  --stack-name $STACKNAME \
  --template-body file://./Test.yaml \
  --stack-policy-body file://./stack-policy.json \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
  --parameters ParameterKey=param1,ParameterValue=foo \
  --region $REGION \
  --profile $PROFILE
```


# Deploy Test Stack changes
```shell
PROFILE=cloudguru
STACKNAME=mytestinfrastructure
REGION=us-east-1
aws cloudformation deploy \
  --stack-name $STACKNAME \
  --template-file Test.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides param1=foo \
  --region $REGION \
  --profile $PROFILE
```
