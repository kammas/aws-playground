**STEP#1 - Create a Kinesis Data Stream using name 'my-data-stream'**

## Deploying the full infrastructure via CLI 
```shell
aws configure --profile cloudguru
aws configure list --profile cloudguru
aws s3 ls --profile cloudguru
```



## Create Main Stack
```shell
PROFILE=cloudguru
STACKNAME=Kinesis01
REGION=us-east-1
aws cloudformation create-stack \
  --stack-name $STACKNAME \
  --template-body file://./template.yaml \
  --stack-policy-body file://./stack-policy.json \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
  --region $REGION \
  --profile $PROFILE
```


**STEP#3 - Create a Kinesis Delivery Stream using name 'my-delivery-stream'**

**STEP#4 - Create a Kinesis Data Analytics apllication using name 'my-analytic-application'**
-> Connect the Data Stream
-> Discover Schema
-> Go to SQL Editor
-> Add Sql From Templates

CREATE OR REPLACE STREAM "DESTINATION_USER_DATA" (
    first VARCHAR(16), 
    last VARCHAR(16), 
    age INTEGER, 
    gender VARCHAR(16), 
    latitude FLOAT, 
    longitude FLOAT
);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_USER_DATA"

SELECT STREAM "first", "last", "age", "gender", "latitude", "longitude"
FROM "SOURCE_SQL_STREAM_001"
WHERE "age" >= 21;

-> Real Data are streamed

We can also persist these data (the filtered) by sending them to Redshift -> S3 by choosing a destination