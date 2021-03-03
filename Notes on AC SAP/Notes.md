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
Service for **Ingestion, Storage and Management** of **Metrics**<p>
Public service so it is accessible from VPC and On Prem using API or Agent (custom metric)<p>
Installing a CloudWatch Agent can provide richer metrics<p>
Cloudwatch alarms react to metrics in comparison to **thresholds** and can be used to notify or perform actions (SNS notifications, ASG scaling events, EventBridge Events)<p>
Apps from VPCs can connect to cloudwatch using either an IGW/Nat GW or an Interface Endpoint<p>
**Namespace** is a container for metrics (e.g. AWS/EC2, AWS/Lambda). Start with AWS ONLY for Amazon metrics<p>
**Datapoint** the smallest component of CW. Has a timestamp and a value<p>
**Metric** a time ordered set of datapoints (e.g. CPUUtilization, NetworkIn,..) . Datapoint is included<p>
**Each Metric** has a **Namespace** and a **MetricName**  <p>
**Dimension** is a key pair allowing to multi tag a metric so as to use it in groups and aggregates accoringly afterwards or not<p>
##  CloudWatch-PART2 (9:31)
**Resolution** either a)standard (60 second granularity) b)high (one second granularity) <p>
**Statistics** are metric data aggregations over specified periods of time (e.g. Sum, Average) and use **Units** of measure (Bytes,Seconds,...)<p>
**Retention** As data ages they are aggregated and stored for longer with less resolution (<60s for 3 hours, 60s for 15 days etc>)<p>
**Percentile** help eliminate outliers by removing great peaks of data<p>
1 Namespace - N Metric<p>
1 Metric - N Datapoint<p>
1 Datapoint - 1 Timestamp,Value,Unit of measure<p>
N Dimensions - M Metrics<p>
##  CloudWatch Logs Refresher (14:00)
We can publish multiple logs to Cloudwatch (e.g for mysql mysql error log, slow query log, general log) or any other log, for cloudwatch to ingest them, on public AWS<p>
Also we can subscribe services to Cloudwatch events to trigger further actions<p>
Cloudwatch logs are sent to the Region they were generated otherwise us-east-1 if service is global
**Log stream** is a sequence of Log Events that share the same source
**Log Group** is a group of Log Streams that share the same retention,monitoring and access control settings
**Metric Filter** can keep looking for specific pattern to result in a **Metric** that can generate alarm, which can trigger events
Exporting logs from Cloudwatch to S3 can take up to 12 hours (not real time) and the encryption will be done wih SSE-S3
**Subscription Filters** can be used to trigger lambda function based on incoming logs from log groups, or merge data in Kinesis Data Stream or other solutions
For near-realtime storage of logs Kinesis Firehose can be used as the destination of Subscription Filters, and for realtime to Lambda or Kinesis Streams
For generating a cloud watch Metric a Metric Filter can be used
##  [Refresher] CloudTrail Refresher (14:10)
##  [DEMO] Setting up an Organisational Trail (17:53)
##  AWS X-Ray (6:42)
##  Cost Allocation Tags (4:43)
##  Trusted Advisor (8:35)
##  Section Quiz - Logging, Monitoring & Cost Management
# DATABASES
Relational / Key-Value / Document / In Memory / Graph / Time Series / Ledger<p>
Document DB is compatible with MongoDB, fully managed like RDS, restore point time like aurora,  like aurora in terms of cluster volume technology
endpoints like aurora, good for CMS, or user profiles
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
IAM authentication is supported: 1)Create RDS Local DB account 2)Configure to use AWS auth token 3)Policy attached to Users or roles mapping IAM identity to local RDS user 4)IAM generate-db-auth-token valid for 15 minutes 5)token is used=> login as the user. THIS IS AUTHENTICATION ONLY. AUTHORIZATION DONE BY RDS Instance<p>
##  [Refresher] Aurora Architecture (13:02)
Failover to a replica is much faster than RDS as Aurora does not need to make changes in storage. Instances use shared volume for storage<p>
Autoscaling, self-healing cluster volume storage, Cross Region Replication, Multi master??? global database
MySQL/Postgre<p>
Scalable Reads / Automated Backups / Auto Scaling Cluster / Multi master support<p>
stores 6 copies of data to 3 AZs
Writer endpoint (master)  and reader endpoints (replicas) 
Faster recovery from database crashes than MySQL and Postgre as it will not rely on redo logs (slightly worse performance though)
Replication features
1. Single Master with 15 replicas max
1. Multi master

Backtrack can rewind back in time without new snapshot (back to X hours) - Much better than Point In Time recovery - Maximum backtrack 72 hours<p>
Can autoscale replicas based on metrics<p>
Aurora to aurora replication lag is minimal. Replication lag (On prem RDS to Aurora etc) due to Mysql native replication can be much higher<p>
We have metrics for persistent storage and for temporary storage (like temp tablespace in oracle)<p>
Useful metrics also like 
1. DB Connections
1. Write IOPS
1. Free local storage
1. CPU utilization
1. Buffer Cache hit ratio

We can create Fault Injection queries to simulate a crash of a replica,simulate disk failure, simulate disk congestion , for X duration<p>
Backups are automatic, and incremetal for retention period up to 35 days, not utilizing IO<p>
Aurora supports also cloning a cluster, which is much faster than new instance from snapshot, however clusters shares the same volume until data change (new data - new volume)<p>
In Aurora UNLIKE RDS we cannot change VPC connectivity after creation. Needs a new clone. To move to new VPC we could:
1. Clone to a new VPC (but same region)
1. Snapshot to a new VPC 
1. Replica to a new VPC and then use MySQL BinLog replication until Lag=0, drain connections, update endpoint or record and done

Clones can be useful for: Testing changes without impact on production / Parameter Group experimentation / Avoid disruptive workload / Cross account sharing / Outside Access using RAM<p>
Authentication with password or IAM/tokens like RDS<p>
Besides Cluster Endpoint (writer) and Reader Endpoint (reader) also supports Custom endpoint where we can define to which writer/reader endpoint will be used. Custom OR Reader<p>
To authenticate with aurora using IAM i need to:
1. Enable IAM authentication for the resource (aurora cluster) AND Create IAM policy to grant me rds-db:connect permission
1. Create user in DB with same username and with AWSAuthenticationPlugin as 'RDS' 
1. User requests from IAM to generate db-auth token
1. user authenticates to aurora with username and token as password (valid for 15 minutes)

KMS keys are region specific.<p>
CANNOT SWAP encryption on existing instance (encrypted stays encrypted, not encrypted remains not encrypted)<p>
WE CAN RESTORE SNAPSHOT and then SWAP encryption<p>
Cross Region Replicas VS Global Database:
1. Using our resources, prone to replication lag, bin log replication VS no-single thread replication bottleneck
1. Several minutes RTO and RPO VS few seconds RPO and 1 minute RTO 
1. Data transfer fees across region VS no fees
1. Global supports write forwarding (send data to close Region and it will forward to primary region faster than internet)

Global Limitations:
1. DOES NOT support Cloning
1. DOES NOT support Backtrack
1. DOES NOT support Parallel Query
1. DOES NOT support Serverless
1. DOES NOT support Start/Stop

##  [Refresher] Aurora Serverless Architecture (9:52)
Minimum and Maximum ACU is defined (Aurora Capacity Units) <p>
No scale up cooldown, <p>
Scale down 15 minute from Scale Up, and 5 minute from scale down <p>
Force scaling can cause interruptions (if during scale down a connection takes too long to complete)<p>
We can pause compute capacity after X time of inactivity<p>
Allows also Http Data API<p>
##  [Refresher] Aurora Multi-master writes (7:51)
Supports in one region to use multiple writes which share the same volume so they are greatly fault tolerant<p>
##  [Refresher] DynamoDB Architecture Basics (11:14)
DynamoDB stores data in partitions, ideally i should make tables with a partition key of large number distinct values<p>
Uniqueness of a row is defined by the primary key (if there is no sort key) or the primary and sort key combination<p>
1 WCU = 1KB/second. 1 RCU = 4KB/second - USING CONSISTENT READS
Data after hash function are stored in specific partition (based on hashed partition key) and DynamoDB will search later on using similar hash on the specific partition<p>
Each Partition can hold up to 10GB of data, supporting up to 3000 read capacity and 1000 write capacity<p>
Hashing is done with consistent hashing. Key is hashed (Mark->1633428562) -> hash key mod N (e.g. 52) -> find first node where it is >=52 (clockwise)<p>
1 RCU supports 1 Strongly Consistent Read or 2 Eventually Consistent Reads<p>
Paxos protocol (for resolving consensus in the network)  identifies the leader storage node<p>
On eventual consistency a random node may be used which may not had the time to synch the data<p>
DYnamoDB allows both Replication and Sharding<p>
Allows Batch Operations<p>
Highly advised to offload large attribute values to S3  
I can use Atomic transactions using TransactWriteItems or TransactGet items and write or read ALL TOGETHER. Up to 25 items or 4MB, within same Region and same account<p>
TTL helps automatically clean items that are useless after X time (e.g. sessions). Data are actually deleted after 48hrs with eventually consistency, may need to add filter expression in queries to not fetch these items, TTL attribute should be number in epoch time <p>
Encryption in transit uses https, all table data at rest also encyrpted including DAX clusters using CMK owned by AWS (default) or managed by AWS (KMS option) - better for auditing to use KMS <p>
Partition Key should not be encrypted to be discoverable<p>
If a user does not have access to the KMS key he can't decrypt the content of the attribute<p>
I can encrypt data before sending them to DynamoDB, using the KMS key<p>
To allow an EC2 instance to connect with DynamoDB without internet we are using a VPC endpoint (Gateway) - will modify route table <p>
##  [Refresher] DynamoDB Operations, Consistency and Performance - PART1 (13:06)
On demand capacity (expensive-flexible / good for new tables with unknown workload / unpredictable traffic / pay as you go)<p>
Provisioned capacity (cheap-not flexible / good for predictable traffic / capacity requirements can be forecasted)<p>
Switch between modes once per 24 hrs<p>
ARN is Region/Account/Table Name specific<p>
Table contains Items (rows). Each item has attributes<p>
Items are limited to 400Kb<p>
Binary should be converted to Base64, support number, string,binary,boolean,null,List Document, Map Document, Set of String/number/Binary<p>
Table name unique for the same Account/Region <p>
##  [Refresher] DynamoDB Operations, Consistency and Performance - PART2 (11:24)
Dynamo DB supports Recovery Point in time for the last 35 days<p>
I can inititate backups like RDS Snapshots<p>
Metrics like RWCapacityUnits / ReadThrottleEvents / SuccesfulRequestLatency / SystemErrors / ThrottledRequests / UserErrors / WriteThrottleErrors<p>
boto3 and similar SDKs support exponential backoff retries when we have Read or Write throttle events<p>
exponential backoff retries is a must on Batch Operations / unprocessed items should be retried<p>
##  [Refresher] DynamoDB Indexes (LSI and GSI) (12:32)
Use GSIs as default, LSI only when strong consistency is required
Local Secondary Index must be created ONLY on creation of table. Has the same Partition Key as the table but different Sort key. Shares the RCU and WCU as the table<p>
Global Secondary Index can be created anytime (creates new table with PK and SK we used). Partition key can be anything and sort key is optional. Uses its own RCU and WCU. I can choose the attributes (columns) that will be projected (fetched) to reduce capacity to minimum. They are Sparse by default (fetching items non-null)<p>
Projection expressions help us defining what we want to be returned (to reduce consumption)<p>
Scan Filtering reads everything of a TABLE and then throws away (slow and not using indexes) - it is better using queries and indexes<p>
Scan default eventuallyConsistent but can become strong consistent with ConsistentRead parameter<p>
Results are no more than 1Mb, if more we should use pagination<p>
Query is done on a specific PARTITION KEY, and optionally one or more SK values. This applies to both LSI and GSI<p>
PutItem overwrites the whole item (all attributes) with the new version being passed while UpdateItem will only Update the passed attributes<p>
##  [Refresher] DynamoDB Streams and Triggers (8:48)
The stream can be configured to provide as view type the following and generate an event
1. the keys only (PK and SK)
1. the new image (the entire new record)
1. the old image (the entire old record)
1. the new and old image (entire new and old record)

##  [Refresher] DynamoDB Accelerator (DAX) (10:58)
Dax can improve performance up to 10x, reduces request times from millis to micros<p>
NO NEED for developer changes!!<p>
DAX is provisioned in multiple AZs for HA. Automatically fails over and promotes new primary node<p>
Supports up to 10 nodes per cluster (1 primary and 9 replicas)<p>
Supports everything except control plane APIs (createTable,DeleteTable etc)<p>
DAX cluster Requires an IAM service role to have access to DynamoDB and also association to a subnet group<p>
On miss cache, an eventually consistent get item operation on DynamoDB occurs. Does not support eventually consistent reads<p>
DAX supports write-through, data is written to DDB then DAX<p>
DAX has an ITEM cache and a QUERY cache mapped to results<p>
DAX can be used when we have
1. need for absolutely minimum latency
1. lots of reads which can be eventually consistent
1. light writes

##  [Refresher] DynamoDB Global Tables (5:20)
Multi master, cross region replication<p>
Strongly consistent reads ONLY in the same region as writes<p>
To setup global tables for a table 
1. it has to be EMPTY
1. I need to enable streams (to replicate)
1. add supported region

Last writer wins
##  ACG On Migration of Mysql to Dynamo DB using DMS
To do so i need to 
1. Create a Replication Instance on DMS
1. Choose source endpoint for source DB (MySql)
1. Create IAM role to allow data to be added to DynamoDB (service that will use this role==DMS, attach policy )
1. find the arn of the role
1. Create target endpoint
1. Create database migration task in DMS
1. Choose if it should 
    * migrate existing data
    * migrate existing data and replicate
    * replicate changes only  

##  AWS Elasticsearch (7:24)
##  [Refresher] Athena (8:52)
##  [DEMO] Athena - Part 1 (14:01)
##  [DEMO] Athena - Part 2 (11:21)
##  Amazon Neptune (6:48)
A graph database. Supports Gremlin and SPARQL
Supports multi-az and up to 15 read replicas
Self healing fault tolerant
Nodes (entities) storing Data and showing Edges (relationships between nodes
Good fit for security, social media, science
##  Amazon Quantum Ledger Database (QLDB) (6:21)
Immutable DB, Serverless, Changes can't be deleted or modified and are verifiable
Supports Amazon Ion documents
Similar to aurora in terms of replication
##  SECTION QUIZ - DATABASES
# DATA ANALYTICS
##  [Refresher] Kinesis Data Streams (10:42)
##  Kinesis Data Firehose - Advanced (9:11)
##  Kinesis Data Analytics - Advanced (9:00)
##  MapReduce 101 (10:24)
##  EMR Architecture (13:51)
##  Redshift Architecture (11:32)
Petabyte scle data warehouse, OLAP (column based), analyze aggregate data<p>
Federated query across different DBs, connects qith Quicksight<p>
Runs on ONE AZ in a VPC<p>
For advanced networking use Enhanced VPC Routing, to have Security Groups NACLs etc like always in VPC<p>
Uses Servers (not serverless)<p>
Leader Node, responsible for the Schema management , and query planning, and aggregation of results sends to Execution Nodes (workers) to execute a query<p>
Dense compute (for high compute) or Dense storage-->RA3  (for high storage)<p>
Distribution styles are: 
1. Even (default - even across slices)
1. Key (identical key values per slice)
1. All (all slices all data)

Redshift spectrum creates tables from data stored in S3 (something like Oracle External Tables). Allows Redshift to use data without storing them to Redshift
##  Redshift Resilience and Recovery (3:40)
Backups
1. Automatic every 8 hours or 5Gb, 1 day retention (up to 35) , incremental
1. Manual snapshots
1. Cross region if configured to copy S3 across regions

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
Significantly improves latency and throughput for read-heavy application workloads
Elasticache consists of:
1. Nodes (where instances of MemCache or Redis run. 1 Node - 1 Instance). Has its own DNS name and Port
2. Redis Shards (grouping of nodes - 1 to 6 nodes)
3. Clusters (1-90 shards if enabled) comprised of the Shards or the Nodes

Memcache is simple, never persisted on Disk, can have 20 Nodes in a single cluster, automatic discovery of nodes in cluster, across AZs
Redis is complex, supports snapshot of data , supports partitioning data across up to 90 shardsm supports replication, supports geospatial data, works across AZs

##  SECTION QUIZ - CACHING, DELIVERY AND EDGE
# MIGRATIONS & EXTENSIONS
##  The 6R's of Cloud Migration (15:45)
To migrate first we **Discover** then **Assess** and then **Prioritize** applications to migrate
Ways to mikrate:
1. Rehost (Lift and Shift) - FOR Minimum effort /  not taking advantage of cloud / TO GAIN IaaS, Easier to Optimize when in AWS - USUALLY USING VM Import/Export + Server Migration Service (SMS)
1. Replatform (Lift and Shift with optimization) - FOR Minimum Effort with Maximum Compatibility and Some Native Cloud. TO GAIN better IaaS without major code changes 
1. Repurchasing (move to something new eg Saas - FOR moving from self managed products to AWS managed products. TO GAIN standardization, cost, risks, admin overhead, operational excellence
1. Refactoring / Rearchitecting (take advantage of cloud) - FOR best results. TO GAIN cheaper, more scalable, better HA/FT, costs aligned with usage 
1. Retire - Do we need this? No? Dump it - FOR cases you don't need it at all
1. Retain (not worth the time/effort to migrate) - FOR cases it is not worth to move or extremely risky Complex legacy applications / hard to test 

##  Virtual Machine Migrations (8:08)
Migrating VMs and applications:
We use the **Application Discovery Service** for DISCOVERY ONLY: a)**Agentless (Connector)** an OVA appliance (Open Virualization Format), integrates with VMWare and creates inventory and resource usage like CPU, limited capabilities of discovery, b)**Agent Based** discovery (within a VM) for full data gathering (network,processes,usage,performance etc), even network communication/dependency among servers
Application Discovery Service can integrate with **AWS migration hub** which tracks migrations within AWS, by providing it the overall architecture of the on premises environment
**SMS (Server Migration Service)** is an Agentless Connector that can migrate whole VM's to AWS of resources discovered by ADS, using Incremental replication of Live Volumes
Server Migration Service supports:
1. VMWare
1. Hyper-V
1. AzureVM

SMS also supports multi-server migrations orchestration
To use it we install a connector (a preconfigured VM) which can interact with the Virtual Server and access the VMs and associated storage, transfers data to S3 within AWS
These S3 data can be converted to AMIs and used to create VMs or EC2, with CFN or other means

##  Database Migration Service (DMS) (11:06)
Migration options
1. Snapshot extraction, import to new instance, replicate using tools (fast, easy, near zero migration downtime)
1. For Homogeneous it is better to use a)Read replica, b)Self managed export/import (engine specific) or other tools. Only for huge data DMS , supports CDC (change data capture) - good for near zero migration downtime
1. For Heterogeneous we do two phases: a)Schema migration (AWS Schema Conversion tool), b)Data migration (Data Migration Service)

DMS is administrative heavy but very strong
DMS can also merge databases. At least one DB should be in AWS
DMS Billing is like EC2 billing. We pay for the Cross AZ and for the Eggress (outgoing) traffic
DMS High Level Steps:
1. Create a Replication Instance on DMS
1. Choose source endpoint for source DB (MySql)
1. Create IAM role to allow data to be added to DynamoDB (service that will use this role==DMS, attach policy )
1. find the arn of the role
1. Create target endpoint
1. Create database migration task in DMS
1. Choose if it should 
    * migrate existing data (full load)
    * migrate existing data and replicate (full load + CDC)
    * replicate changes only (CDC)  

DMS can provide data validation to ensure data were migrated accurately from source to target   . This happens right after a full load completes or as they occur during CDC 
We are able to configure the validation settings and also have access to the tables statistics during validation to understand the progress
Supported sources for DMS:
1. Everything
1. Mongo DB
1. SAP
1. IMB DB2    
1. Azure
1. S3

Supported targets for DMS:
1. Everything
1. Mongo DB
1. Elastic Search
1. Apache Kafka   
Schema Conversion Tool can convert schema between engines, supported for Windows, Fedora, MacOS, Ubuntu

Steps to use SCT are:
1. Download and run installer for OS 
1. Configure JDBC or other driver
1. Create mapping rules
1. Convert the schema
1. Create migration assesment report
1. handle manual conversions
1. update and refresh the converted schema
1. save and apply the converted schema

On top of SCT with it we can use Data Extraction Agents for additional transformation of the source (processing takes place on additional EC2 or snowball Edge)
DMS to migrate data across accounts:
1. Configure VPC peering across VPC of accounts / Acceptor accepts the request
1. Modify Route Tables
1. Modify if needed security groups
1. Create Snapshot on source account
1. Make sure target account has access to KMS key for the snapshot if needed
1. Restore snapshot on target account
1. Configure replication instance on DMS and wait replication lag = 0

If for the above DBs were NOT homogeneous we would need to run SCT first before DMS??
Investigating DMS Tasks:
1. Slow DMS Tasks: Replication instance is underprovisioned / Check RAM,CPU,swap, IOPS / Split tasks (disable Multi AZ, Turn off automatic backups, turn off logging, Limited LOB mode so as to migrate large ones manually)
1. Network issues: Check security groups, source and target have egress, ingress on security group on the database port from the replication instance
1. Account used by DMS may not have access to the Datastore
1. Missing objects. DMS does not migrate secondary indexes or non-primary key constraints. This will have to be done manually using native DB tools
1. CDC (change data capture - replication) stuck after full load: Indexes should be there otherwise full table scan,

DMS is used for a)Modernization, b)Migration and c)Replication purposes
WQF (Workload Qualification Framework) can help visualizing of the timeline of the migration. It is an AMI provided by Amazon Marketplace with SCT preinstalled
Best Practices exist in Playbooks
We use SCT + DMS + Playbooks
We use Multi AZ DMS for HA during replication
DMS uses eventual consistency to replicate (CDC) by monitoring/pushing the transaction logs
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
Snoball edge has on-board storage and compute poer and supports S3 API
Use cases:
1. Bandwidth
1. No access to the target database/storage
Migration Process:
1. AWS SCT extract data locally and move data to an edge device
1. Ship edge device to AWS
1. Edge device automatically loads data to S3 bucket
1. AWS DMS takes the files and migrates to target data store

Files uploaded to Snowball in order to be able to be uploaded to S3 they need to be <5TB. 
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
Glue is a fully managed serverless ETL service (Extract,Transform and Load - like Talend) that helps us organize and format out data for use with e.g. Redshift
AWS Glue can extract data from a source (S3,RDS,JDBC,DynamoDB,Kinesis Data Streams, Apache Kafka), clean it up, transform it and then move it to our desired datastore (e.g. S3, RDS, JDBC, Redshift, Elastic Map Reduce)
AWS Glue Catalog is where we store annotate and share metadata. 
Avoid data silos as the Catalog is shared for the account, per region.
Glue jobs can be triggered manually OR via events using Event Bridge
e.g. Storing data to a Data Lake (e.g. S3) -> Define a Glue Crawler -> Point it to DataStore -> Table Definitions created
e.g. Glue can generate Scala or Python script for transformation
The catalog helps us create and monitor our ETL jobs, to populate the catalog we use our crawler
Glue Data Catalog will contain the following information )metadata):
1. Connections
1. Crawlers
1. Databases
1. Tables
1. ETL Jobs
1. Triggers

Glue Pricing is per DPU (Data Processing Unit - 4VCPU and 16GB RAM)
Glue Jobs:
1. Apache Spark Jobs
1. Streaming ETL Jobs (Spark Streaming)
1. Python Shell 

DataPipelines is what was used before Glue and is not Serverless. Requires instances to run but is similar
##  Device Farm (4:19)



