# COURSE AWS ACCOUNTS
##  Multi-factor Authentication (MFA) (8:25)
##  [DEMO] Create and secure the master account (12:23)
##  [DEMO] Create the ORG, member accounts (6:09)
##  [DEMO] Configure Role Switch and CLI access using roles (16:04)
# Tech Fundamentals [IF YOU NEED A REFRESHER - IF IN DOUBT .. WATCH]
##  YAML101 - YAML AINT MARKUP LANGUAGE (9:55)
##  JSON101 - JavaScript Object Notation (7:32)
##  Network Starter Pack - 0 - INTRO (5:00)
##  Network Starter Pack - 1 - PHYSICAL (10:02)
##  Network Starter Pack - 2 - Data Link - Part 1 (8:47)
##  Network Starter Pack - 2 - Data Link - Part 2 (14:24)
##  Network Starter Pack - 3 - Network - Part 1 (12:12)
##  Network Starter Pack - 3 - Network - Part 2 (19:13)
##  Network Starter Pack - 3 - Network - Part 3 (15:21)
##  Network Starter Pack - 4 - Transport - Part 1 (15:39)
##  Network Starter Pack - 4 - Transport - Part 2 (17:08)
##  Network Starter Pack - EXTRA - Network Address Translation - PART1 (11:00)
##  Network Starter Pack - EXTRA - Network Address Translation - PART2 (9:38)
##  Network Starter Pack - EXTRA - Subnetting - PART1 (14:35)
##  Network Starter Pack - EXTRA - Subnetting - PART2 (10:33)
##  Distributed Denial of Service (DDoS) attack (14:38)
##  Secure Sockets Layer (SSL) and Transport Layer Security (TLS) (11:41)
# ADVANCED PERMISSIONS & ACCOUNTS
##  Security Token Service (STS) (6:53)
##  Revoking IAM Role Temporary Security Credentials (9:23)
##  [DEMO] Revoking Temporary Credentials - PART1 (13:03)
##  [DEMO] Revoking Temporary Credentials - PART2 (10:07)
##  Policy Interpretation Deep Dive - Example 1 (10:54)
##  Policy Interpretation Deep Dive - Example 2 (9:21)
##  Policy Interpretation Deep Dive - Example 3 (11:14)
##  Permissions Boundaries & Use-cases (17:20)
##  AWS Permissions Evaluation (10:14)
##  [DEMO] Cross Account Access to S3 - SETUP (10:54)
##  [DEMO] Cross Account Access to S3 - PART1 (13:36)
##  [DEMO] Cross Account Access to S3 - PART2 (7:02)
##  AWS Resource Access Manager (RAM) (14:43)
##  [DEMO] Shared ORG VPC - PART1 (11:17)
##  [DEMO] Shared ORG VPC - PART2 (16:04)
##  Service Quotas (13:27)
##  SECTION QUIZ - ADVANCED PERMISSIONS & ACCOUNTS
# ADVANCED IDENTITIES & FEDERATION
##  SAML2.0 Identity Federation (12:21)
##  AWS Single Sign-on (SSO) (9:57)
##  [DEMO] Adding Single Sign-on to the Animals4life ORG - PART1 (15:05)
##  [DEMO] Adding Single Sign-on to the Animals4life ORG - PART2 (11:13)
##  Amazon Cognito (6:21)
##  [AdvancedDemo] Using Web Identity Federation - PART1 (8:51)
##  [AdvancedDemo] Using Web Identity Federation - PART2 (8:27)
##  [AdvancedDemo] Using Web Identity Federation - PART3 (8:33)
##  [AdvancedDemo] Using Web Identity Federation - PART4 (12:33)
##  [AdvancedDemo] Using Web Identity Federation - PART5 (2:46)
##  Amazon Workspaces (8:44)
##  [DEMO] Using workspaces with an AWS Directory Service - PART1 (8:55)
##  [DEMO] Using workspaces with an AWS Directory Service - PART 2 (14:21)
##  Directory Service Deep Dive (Microsoft AD) (10:35)
##  Directory Service Deep Dive (AD Connector) (7:52)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART1 (5:10)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART2 (12:01)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART3 (12:49)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART4 (18:59)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART5 (14:38)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART6 (18:10)
##  [DEMO] Implementing a hybrid directory solution in AWS - PART7 (5:27)
##  SECTION QUIZ - ADVANCED IDENTITIES & FEDERATION
# NETWORKING & HYBRID
##  Border Gateway Protocol 101 (17:29)
##  [Refresher] AWS Global Accelerator (10:37)
##  Site2SiteVPN Refresher (18:00)
##  Transit Gateway Refresher (10:04)
##  Advanced VPC Routing - PART1 (11:29)
##  Advanced VPC Routing - PART2 (11:51)
##  Accelerated Site-to-Site VPN (9:55)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE1 (11:56)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE2 - PART1 (13:44)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE2 - PART2 (11:36)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE3 - PART1 (12:56)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE3 - PART2 (8:22)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE4 (22:19)
##  [NEW][AdvancedDEMO] Advanced Site-to-Site VPN - STAGE5 (3:27)
##  Direct Connect Refresher - PART1 (13:12)
##  Direct Connect Refresher - PART2 (9:30)
##  Direct Connect Resilience (14:07)
##  DX LAGS (5:44)
##  Direct Connect Gateway, TGW and Transit VIFS (13:52)
##  [Refresher] Domain Name System (DNS) Fundamentals - PART1 (11:40)
##  [Refresher] Domain Name System (DNS) Fundamentals - PART2 (10:04)
##  [Refresher] Route53 (R53) Fundamentals (6:06)
##  [Refresher] DNS Record Types (13:25)
##  [Refresher] Route 53 Public Hosted Zones (10:26)
##  [Refresher] Route 53 Health Checks (12:04)
Health checks are separate from records, but are used by records<p>
Health checkers are global. TCP, HTTP,HTTPS, with String Matching (body of response checked - the first 5120 bytes of the response)<p>
Types of checks a)Endpoint that i specify, b)CloudWatch Alarms, c)Checks of checks (overall health - multi factor - e.g. less than X resources healthy)<p>
##  [Refresher] R53 Routing Policies (15:09)
Simple: Routing to a single resource. An IP is fetched from a single record which has 1-N values<p>
Failover: Two records of the same name and type. A primary and secondary. Each record has a health check. Primary always returned if healthy. <p>
Weighted: Multiple records of the same name in the hosted zone, each with a weight value (higher weight - higher probability to fetch record) 
Useful for Load Balancing or testing new software versions<p>
Latency-based: Multiple records with same name and type, specifying region of resource, R53 chooses resource from region with lowest latency <p>
Geolocation: Multiple records with same name and type, specifying location DEFAULT/Continent/Country. Tries to find resource looking a match based on Country THEN Continent THEN Default. Helps fetching continent by location <p>
Multi-value: Multiple records with same name + each health check. Returns all records that are healthy<p>
##  [**NEW**] Gateway Endpoint Refresher (11:41)
Provide private access to S3 and DynamoDB (without them to be public accessible). Per service , per region (region specific) - HA<p>
Prefix list added to route table. Endpoint policy can control access of the endpoint. <p>
Use cases: a)Access to a private VPC to S3 and DynamoDB without internet, b)Allow access to S3 from gateway endpoint ONLY (not from other subnets)<p>
Endpoint Policy just controlls restrictions (like SCP)<p>
##  [**NEW**] Interface Endpoint Refresher (11:14)
Provide private access to ALL EXCEPT S3 and DynamoDB (without them to be public accessible). Per subnet ENI added - NOT HA<p>
Endpoint provides NEW service endpoint DNS for the service REGIONAL and ZONAL. Endpoint policy can control access of the endpoint.<p>
Support Security Groups controlling network access of Endpoints. For TCP and IPv4 ONLY. <p>
Uses PrivateLink (technology allowing AWS or 3rd Party services injected to my VPC with ENI)<p>
Without Private DNS Private Instances go through ENI and Public ones through IGW<p>
With Private DNS (default) the default DNS is overriden and Public and Private instances go through ENI<p>
Endpoint Policy just controlls restrictions (like SCP)<p>
##  VPC Endpoint Policies & Bucket Policies (12:11)
Endpoint Policy just controlls restrictions (like SCP)<p>
Bucket Policy can allow access to specific VPCs<p>
##  [DEMO] Private S3 Buckets - PART1 - SETUP (8:39)
##  [DEMO] Private S3 Buckets - PART2 (17:19)
##  Advanced VPC DNS & DNS Endpoints (15:42)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART1 (8:41)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART2 (7:05)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART3 (16:25)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART4 (8:22)
##  Private Link (8:49)
##  IPv6 Capability in VPCs - PART1 (10:25)
##  IPv6 Capability in VPCs - PART2 (11:04)
##  Advanced VPC Structure - How Many AZs ? (11:53)
##  Advanced VPC Structure - Subnets & Tiers - PART1 (7:43)
##  Advanced VPC Structure - Subnets & Tiers - PART2 (14:10)
##  SECTION QUIZ - NETWORKING & HYBRID
# STORAGE SERVICES
##  [Refresher] FSx for Windows File Server (11:34)
##  [NEW] FSx for Lustre (14:19)
##  EFS Refresher (12:11)
##  [DEMO] Implementing EFS - PART1 (9:08)
##  [DEMO] Implementing EFS - PART2 (12:52)
##  S3 Object Storage Classes - PART1 (9:23)
##  [UPDATE20201110] S3 Object Storage Classes - PART2 (10:02)
##  S3 Lifecycle Configuration (13:05)
##  [Refresher] S3 Replication (13:55)
##  [Refresher] S3 Object Encryption - PART1 (10:08)
##  [Refresher] S3 Object Encryption - PART2 (11:38)
##  [REFRESHER] S3 Presigned URLs (10:57)
##  [UPDATE202101] [DEMO] [Refresher] S3 Presigned URLs (19:12)
##  [Refresher] S3 Select & Glacier Select (5:32)
##  S3 Object Lock (9:56)
##  [UPDATE202102] Amazon Macie (12:04)
##  EBS and Instance Store Performance - PART1 (12:06)
##  EBS and Instance Store Performance - PART2 (11:38)
##  SECTION QUIZ - STORAGE SERVICES
# COMPUTE, SCALING & LOAD BALANCING
##  [NEW] Regional and Global AWS Architecture (11:04)
##  [NEW] EC2 Purchase Options - PART1 (9:26)
##  [NEW] EC2 Purchase Options - PART2 (11:56)
##  Reserved Instances - the rest (11:58)
##  EC2 Networking (16:21)
##  [NEW] Bootstrapping vs AMI Baking (17:09)
##  [NEW] Elastic Load Balancer Architecture (ELB) - PART1 (10:26)
ELB distribute connections of users to back-end services. Load Balancer created with a Single DNS record, type A record<p>
Provisioning items for consideration:<p>
a)IPV4 or IPV4+IPV6<p>
b)AZ used by the ELB (subnets in two or more AZ). Resolves to the Nodes in subnets<p>
c)Internet facing or internal. Related only to the IP address for the Nodes. Functionality / access is same for interne and internal from Node ELB<p>
d)Need preferrably a /27 subnet, can work with /28 as well if needed. Need 8+ Free IPs per subnet<p>
##  [NEW] Elastic Load Balancer Architecture (ELB) - PART2 (12:50)
LB support CROSS-ZONE LB. So a LB Node in AZA can forward traffic to AZB instances and vice versa. Feature that needs to be enabled<p>
ELB is a DNS A record (maps a domain name to the IP address) pointing at Nodes on each AZ<p>
##  [NEW] Session State (9:11)
##  ELB Evolution (4:10)
ELB all three Load Balancers<p>
CLB for Http,Https and lower level. Not really layer 7.Lack Http protocol features. More expensive. 1 SSL per CLB. Do not use<p>
ALB for Http/S/Websocket. Support target group and rules<p>
NLB for TCP,TLC,UDP,TCP_UDP.. Support target group and rules<p>
##  Application vs Network Load Balancers (ALB vs NLB) (16:26)
CLB does not scale (1SSL pes CLB). SNI not supported<p>
ALB supports SNI => For each application/site, using listener based rules, add a Host Rule handling Https, also each rule forwards to multiple target groups<p>
ALB true Layer 7 LB, understands content type, custom headers, user location and app behavior to make decisions <p>
ALB's Https always terminated on the ALB. no unbroken SSL from client to application. => new connection from ALB to Application. <p>
ALB SSL cert installed on ALB if Https used <p>
ALB can check application health<p>
ALB supports Rule Conditions like "host-header", "http-header", path, IP, query string etc, that are processed in a priority order by a listener, and based on that action can be applied (forward, redirect, authenticate-cognito etc). Also a default rule catchall exists if nothing else matches<p>
ALB we could have a Source IP Rule vs the usual Host Rule to identify if the request came from a corprorate IP and forward to other APP<p>
NLB faster than ALB, no understanding of Http,Https (no headers, no cookies, no stickiness), poor health check (ICMP/TCP - not app aware), can have Static IP for whitelisting<p>
NLB unbroken encryption Client to Instance using TCP Listeners. Used with PrivateLink to provide services to other VPCs<p>
##  [NEW] Session Stickiness (9:25)
ALB cookie duration 1s - 7 days. Backend instance will change if a)cookie expires b)instance fails. Needed when backend is stateful and want to use ELB. BAD - Uneven load.<p>
Cookie AWSALB for ALB (AWSELB for CLB) held by client, locks session to 1 Backend Instance. Optimal is to store session data externally and not use stickiness<p>
##  [DEMO] Seeing Session Stickiness in Action (13:29)
##  ASG Refresher (16:12)
ASG provide Automatic Scaling and Self-Healing for EC2 using EITHER a Launch Configuration OR a Launch Template version. Min, Desired, Max sizes<p>
Scaling Policy allows for dynamic Desired capacity based on metrics. a)Manual Scaling b)Scaled Scheduling (time based) c)Dynamic Scaling - c1)Simple, CPU>50%+1 CPU<30%-1 c2)Stepped, greater steps for quicker reactions 1 (e.g. +1 for 50%, +3 for 80%) c3)Target Tracking, +- based on specific target of metrics<p>
Cooldown period: Time to wait after scaling action before proceeding to next, to reduce costs<p>
ASG instances are added to or removed from a Target Group <p>
ASG can use Load Balancer checks which are much richer than EC2 checks. Careful the check to be appropriate<p>
ASG Scaling Processes: Launch - SUSPEND => No scale out, Terminate - SUSPEND => No scale in. RESUME scale in/out functional again <p>
ASG options to "AddToLoadBalancer", "AlarmNotification" (accept CW notifications), "AZRebalance" (Balance Instances eveny across AZs), "HealthCheck" (instance health checks on/off), "ReplaceUnhealthy" (terminate and replace unhealthy), "ScheduledActions", "Standby" (to put them aside from ASG for a while, maintenance)<p>
Free, Cool down large for cost effective, Smaller instances for granularity, ASG With ALB-> Elasticity<p>
##  ASG Lifecycle Hooks (5:24)
ASG Lifecycle Hooks allows to configure custom actions that will take place on ASG actions (events launch/terminate transitions)<p>
Adding a Lifecycle Hook on Launch or Terminate we can add two more intermediate states that will wait for X time OR until we run the "CompleteLifecycleAction" before the "InService" or "Terminate" state. This is accomplished with SNS, SQS or EventBridge receiving notifications (requires also a role and Notification metadata in lifecycle Hook edited accordingly)<p>
##  EC2 Placement Groups (14:29)
##  SECTION QUIZ - COMPUTE, SCALING & LOAD BALANCING
# MONITORING, LOGGING & COST MANAGEMENT
##  CloudWatch-PART1 (10:00)
##  CloudWatch-PART2 (9:31)
##  CloudWatch Logs Refresher (14:00)
##  [Refresher] CloudTrail Refresher (14:10)
##  [DEMO] Setting up an Organisational Trail (17:53)
##  AWS X-Ray (6:42)
##  Cost Allocation Tags (4:43)
##  Trusted Advisor (8:35)
##  Section Quiz - Logging, Monitoring & Cost Management
# DATABASES
Relational / Key-Value / Document / In Memory / Graph / Time Series / Ledger<p>
##  [Refresher] RDS Architecture (9:37)
Oracle/Postgre/SQL Server/MariaDB/MySQL<p>
Supports Read Replicas / Automated Backups / Scalable Storage and Compute / Multi AZ for failover<p>
Cloudwatch reads metrics from hypervisor (so limited data) - Measures Freeable memory (which includes memory that could be in use in buffers and cache)<p>
Enhanced Monitoring retrieves data from Agent on the instance - Measures Free Memory+++ (actual free memory) or swap<p>
Event Bridge > CloudWatch Events. <p>
Instance statuses failed, restore-error,incompatible can result in severe outage<p>
Statuses like incopatible and failed are not billable<p>
Logs depend on config parameters: Error for erros, general for SQL user log, slow query for queries that take long, audit for queries, <p>
MySQL , Maria DB log which statements are logged and slow queries<p>
Postgre logs DML,DDL, or BOth and Slow queries and config of retention period<p>
RDS: We can export the logs to CloudWatch logs for security investigations, performance investigation etc<p>
RDS -> CW logs -> LogGroup -> Filter Pattern -> Custom Metric -> S3 -> Athena etc<p>
Error of a user when creating a service-linked role -> may be missing iam:CreateServiceLinkedRole perimission<p>
AmazonRDSReadOnlyAccess for reading , AmazonRDSFullAccess for full access<p>
Supports External Authentication Kerberos and MicrosoftAD (NOT for MariaDB)<p>
IAM auth supported during creation or later<p>
But has limitations (MySQL 200 connections/sec / Postgre needs SSL enabled), accomplished by generation of token expiring within 15 minutes<p>
Secrets Manager can rotate passwords<p>
RDS CA-2019 is used for SSL<p>
SSL can be forced for Postgre to all users<p>
DB Subnet groups need to have either ALL private or ALL public subnets<p>
VPC can be changed if we modify the DB subnet group. New Security group will also be used (restart takes place)<p>
To change storage, we trigger the instance to a storage-optiization status. This can't change for 6 hours. Also increase should be minimum 10% upwards. Reducing is harder (with DMS or export to new)<p>
OUTAGE:a)Same AZ Region Changing Storage Type, b)DB Engine Maintenance change of Major Version upgrade (except MS SQL Server)<p>
NO OUTAGE: a)Converting from 1AZ to Multi AZ<p>
Best Practices for RDS: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html<p>
Static parameters require restart while Dynamic apply immdediately.<p>
Parameter Groups are the main configuration. Option groups are special configuration and VPC specific<p>
Persistent option of Option Group can be modified<p>
Permanent option of Option Group can't be modified<p>
Changing Parameter Group needs reboot<p>
Maintenance: <p>
a)Required - some time will be applied eventually  (security,availablities) - multi az reduces time to failover time<p>
b)Available - option not mandatory<p>
c)Next Window - schedule for next window (can be deferred)<p>
d)In progress - can't be stopped till finishes<p>
Maintenance window defined by me or random 30-minute in an 8 hour time block, which varies per region, in UTC time<p>
Hardware maintenance shown only on Dashboard<p>
Troubleshooting: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Troubleshooting.html<p>
a)Issue: Changes not taking effect -> Symptom: Parameter Group is in "pending-reboot" state or static parameter changed -> Fix: reboot by myself or maintenance rebooting is needed<p>
b) Issue: Storage full  -> Symptom: Users complain/Console showing error/e.g in 6 hours needed more storage than auto scaled previously  -> Fix: ModifyDBInstance + check reason  <p>
c) Issue: Replication stopped -> Symptom: Complaint stale data / Problem on migration / Errors in logs  -> Fix: e.g. match parameter group configuration (network size may vary) / Ensure read_only on replica / replication supported on InnoDB only <p>
d) Issue: Insufficient Capacity Error -> Symptom: Unable to create or update DB  -> Fix: Try different size, AZ or at another time <p>
e) Issue: Too many connetcions -> Symptom: Some connect some not  -> Fix: Increase connections / check reason <p>
On demand pricing , calculated by second. For unpredictable load<p>
Reserved Instance pricing, one-to-three year purchase. For predictable load<p>
Backup storage 1:1 is free<p>
Data Transfer across regions is NOT free and EC2-RDS across AZ is NOT FREE<p>
Data transfer Across AZ for Multi AZ and replication is Free<p>
Oracle is the only that has BYOL (bring your own license)<p>
Rebooting a Multi AZ DB, with Failover, swaps primary and failover instances (has 30 sec downtime)<p>
Creating a RR on an RDS adds an asynch replica instance, (has no downtime - takes 9 minutes)<p>
Promote RR from replica to primary (no downtime/lost data ONLY ON MySQL and Maria DB  - Other DBs lose data - takes 9 minutes) - Need to change DNS from the Private Route 53 DNS CNAME<p>
Working with RR - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html<p>
AWS Provides Managed Database Instances (even though it is called DBaaS it is not 100% accurate) - convenience to not handle EC2 instances<p>
##  [Refresher] RDS Multi-AZ (8:53)
MultiAZ is same Region only, 60-120 failover, does SYNCHRONOUS replication, can occur in several cases<p>
##  [Refresher] RDS Backups and Restores (13:25)
Automatic Backups and Manual Snapshots are stored in S3 managed buckets<p>
for single AZ they are done on the primary, on multi AZ from standby<p>
First snapshot is full then incremental. Manual snapshots need to be deleted manually. Do not expire<p>
GOOD RPO BAD RTO
##  [Refresher] RDS Read-Replicas (7:52)
Performance and Availability benefits<p>
RDS Read Replicas can be added to an RDS Instance - 5 direct per primary instance.<p>
They can be in the same region, or cross-region replicas.<p>
They provide read performance scaling for the instance, but also offer low RTO recovery for any instance failure issues<p>
N.B they don't help with data corruption as the corruption will be replicated to the RR.<p>
GOOD RTO BEST RPO But can have corrupt data replicated<p>
RR is Read only until promoted (irreversible)<p>
Promote RR to Primary ONLY on failure<p>
##  RDS Data Security (7:03)
Supported EBS volumes encrypted by KMS, with CMS or AWS key<p>
MSSQL and Oracle support TDE encryption (Engine doing the encryption - not just aws). Oracle uses CloudHSM<p>
When KMS is used, DEK (Data Encryption Keys) are generated by KMS and hosted on hosts. These are used to encrypt/decrypted data without the DB knowing it<p>
IAM authentication is supported: 1)Create RDS Local DB account 2)Configure to use AWS auth token 3)Policy attached to Users or roles mapping IAM identity to local RDS user 4)IAM genearate-db-auth-token valid for 15 minutes 5)token is used=> login as the user. THIS IS AUTHENTICATION ONLY. AUTHORIZATION DONE BY RDS Instance<p>

##  [Refresher] Aurora Architecture (13:02)
MySQL/Postgre<p>
Scalable Reads / Automated Backups / Auto Scaling Cluster / Multi master support<p>
##  [Refresher] Aurora Serverless Architecture (9:52)
##  [Refresher] Multi-master writes (7:51)
##  [Refresher] DynamoDB Architecture Basics (11:14)
DynamoDB stores data in partitions, ideally i should make tables with a partition key of large number distinct values
Data after hash function are stored in specific partition (based on hashed partition key) and DynamoDB will search later on using similar hash on the specific partition
Each Partition can hold up to 10GB of data, supporting up to 3000 read capacity and 1000 write capacity
Hashing is done with consistent hashing. Key is hashed (Mark->1633428562) -> hash key mod N (e.g. 52) -> find first node where it is >=52 (clockwise)
1 RCU supports 1 Strongly Consistent Read or 2 Eventually Consistent Reads
Paxos protocol (for resolving consensus in the network)  identifies the leader storage node
On eventual consistency a random node may be used which may not had the time to synch the data
Scan Filtering reads everything of a TABLE and then throws away (slow and not using indexes) - it is better using queries and indexes
Scan default eventuallyConsistent but can become strong consistent with ConsistentRead parameter
Results are no more than 1Mb, if more we should use pagination
Query is done on a specific PARTITION and uses PK, PK+SK, or secodary indexes
PutItem overwrites the whole item (all attributes) with the new version being passed while UpdateItem will only Update the passed attributes
DYnamoDB allows both Replication and Sharding
Allows Batch Operations
 
##  [Refresher] DynamoDB Operations, Consistency and Performance - PART1 (13:06)
On demand capacity (expensive-flexible / good for new tables with unknown workload / unpredictable traffic / pay as you go)
Provisioned capacity (cheap-not flexible / good for predictable traffic / capacity requirements can be forecasted)
Switch between modes once per 24 hrs
ARN is Region/Account/Table Name specific
Table contains Items (rows). Each item has attributes
Items are limited to 400Kb
Binary should be converted to Base64, support number, string,binary,boolean,null,List Document, Map Document, Set of String/number/Binary
Table name unique for the same Account/Region 
##  [Refresher] DynamoDB Operations, Consistency and Performance - PART2 (11:24)
Dynamo DB supports Recovery Point in time for the last 35 days
I can inititate backups like RDS Snapshots
Metrics like RWCapacityUnits / ReadThrottleEvents / SuccesfulRequestLatency / SystemErrors / ThrottledRequests / UserErrors / WriteThrottleErrors
boto3 and similar SDKs support exponential backoff retries when we have Read or Write throttle events
exponential backoff retries is a must on Batch Operations / unprocessed items should be retried
##  [Refresher] DynamoDB Indexes (LSI and GSI) (12:32)
Local Secondary Index must be created ONLY on creation of table. Has the same Partition Key as the table but different Sort key
##  [Refresher] DynamoDB Streams and Triggers (8:48)
##  [Refresher] DynamoDB Accelerator (DAX) (10:58)
##  [Refresher] DynamoDB Global Tables (5:20)
##  AWS Elasticsearch (7:24)
##  [Refresher] Athena (8:52)
##  [DEMO] Athena - Part 1 (14:01)
##  [DEMO] Athena - Part 2 (11:21)
##  Amazon Neptune (6:48)
##  Amazon Quantum Ledger Database (QLDB) (6:21)
##  SECTION QUIZ - DATABASES
# DATA ANALYTICS
##  [Refresher] Kinesis Data Streams (10:42)
##  Kinesis Data Firehose - Advanced (9:11)
##  Kinesis Data Analytics - Advanced (9:00)
##  MapReduce 101 (10:24)
##  EMR Architecture (13:51)
##  Redshift Architecture (11:32)
##  Redshift Resilience and Recovery (3:40)
##  AWS Batch (14:44)
##  AWS Quicksight (4:08)
##  SECTION QUIZ - DATA ANALYTICS
# APP SERVICES, CONTAINERS & SERVERLESS
##  [Refresher] Introduction to containers (17:13)
##  [DEMO] [Refresher] Creating a Container Image (17:25)
##  [Refresher] ECS - Concepts (10:25)
##  [Refresher] ECS - Cluster Types (13:30)
##  [DEMO][Refresher] - Deploying 'container of cats' using Fargate (16:08)
##  [Refresher] Simple Notification Service (SNS) (7:49)
##  [Refresher] Simple Queue Service [SQS] (15:46)
##  Amazon MQ (8:15)
##  AWS Lambda In-depth - PART1 (11:08)
##  AWS Lambda In-depth - PART2 (13:59)
##  AWS Lambda In-depth - PART3 (17:24)
##  [UPDATE202101] [DEMO] Accessing Private VPC Resources using Lambda w/ TheCatAPI!!!! - PART1 (8:14)
##  [UPDATE202101] [DEMO] Accessing Private VPC Resources using Lambda w/ TheCatAPI!!!! - PART2 (17:20)
##  [Refresher] CloudWatchEvents & EventBridge (6:58)
##  Advanced API Gateway (17:12)
##  [Refresher] AWS Step Functions (16:09)
##  Simple Workflow Service (SWF) (8:13)
##  Amazon Mechanical Turk (3:44)
##  Elastic Transcoder & AWS Elemental MediaConvert (8:45)
##  AWS IOT (6:30)
##  AWS Greengrass (4:15)
##  SAM - Serverless Application Model (5:48)
##  [DEMO] SAM CLI (18:57)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART1 (4:40)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART2 (7:47)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART3 (15:25)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART4 (13:22)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART5 (14:44)
##  [AdvancedDemo] Build A Serverless App - Pet-Cuddle-o-Tron - PART6 (1:56)
##  Section Quiz - APP SERVICES & SERVERLESS
# CACHING, DELIVERY AND EDGE
##  [NEW] CloudFront Architecture - Refresher (16:09)
##  [NEW] CloudFront Behaviours (10:49)
##  [NEW] TTL and Invalidations (13:53)
##  [NEW] CloudFront, SSL & SNI (15:10)
##  [NEW] Origin Types & Origin Architecture (10:15)
##  [NEW] Caching Performance & Optimisation (16:23)
##  [NEW] CloudFront Security - OAI & Custom Origins (8:50)
##  [NEW] CloudFront Security - Private Distributions (9:14)
##  [NEW] CloudFront Geo Restriction (9:52)
##  [NEW] CloudFront Security - Field-Level Encryption (9:26)
##  [NEW] CloudFront - Lambda@Edge (8:03)
##  [NEW] Elasticache (12:51)
##  SECTION QUIZ - CACHING, DELIVERY AND EDGE
# MIGRATIONS & EXTENSIONS
##  The 6R's of Cloud Migration (15:45)
##  Virtual Machine Migrations (8:08)
##  Database Migration Service (DMS) (11:06)
##  [AdvancedDEMO] Database Migration Service-STAGE1 (6:08)
##  [AdvancedDEMO] Database Migration Service-STAGE2 (6:52)
##  [AdvancedDEMO] Database Migration Service-STAGE3-PART1 (11:16)
##  [AdvancedDEMO] Database Migration Service-STAGE3-PART2 (9:05)
##  [AdvancedDEMO] Database Migration Service-STAGE4 (14:40)
##  [AdvancedDEMO] Database Migration Service-STAGE5 (4:27)
##  Storage Gateway - Volume Gateway (14:15)
##  Storage Gateway - Tape Gateway (VTL) (12:11)
##  Storage Gateway - File Gateway (12:17)
##  AWS Snowball // Snowball Edge // Snowmobile (10:45)
##  [Refresher] AWS Datasync (9:27)
##  SECTION QUIZ - MIGRATIONS & EXTENSIONS
# DEPLOYMENT & MANAGEMENT
##  [Refresher] CloudFormation Refresher (10:55)
Importing Stacks and not hardcoding ARN ensures a deletion of an imported stack does not leave the stack orphan. Prefer it over hardcoded ARN
cfn-init (try to reach specific end states - unlike bootstrap that runs script)
cfn-signal can provide accurately if the creation has indeed been completed
cfn-hup to monitor for N time after cfn-init, for changes/actions
logs of cfn-init and similar are under var/log on Ubuntu
AWS SAM, i can write on YAML/JSON and also test locally. Supports native transformation
AWS CDK, i can write on javascript/typescript/python/java/.net. Reusability. Supports native transformation
##  CloudFormation Custom Resources-PART1-THEORY (11:43)
##  CloudFormation Custom Resources-PART2-DEMO (11:35)
##  CloudFormation Nested Stacks (14:17)
##  CloudFormation Cross-Stack References (10:06)
##  CloudFormation Stack Sets-PART1-THEORY (9:21)
##  CloudFormation Stack Sets-PART2-DEMO (9:55)
##  CloudFormation Stack Roles (6:52)
##  Service Catalog (7:25)
##  CI/CD using AWS Code* (15:29)
##  Elastic Beanstalk (18:47)
##  [NEW] OpsWorks (15:56)
##  AWS Systems Manager - Agent Architecture (7:39)
##  AWS Systems Manager - Run Command (4:47)
##  AWS Systems Manager - Patch Manager (12:00)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE1 (9:23)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE2 (13:17)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE3a (8:14)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE3b (13:25)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE4 (8:34)
##  [NEW][AdvancedDEMO] - Systems Manager - STAGE5 (7:19)
##  SECTION QUIZ - DEPLOYMENT & MANAGEMENT
# ADVANCED SECURITY AND CONFIG MANAGEMENT
##  AWS Guard Duty (4:32)
##  AWS Config (6:39)
##  AWS Inspector (7:26)
##  [Refresher] Encryption 101 - PART1 (14:13)
##  [Refresher] Encryption 101 - PART2 (7:10)
##  Key Management Service (KMS) (18:03)
##  CloudHSM (15:10)
##  AWS Certificate Manager (ACM) (11:21)
##  [Refresher] AWS Parameter Store (5:20)
##  [Refresher] AWS Secrets Manager (7:47)
##  VPC Flow Logs & Flow Logs vs Packet Sniffing (11:16)
##  [Refresher] AWS WAF and Shield (12:57)
##  Section Quiz - ADVANCED SECURITY AND CONFIG MANAGEMENT
# DISASTER RECOVERY & BUSINESS CONTINUITY IN AWS
##  Types of DR - Cold, Warm, PilotLight (17:41)
##  DR Architecture - Storage (8:09)
##  DR Architecture - Compute (7:52)
##  DR Architecture - Database (10:20)
##  DR Architecture - Networking (8:22)
##  Section Quiz - DISASTER RECOVERY & BUSINESS CONTINUITY IN AWS
# EVERYTHING ELSE
##  Amazon Lex & Connect (7:45)
##  AWS Rekognition (4:51)
##  Kinesis Video Streams (5:09)
##  AWS Glue (6:23)
##  Device Farm (4:19)



