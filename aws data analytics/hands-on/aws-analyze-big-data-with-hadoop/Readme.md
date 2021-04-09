## Analyze big data with Hadoop
https://aws.amazon.com/getting-started/hands-on/analyze-big-data/?trk=gs_card


![image](firefox_u8YvlFIO6z.png)

Steps:
1. Create EC2 keypair (to be able to access later on EC2s) - named "myemrkeypair"
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:
2. Create S3 bucket named "pkammasemrbucket" and "pkammasemrbucketoutput"
https://s3.console.aws.amazon.com/s3/home?region=us-east-1#
3. Upload health_violations.py to S3 bucket
https://s3.console.aws.amazon.com/s3/upload/pkammasemrbucket?region=us-east-1
4. Upload food_establishment_data.csv to S3 bucket
5. Run on CLI:
```
PROFILE=cloudguru

aws configure --profile  $PROFILE 

aws emr create-default-roles --profile $PROFILE

--Add to EMR_DefaultRole the AmazonEC2FullAccess 

aws emr create-cluster \
--name "My X EMR Cluster" \
--release-label emr-5.32.0 \
--applications Name=Spark \
--ec2-attributes KeyName=myemrkeypair \
--instance-type m4.large \
--instance-count 3 \
--profile $PROFILE \
--use-default-roles

aws emr describe-cluster --cluster-id j-HB1V4BZHVFXP --profile $PROFILE


aws emr add-steps \
--cluster-id j-HB1V4BZHVFXP \
--steps Type=Spark,Name="My Spark Application",ActionOnFailure=CONTINUE,Args=[s3://pkammaemrbucket/health_violations.py,--data_source,s3://pkammaemrbucket/food_establishment_data.csv,--output_uri,s3://pkammaemrbucketoutput/myOutputFolder]
							

For Console:

ApplicationLocation:
s3://pkammaemrbucket/health_violations.py


Arguments:
--data_source s3://pkammaemrbucket/food_establishment_data.csv
--output_uri s3://pkammaemrbucketoutput/myOutputFolder

```
