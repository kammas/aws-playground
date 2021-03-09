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
Permission Boundaries define the maximum permissions an identity can receive - they don't grant any access<p>
Permission Boundaries can be applied to IAM Users or IAM Roles<p>
Resource policies will be applied to full, but Identity permissions will be reduced according to boundaries<p>
Permission Boundaries are used e.g. to administrators so as to have limited capabilities even though they are administrators<p>
Admin Boundary: This is accomplished by e.g  assigning an "allow * on IAM" but use 2 boundaries, 1 to allow to manage password etc only on same user and boundary of specific allowed IAM Actions<p>

**Effective Permissions of a User or Role** are "Permissions Boundaries" INTERSECTION "Identity Based Policy"<p>

**Service Control Policy (SCP)** is a json document (policy) that can be attached to an OR, OU or Account<p>
The policy impacts all children including root user (if he is not the top root)<p>
SCP reduces the account capabilities in total (account boundary)<p>
Provides Allows or Denies. Default is all Allow (which is the same as if there is no SCP)<p>
SCPs are Account Permissions Boundaries and Limit what the account can do<p>

**Effective Permissions of Identities in an account with SCP** are "What is allowed in a SCP" INTERSECTION "Identity Policies in Accounts"<p>


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
**NACLs** are used IN and OUT of a Subnet. (**stateless**) - Rule/Type/Protocol/Port Range/Source/Allow-Deny Inbound/Outbound (e.g 100/All Traffic/Protocol/Port Range/Source/A-D). Usually open for IN X port and for OUT ephemeral ports (1024-65535)<p>
**SGs** are used IN of an Instance or Resource (**statefull**) - Type/Protocol/Port Range/Destination (e.g. All Traffic / Http / 80 / 0.0.0.0/0)<p>
Subnets associate to ONLY 1 Route Table, Either the VPC Main RT or a custom<p>
RT handle differently IPv4 and IPv6<p>
Routes send traffic based on destination (default, network CIDR,IP CIDR) to a target (where it will be sent)<p>
Limit of 50 static routes and 100 dynamic routes<p>

RT Priority:
1. Longest (more specific) Destination wins
2. Static Route
3. Propagated Route
4. DX
5. VPN Static
6. VPN BGP
7. AS Path (via BGP the distance - shortest wins)
**Internet Gateway (IGW):** The Amazon VPC side of a connection to the public Internet.<p>
**NAT Gateway:** A highly available, managed Network Address Translation (NAT) service for your resources in a private subnet to access the Internet.<p>
**Virtual private gateway (VGW):** The Amazon VPC side of a VPN connection.<p>
Reverse Proxy - Ingress Routing<p>
Gateway Route Tables (for VGW or IGW)<p>
The final destination is known only to the GW<p>

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
AWS Region, connected with multiple DX Locations (AWS-Datacenter) by redundant high speed connections<p>
AWS Region <-> AWS DX Router and using a Cross Connect cable, <-> Customer or Provider DX Router <-> Customer Premises Router <p> 
For Resilience we need:
2 AWS DX Routers in the DX Location <-> cross connect 2 Customer DX Routers <-> 2 Customer Premises Routers <p>
(idealy 2 different DX Locations, 2 different Customer premises, 2 different Telco Provider cables)<p>
even beter with 4 AWS DX Routers <-> 4 customer DX routers <-> 4 customer premises routers<p>
##  DX LAGS (5:44)
Direct Connect **Link Aggregation Groups (LAG)** are a way to combine individual direct connects into a faster logical connection (e.g. merge 3x10Gbps to a 30GBps)<p>
They improve managability and speed and are NOT designed for resilience.<p>
They can help only on smaller cables such as cables<p>
LAG == SPEED != RESILIENCE<p>
Maximum 4 connections per LAG, all of the same speed, all terminate in same location<p>
LAG has minimumLinks attribute, which define the minimum connections that should be active for the LAG to be considered as Active<p>
e.g. Total links==4, minimumLinks==2, if  active links are 2-> LAG is Active, if active Links are 1-> LAG is not active<p>
##  Direct Connect Gateway, TGW and Transit VIFS (13:52)
Direct Connect is a regional service, connecting Customer Premises to 1+ DX Locations<p>
Public VIF can access all AWS Public Regions<p>
Private VIFs can access VPCs in the same Region via VGW's (as default - there are workarounds)<p>
Maximum 10 VGW attachments to a DX Gateway<p>
1 DX up to 50 Private VIFs<p>
1 DX Gateway up to 3 TGWs<p>

**Public VIF:**<p>
Router in on premises initially has 0.0.0.0/0 to use Public Internet Connectivity<p>
After Connecting On Prem to DX Location, and enabling BGP, Adress space for public spaces of AES for all regions is advertised via BGP => More specific routes are defined => The routing will prefer the Direct Connect => Higher performance than using Public Internet<p>

**Private VIF:**<p>
**W/O DX Gateway** (if we have only one region):<p>
AWS Region <-> VGW <-> AWS DX Router <-> crossConnect Cable <-> Customer or Provider DX Router <-> Customer Premises Router + Private VIF from On prem to VPC VGW<p>

**With DX Gateway** which is a Global Network Device (to peer-connect to multiple regions - NO TRANSIT - just all VPCs to On Prem):<p>
AWS Region1 VGW <-> DX Gateway <-> AWS Region2 VGW <p>
Region VPC <-> AWS VGW <-> DX Gateway <-> private VIF <-> On Prem Router<p>
On Prem will receive BGP advertisements for all VPCs via the DX Gateway<p>

**With DX Gateway and Transit Gateway** which are both Global Network Devices (for transitive multi region):<p>
AWS Region1  <-> TGW <-> AWS Region2 VGW<p>
DX Gateway1 <-> TGW - Transit VIF <-> DX Gateway2 <p>
Region VPC <-> AWS VGW <-> DX Gateway <-> private VIF <-> On Prem Router<p>
On Prem will receive BGP advertisements for all VPCs via the DX Gateway, that will have receive them via the TGWs<p>

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
We want to create three buckets with different access
1. Public access + from limited VPC subnets. Both from VPC and Internet but from specific subnet only. From VPC we use Gateway Endpoint (automatically adds route with prefix Destination to go to the Endpoint) and lock the subnet we want. Also S3 bucket policy to allow
2. Private access VPC only, specific subnet. From VPC we use Gateway Endpoint and lock the subnet we want. Also combine it with S3 bucket policy to allow the specific arn of the endpoint only
3. Only public not VPC. Endpoint policy prohibits connecting to Bucket from VPC
##  Advanced VPC DNS & DNS Endpoints (15:42)
In VPC the +2 address of the CIDR is reserved for DNS and all VP resources can use it for DNS. e.g. for 10.16.0.0/16 the DNS would be 10.16.0.2<p>
In Subnets the +2 address of the CIDR is also reserved and is called **Route53 Resolver** and provides R53 Public and Associated Private Zones<p>
Route53 Resolver is only accessible from within a VPC (Not from site-to-site VPN or DX) => Hybrid network integration IN and OUT is problematic (AWS-On Prem)<p>
We want On Prem and AWS VPC network to have a common DNS that is not publicly accessible.<p>
On AWS VPC instances will use R53 resolver for Public and Private Zones. And next, the Public DNS. Private DNS is not available between AWS VPC - On Prem (Problem)<p>
**Solution Before R53 Endpoints** was:
1. AWS Side: a)DNS forwarder in EC2 with DHCP options sets, that forwards selectively to a1)On Premises Resolver, a2)otherwise to R53 Resolver otherwise on a3)Public DNS  
2. On Prem side: a)On prem Resolver for private and locally hosted DNS zones  b)anything else to DNS forwarder and then to R53Resolver

**Solution with Route 53 Enpoints**:
Route53 Endpoints are VPC Interfaces (ENIs) so they are accessible over VPN and DX. <p>
They use: <p>
a) Resolver Inbound Enpoints for On Premises -> R53 resolver. Two AWS subnets, two IP addresses, On Prem DNS infrastructure configured to forward queries, for non local DNS<p>
b) Resolver Outbound Endpoints for AWS VPC -> Conditional forwarders on R53Resolver -> Outbound Endpoint -> On-premises DNS<p>
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART1 (8:41)
We are building an advanced DNS solution between On Prem and AWS, that will allow On Prem and AWS to resolve DNS of servers within AWS/On Prem without using a Public DNS<p>
To implement this normally we would be having something like Direct Connect + VPN, but for demo we use VPC peering. Steps are:
1. We create a VPC peering connection 
2. Configure also routing of the Route Tables in both subnets
3. Create Inbound Endpoints (on AWS VPC) from the Route53 service with security group that allows traffic from any source IP on ICMP, and all TCP ports for two AZs and Subnets where the ENIs will be injected. This allows traffic headed to Inbound Endpoints to reach correct destination   
4. On the On Prem DNS servers, we will add the zone of aws, with the Endpoint IPs, on each DNS server. This will forward DNS requests from the On Prem DNS servers, to the Inbound endpoints of AWS.With the help of one ore more Private Hosted Zone (Route53), having A records towards EC2s, we can route traffic using names to the correct IP of AWS instance . On Prem -> DNS1/DNS2 -> Inbound IP1/2->Route53 Private Hosted Zones -> Arecord
5. Next assuming there was a different DNS used by APPS on prem, we will change Apps on prem to use for DNS the two new DNS On Prem Servers. Now all traffic can be routed from On Prem to AWS
6. Next we create on the AWS VPC (again) an Outbound Endpoint from the Route53 service, with same security group as the Inbound Endpoint. This will allow AWS DNS queries of the AWS to identify IPs of On Prem servers. 
7. Also we will create a forward Rule from Route53 for each On Prem domain we want AWS services to use the rule and associate it with the AWS VPC and Outbound Endpoint and also define the On Prem endpoints that should be used as targets in that case (the two IPs of On Prem DNS at port 53). 
8. Now all DNS from AWS EC2 -> Route53Resolver -> Because of the rule goes to Outgoing Endpoint -> These go to On Prem DNS1-2 -> Correct Private IP fetched. DONE
 
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART2 (7:05)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART3 (16:25)
##  [DEMO] Implementing AWS & On-premises Hybrid DNS - PART4 (8:22)
##  Private Link (8:49)
AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network.<p>
Similar to Interface Endpoints but for providing or consuming securely services of AWS or Marketplace or On Premises applications <p>
AZ IDs are the same across accounts (e.g. use-az1)<p>
If we have a VPC Service Provider (that wants to selectively share the service) and a VPC Service Consumer (that wants to consume the service) we do the following:
1. Create an Endpoint Service on VPC Service Provider
2. Create NLB (Network Load Balancer), which creates LB Nodes on each AZ.
3. Permission is granted to IAM Users, Roles, Accounts or Anyone
4. We deploy Interface Endpoints (ENIs) on Consumer VPC AZs subnets (can be protected by SGs and NACLs)

For HA we need to deploy multiple endpoints (1 per AZ on Consumer VPC)
Private Link supports only IPv4 and TCP (not IPv6)
Private DNS is supported => We use two Outbound Endpoints and a Rule, that will point to the DNS servers of the Service
Private Link is supported for DX, Site-to-site VPN, VPC Peering

##  IPv6 Capability in VPCs - PART1 (10:25)
IPV4 is comprised of the following Publicly Routable (most of them):
1. CLASS A (0.x.x.x-127.x.x.x) - Super Large Organizations
2. CLASS B (128.x.x.x-191.x.x.x)
3. CLASS C (192.x.x.x - 223.x.x.x)

Public address is never ever configured on the OS of an EC2. Only private IP is known/configured to the OS<p>
##  IPv6 Capability in VPCs - PART2 (11:04)
IPv6 are publicly routable, NAT not used. AWS provides a /56 range of IPv6 per vpc<p>
same routing logic as IPv4 (dest/target/specific higher priority)<p>
To allow only outgoing Internet Access to IPv6, i use Eggress Only IGW (combined with IGW for IPv4 internet)<p>
IPv6 can be added also after creation of vpc/subnet<p>
not everything in aws supports IPv6 (eg PrivateLink and Interface Endpoints DO NOT)<p>
##  Advanced VPC Structure - How Many AZs ? (11:53)
To calculate the AZs i should use, i subtract from the total AZs, the Buffer AZ (how many we should be able to tolerate going down)-> Nominal AZs (e.g. 6-1=5)<p>
##  Advanced VPC Structure - Subnets & Tiers - PART1 (7:43)
NACL is per subnet. One reason to have more than 1 subnets is if we need to use different EXPLICIT DENIES to IP addresses or set of IP addresses<p>
SGs can be configured to allow connectivity only from specific resources/ENIs (e.g. EC2)<p>
So a DB in a Public subnet could have the followig protection:
1. Not assign public IP
2. Using SG allow connectivity only from an EC2

If we split the APP and DB in different subnets we can add one more extra security Layer - a NACL<p>
Also one more additional security / better design is that we can have different Route Tables for Public subnets and Private Subnets (which is the main reason of multiple subnets)<p>
##  Advanced VPC Structure - Subnets & Tiers - PART2 (14:10)
An internet Facing ALB needs to run from Public Subnets, HOWEVER it can communicate with Private Instances (within private subnets) 
##  SECTION QUIZ - NETWORKING & HYBRID
# STORAGE SERVICES
##  [Refresher] FSx for Windows File Server (11:34)
FSx provides native windows file servers/shares for integration with windows environments using native Directory Service or Self-Managed AD<p>
Single (1 subnet) or Multi AZ (subnets) within a VPC (HA)<p>
Automatic and On-Demand backups<p>
Accessible using VPC,Peering,VPN,DX, supports all windows FS does, windows permission model, de-duplication (sub file), DFS (Distributed file system), KMS at rest, enforced encryption in transit<p>
Protocol is **SMB**, Supports also volume shadow copies (file versioning restored from client side)<p>
Use case to act as the file system of Workspaces <p>
Performance: up to 2Gb/sec, thousand IOPS, <1ms latency<p>

##  [NEW] FSx for Lustre (14:19)
For HPC (ML/BI/Financial Modeling), done using Linux Clients, using **POSIX** **interface**<p>
100Gb/Sec throughput & Sub millisec latency<p>
Deployment Types:
1. Scratch - Highest performance / Short term / NO HA / NO replication
2. Persistent - Lower performance / Long Term / HA / Replication IN ONE AZ ONLY / Self Healing 

Accessible using VPC,Peering,VPN,DX. <p>
Requires HIGH BANDWIDTH<p>
Usually there are EC2 Linux instances (clients) that access the Lustre File system over an ENI that is installed on the subnet (and optionally an S3 bucket)<p>
Depending on the size of Lustre several Lustre File Servers are placed, which are the ones handling the requests. Each has also an in memory cache for frequent files<p>
More storage => More servers => More aggregate throughput =>  More IOPS can be delivered over the ENI<p>
Writes and Reads are not using cache and are dependant on performance characteristics of storage<p>
Reads from cache are dependant on characteristics of ENI 
Backups manual or automatic 0-35 days retention. Unlike other products 0 days means NO AUTOMATIC BACKUP<p>

##  EFS Refresher (12:11)
The Elastic File System (EFS) is a shared file system within AWS based on the Network File System (AWS implementation of **NFS**) (POSIX interface)<p>
It can be mounted on Multiple linux EC2 instances, or on-premises servers as long as private networking exists between that network and AWS.<p>
EBS is block storage (physical storage) while EFS is file storage (hierarchical storage) but seen by instances as if it was connected to the instance<p>
Private Service via mount targets (ENIs) inside a VPC<p>
Accessible using VPC,Peering,VPN,DX. <p>
Also accessible via Lambda if Lambda configured to use VPC networking, great option when there is Lambda temp storage limitation<p>
Officially Linux ONLY<p>
Performance Modes:
1. General Purpose (default)
2. Max IO (can use FSx Lustre though....) 

Throughput Modes:
1. Bursting mode (more random)
2. Provisioned (steady)

Storage Classes support also Lifecycle Policies:
1. Standard 
2. Infrequent Access


##  [DEMO] Implementing EFS - PART1 (9:08)
Create file system -> Customize -> set mount targets (1 per AZ for HA) -> choose AZ/subnet/SG -> After creating i can check it is ready checking EFS/network IPs to see they are available to be mounted. then i add it to linux with<p>
sudo yum -y install amazon-efs-utils<p>
sudo mkdir -p /efs/wp-content  (replacing wp-content)<p>
sudo nano /etc/fstab<p>
file-system-id:/ /efs/wp-content efs _netdev,tls,iam 0 0 (replacing file-system-id with fs-xxxx)<p>

##  [DEMO] Implementing EFS - PART2 (12:52)
##  S3 Object Storage Classes - PART1 (9:23)
S3 standard stores in 3 AZ (11 9s availability) - Price a)GB/m of data stored b)cost for transfer out, c)per 1000 requests - first byte latency can be publicly available<p>
S3 standard IA, difference smaller cost per GB but retrieval fee, minimum duration for 30 days. Should be used for for data not accessed often, important or irreplaceable and large<p>
S3 One zone IA, same as S3 IA, but with smaller cost and no resilience. durability is the same (if AZ does not fail). Should be used for for data not accessed often, replaceable and large<p>


Http 200ok means it is stored succesfully<p>
##  [UPDATE20201110] S3 Object Storage Classes - PART2 (10:02)
**S3 Glacier** can be retrieved a)expedited (5 minutes), b)standard (5 hours), c)bulk (12 hours)<p>
They are moved to IA zone when retrieved. 90 day minimum duration <p>

**S3 Glacier Deep Archive** can be retrieved within 48 hours<p>
180 day minimum duration<p>

**Intelligent Tiering** is monitoring usage of objects and does the move among tiers automatically<p>
Intelligent Tiering has cost /100k objects and consists of:
1. Frequent Access
2. Infrequent Access
3. Archive (90 day minimum)
4. Deep Archive (180 day minimum)

Ideal on Long Lived data when usage pattern changes a lot<p>

##  S3 Lifecycle Configuration (13:05)
**Lifecycle Configuration** is a set of rules, which consist of Transition Actions (among classes) or Expiration Actions (delete objects or versions after X time)<p> 
Can be applied to Buckets or group of objects using tags or prefixes<p>
Smaller objects can be costly<p>
S3 standard needs to stay there 30 days minimum<p>
To transition an object from S3 to S3IA and then S3 Glacier with one rule it has to wait 30 days in standard, then 30 days in IA to go to glacier<p>
BUT if we use two rules we could transition it without waiting 30 days in IA BUT using the billable period (so it can cost)<p>
S3 to Glacier can go with 1 day delay<p>


##  [Refresher] S3 Replication (13:55)
S3 supports Cross Region Replication and Same Region Replication for same accounts or different accounts<p>
Source bucket is configured for the replication, along with an IAM role allowing S3 to assume it (so in its trust policy having S3 service) <p>
This role's permission policy allows it to read objects from the source bucket and replicate objects to the destination bucket<p>

For replication across different accounts the role needs to be trusted by the destination account<p>
To do so we need to add a bucket policy (resource policy) in the destination account to allow the role in the source account, to replicate objects into it<p>

replication can be done for 
1. all objects or a subset using prefix or tags
2. specific storage class (we can override the default and store objects to different-lower class for economy)
3. ownership (default is source account but we can change that to be owned by destination account)

Replication Time Control can guarantee that objects will be replicated within 15 minutes<p>
Replication is not retroactive (applies from that moment onwards) and it is one way<p>
Can replicate unencrypted, SSE-S3 (and also SSE-KMS with additional config)<p>
Bucket owner should have permission to read objects for them to be replicated<p>
Changes on S3 objects due to Lifecycle system events (expiration / moving to Glacier etc) will not be replicated and NO DELETES are replicated<p>

Replication Use Cases
1. SRR - Log aggregation
2. SRR - Prod and Test Sync
3. SRR - Resilience with strict sovereignty
4. CRR - Global Resilience Improvements
5. CRR - Latency Reduction

##  [Refresher] S3 Object Encryption - PART1 (10:08)
Encryption is on an object level not bucket<p>
Client side encryption all is done by client, S3 receives and stores scrambled data<p>
Server side encryption s3 receives unencrypted data and encrypt them and splits as follows:
1. SSE-C (Customer key) - Customer manages keys / S3 manages encryption / S3 storage - s3 receives (object+key), s3 stores (encrypted object+hash of the key)
2. SSE-S3 (S3 Managed Key) - S3 manages keys / S3 manages encryption / S3 storage - s3 receives (object), s3 stores (encrypted object+encrypted key) - not suitable in cases a)need to own the keys, b)need to manage rotation time of keys, c)need not even an S3 Admin to access these
3. SSE-KMS (Customer Master Key stored in KMS) - KMS+S3 manages keys / S3 manages encryption / S3 storage - s3 receives (object+plain text KMS key+encrypted KMS key based on CMK), s3 stores (encrypted object+encrypted key). I can choose a Customer Master Key i create, and choose the permissions on it and rotation and CloudTrail logs call towards that key . Since access to the initial Customer Master Key is needed S3 admins can not decrypt objects.** Customer Master Key decrypts the encrypted key and the decrypted key decrypts the object**

##  [Refresher] S3 Object Encryption - PART2 (11:38)
Encryption: plain text + key + algorithm = cipher text<p>
Decryption: cipher text + key + algorithm = plain text<p>

Default bucket encryption: If x-amz-server-side-encryption header is used when storing object to S3 then server side encryption will be used<p>
If i use AES256 (default) --> SSE-S3, If i use aws:kms SSE-KMS is used<p>
##  [REFRESHER] S3 Presigned URLs (10:57)
Presigned URL's are a feature of S3 which allows the system to generate a URL with access permissions encoded into it, for a specific bucket and object, valid for a certain time period.<p>
The person using an S3 bucket presigned URL acts as the person that generated the presigned URL. Can either download (GET) or upload (PUT)<p>
Presigned URLs are used for a)offload media to S3 or b)serverless applications, c)access objects in private buckets<p>
Presigned URL can be generated by anyone (even someone not having access to the object). This does not mean that access is granted when using it. At the time signed url is used the one that generated it needs to have access for presignedURL to function properly <p>
When url is used permissions of the one accessing it match the permissions the one that generated it<p> 
Don't generate with an IAM role as role's credentials may expire sooner than presigned url. Always i should use long term identities<p> 

##  [UPDATE202101] [DEMO] [Refresher] S3 Presigned URLs (19:12)
Using AWS CLI<p> 
similar to aws s3 presign s3://... --expires-in 180<p> 
we will get a presigned url that is accessible for the next 3 minutes<p> 

##  [Refresher] S3 Select & Glacier Select (5:32)
S3 can store infinite objects smaller than 5TB<p> 
To reduce data usage and time, S3 and Glacier allows me to select using SQL-like statements, to retrieve part of the object, on CSV,JSON,Parquet (Bzip2 for csv,json)<p> 

##  S3 Object Lock (9:56)
Object Lock is either enabled on bucket creation (along with versioning) OR i need to contact AWS support after it is created
Object Lock implements a Write-Once-Read-Many (WORM). NO DELETE, NO OVERWRITE
I can choose any or none of the following, for Bucket default or each object individually:
1. Retention period (in days or years). 
   1. Compliance Mode impact (even by root user)
      1. Object can't be deleted or overwritten for the retention period
      2. Retention period can't be reduced
      3. Retention Mode can't be changed during Retention Period
   2. Governance Mode
      1. Object can't be deleted or overwritten for the retention period
      2. Users with special permissions can bypass the Governance Mode by having a permission (s3:ByPassGovernanveRetention) and specifying a header (x-amz-bypass-governanve-retention:true - is default on console ui)
2. Legal Hold. Set ON or OFF => No Deletes or Changes to object. Only user with s3:PutObjectLegalHold can set it to ON/OFF

##  [UPDATE202102] Amazon Macie (12:04)
Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS. It can discover,monitor and protect data stored in S3 buckets<p>
We enable it and point it to buckets within many AWS accounts, Macie discovers data categorized as PII (personally identifiable information), PHI (Personal Health Information) or financial data.<p>
Using data identifiers (rules that content is assesed against) (managed/built into the product with ML and AI or custom data identifiers - regex based)<p>

Macie's discovery can be integrated with Security Hub or Event Bridge for automatic event driver remediation<p>

We configure a Macie Discovery Job, with a Discovery Schedule, to Detect and Classify N buckets, using managed and custom data identifiers, to produce findings to the console OR generate events to Event Bridge for remdeiation using Lambda<p>

On Custom Data Identifiers, refinements can be applied like keywords, Maximum Match Distance and Ignore Words <p>

Macie produces the following findings:
1. Policy findings: Triggered when changes to an S3 bucket are done that reduce security or provide concerns (after Macie is enabled)
2. Sensitive Data findings: When the following classifications of data are identified: Credentials, Sensitive Data, Medical Data etc

##  EBS and Instance Store Performance - PART1,2 (12:06)
EBS is network block storage, that can be used inside any OS as volumes (boot or data), completely independant to EC2 lifecycle (POSIX interface)<p>
Provisioned in 1 AZ and accessed by that 1 AZ only, can be resized and snapshotted to S3, they are regionally resilient<p>
They are attached to 1 EC2 instance except io1 which can multi attach => Attach to more than 1<p>
EBS follows the EC2 instance if it goes to different host<p>
EBS Volume Type and Size can massively impact performance<p>
Instances has a max storage performance<p>
Instance Store is a pysical disk in an EC2 host<p>
Instance Store Data can be lost in the following cases:
1. Hardware Failure
2. Instance move to different EC2 host after a STOP and START of EC2
   
Instance store can't be resized as it is a physical disk, has the highest performance though (IOPS and MB/s) of anything that can connect to EC2 (locally connected)<p>   
Instance Stored can be striped - Raid0 for high performance OR RAID1 for mirroring<p>

Volumes:
1. HDD based Volumes for large streaming workloads (cost/throughput optimized => Bits per second) - NOT FOR BOOT VOLUMES, BAD for (high IOPS, Low Latency)
   1. st1, frequently accessed, throughput optimized (t for throughput - 40MiB/s/TiB - 500MiB/s/TiB Max - **500 Max IOPS**)
   2. sc1, infrequently accessed, (c for coal - 12MiB/s/TiB - 250MiB/s/TiB Max - **250 Max IOPS**)
2. SSD based Volumes for transactional workloads which involve frequent read/write operations / small bits of data (performance/IOPS optimized => Operations per second)
   1. gp2, general performance, (1GiB-16TiB, **16000 Max IOPS** - 3 IOPS per GiB - min 100 IOPS) - IOPS linked to size
   2. io1/io2, (4GiB-16TiB, **64000 Max IOPS**, 50 or 500 per GiB) - best for DBs SQL and NoSQL
Instance Store: i3 ULTIMATE PERFORMANCE (1.6Million - 2million IOPS!!!)<p>
I can create striped volumes (**Raid0**->double performance) which means i can make **2*64K->128K IOPS**<p>
Also i can create mirrored volumes (**Raid1**->double resilience) which means i can make **2*64K->64K 2x resilience**<p>
**EC2 Max** Instance Limit though is **160K IOPS**. So this is the maximum ever EC2 can use<p>
For more than 160000 IOPS use Instance Store<p>
##  SECTION QUIZ - STORAGE SERVICES
# COMPUTE, SCALING & LOAD BALANCING
##  [NEW] Regional and Global AWS Architecture (11:04)
Netflix Global Application, Comprised of smaller Regional applications<p>

Three main Architectures:
1. Small scale, One Region - One Country
2. One Region One Country but with DR Requirements across Regions
3. Across Multiple Regions

Global Elements:
1. Global DNS using R53 for service discovery / Regional based Healths and Request Routing
2. Cache content Globally on CDN Layer Cloudfront reading from Origin, as close to end users as possible

Region Elements:
1. ELB or API GW to route accoridngly (Web tier)
2. EC2,Lambda,Containers (Compute Tier) - using Store Services (S3,EFC)
3. RDS/Aurora/DynamoDB (DB Tier) combined with caching (DAX,Elasticache)
4. App Services (SQS,SNS,Kinesis) 

##  [NEW] EC2 Purchase Options - PART1,2 (9:26)
EC2 Purchase Options:
1. On Demand - Default, no interruption, no capacity reservation, predictable pricing, no upfront cost, no discount, short term unknown workloads. I can also use On-demand capacity reservations for X time, to make sure i will own EC2 at that time -> will pay this regardless of usage
2. Spot - I pay the spot price even if my max is higher, for non time critical, things that can rerun, cost sensitive, anything stateless
3. Reserved - Longterm consistent usage, reservation to an AZ or Region, in AZ reserves capacity, in Region does not reserve but benefits launches in Region,partial benefit launching a larger than reserved
   1.  no upfront, 1-3 years,
   2.  partial upfront, 1-3 years,
   3.  all upfront (standard reserved), 1-3 years,
   4.  scheduled reserved, not for all types and regions, minimum 1200 hours/year, minimum 1 year
4. Dedicated Instances - Hardware is not shared with other AWS customers, but i do not own the host, extra charges for instances (really strict requirements)
5. Dedicated Host - Paying for full host, for licensed software based on resources, host affinity -> instances remain on the same host supported, no instance charges, capacity management required

##  Reserved Instances - the rest (11:58)
EC2 Delivery Order Capacity
1. Reserved
2. On Demand
3. Spot

Classes:
1. General Purpose
   1. Mac - macOS
   2. T4 (support Nitro) 40% better than T3
   3. T3 (support Nitro) 30% better than T2
2. Compute (C)
3. C6 (compute optimize)
4. Memory Optimized (R, X)
5. Accelerated Computing GPU (P,I,G)
6. Storage Optimize (I,D)

EC2 Savings Plan
1. EC2 Instance Savings Plans (specific size, specific hours per year, specific AZ or Region) (flexible size, OS, tenancy)
2. Compute Savings Plans (flexible instance family, region, OS, tenancy, compute options)
Beyond the commitment (e.g. 20$ per hour) On Demand is used

##  EC2 Networking (16:21)
Any EC2 when launched are added a Primary ENI. This is removed when server is stopped. A Secondary ENI can be added to the EC2 ON THE SAME AZ BUT ON ANY SUBNET<p>
Secondary ENI can be detached and attached to other EC2s. Also SGs are associate to an ENI not an EC2<p>
Essentially we can have for an EC2 a Private Interface on Private Subnet for Management and a Public Interface on Public Subnet for Internet<p>
Additionally we can protect the subnets with NACLs. ENIs have 1 Mac Address, N IPv6 Addresses, N SGs. IPv6 if enabled they are routable, and they are accessible on OS<p>
Private IPv4 addresses of Primary or Secondary Instance (can have multiple private IPs for secondary - depending on EC2 size) are visible to the OS<p>
Public IPv4 address,not visible to the OS,temporary for EC2 Lifecycle, is assigned to the Primary Interface of an EC2 Instance if:
1. EC2 is launched in Subnet configured to allocate Public IPv4 addresses
2. EC2 is launched with a Public IPv4 address

**EIP (Elastic IP)** are allocated to the AWS account and are **associated with an EC2 Instance <--> its Primary ENI** and the non-elastic IP is released forever<p>
EIPs are chargeable regardless if they are attached or not, to a running Instance or not<p>
 
For each Instance having Multiple ENIs and multiple SGs, the traffic is evaluated against all SGs and if allowed it reaches EC2 <p>
Each ENI does a SRC/DST check -> drops packets if the SRC or DST isn't ON that ENI. This needs to be disabled in cases like NAT instances (so disabling it on the Primary Interface of the NAT ENI) <p>
If License is based on Mac address, i should use a secondary ENI to bind its MAC with the license and if i need to migrate it, will detach and attach it to the new EC2<p>

##  [NEW] Bootstrapping vs AMI Baking (17:09)
Ready for Service or Complete: Means Users can use the Service as intended
In general we want to provide the maximum flexibility but also the maximum deployment speed, to allow the App Configuration to be a separate stage/step than the Base Dependencies / Application / Application Updates => <p>
Best option is to do the following:
1. Provision a base EC2
2. Perform the time consuming part of the APP install
3. Create an AMI
4. For new installations Customize AMI at launch time using User Data

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

## [AdvancedDemo] Architecture Evolution - STAGE1 - PART1 (13:06) 

##  EC2 Placement Groups (14:29)
When you launch a new EC2 instance, the EC2 service attempts to place the instance in such a way that all of your instances are spread out across underlying hardware to minimize correlated failures. You can use placement groups to influence the placement of a group of interdependent instances to meet the needs of your workload.<p> Depending on the type of workload, you can create a placement group using one of the following placement strategies:
1. Cluster (best network performance) – packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC applications. Launching ALL at the same time is preferrable (10Gbps vs 5 Gbps). ALWAYS ENHANCED NETWORKING. ONE AZ ONLY. Ideally same VPC and same Instance Type
2. Spread (maximum non-scalable availability and resilience) – strictly places a small group of instances across distinct underlying hardware to reduce correlated failures. MULTIPLE AZs, Each EC2 is on a different Rack (different network and power source), Limit of 7 Instances per AZ => 6*7=42 Instances Max. DEDICATED HOSTS OR INSTANCES NOT SUPPORTED. Use Case small number of critical instances that need to be kept separated from each other
3. Partition (best scalable availability and resilience) – Like Spread but using N instances instead of 1. Spreads your instances across logical partitions such that groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions. This strategy is typically used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka. MULTIPLE AZs, Each **GROUP OF EC2/Partition** is on a different Rack (different network and power source), Limit of 7 GROUP OF EC2/PARTITION per AZ => 6*7=42 GROUP OF Instances Max. DEDICATED HOSTS OR INSTANCES NOT SUPPORTED.

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
Cloudwatch logs are sent to the Region they were generated otherwise us-east-1 if service is global<p>
**Log stream** is a sequence of Log Events that share the same source<p>
**Log Group** is a group of Log Streams that share the same retention,monitoring and access control settings<p>
**Metric Filter** can keep looking for specific pattern to result in a **Metric** that can generate alarm, which can trigger events<p>
Exporting logs from Cloudwatch to S3 can take up to 12 hours (not real time) and the encryption will be done wih SSE-S3<p>
**Subscription Filters** can be used to trigger lambda function based on incoming logs from log groups, or merge data in Kinesis Data Stream or other solutions<p>
For near-realtime storage of logs Kinesis Firehose can be used as the destination of Subscription Filters, and for realtime to Lambda or Kinesis Streams<p>
For generating a cloud watch Metric a Metric Filter can be used<p>
##  [Refresher] CloudTrail Refresher (14:10)
CloudTrail Is a product which logs API calls and account events as a Cloud Trail Event and is REGION SPECIFIC BUT A TRAIL CAN BE SET ALSO TO APPLY TO ALL REGIONS<p>
Global Services log to us-east-1 (Global Service Events)<p>
It's very often used to diagnose security or performance issues, or to provide quality account level traceability.<p>
It is enabled by default in AWS accounts and logs free information with a 90 day retention.<p>
It can be configured to store data indefinitely in S3 or CloudWatch Logs.<p>
To customize the service i can create 1 or more Trails that will be logging Management Event (management operations or such as creating VPC, terminating EC3 ) and/or Data Events (Resource Operations ON A RESOURCE such as Trigger of a Lambda, S3 object was accessed etc)<p>
CloudTrail generated logs can be stored as compressed json files to S3 and parsed by any tooling able to read JSON files and/or to CloudWatch logs to Search or take actions based on Metric Filters<p>
Organizational Trail can also be created from the master account of the organization, logging for all Accounts of the Organization to a single point.<p>
CloudTrail is NOT REAL TIME. Approximately 15 minutes delay max.<p>
To configure a Trail we will also need an IAM Role to allow Cloud Trail to send data to CloudWatch<p>

##  [DEMO] Setting up an Organisational Trail (17:53)
When asking to create trail and store data on a new S3 bucket the bucket policy is modifies accordingly to allow access from CloudTrail to S3 bucket<p>
##  AWS X-Ray (6:42)
AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. <p>
With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. <p>
X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components.<p>
A Tracing header is generated by the first service and it is passed along to other services to show the session flow (distributed tracing)<p>
Segments (trace info such as IP, host, request,response,browser, start and end times etc) are send to XRAY<p>
Subsegments are more granular data of the above, calls to other endpoints etc<p>
Service Graps is generated using the above which is a JSON document describing how all the services and resources work together<p>
XRay console uses the Service Graph + the data collected to generate a Service Map (visual representation of the Service Graph)<p>
Accessing XRAY app--> Tracing Header generated ->Segment is generated-> next service etc<p>
Service map shows the Flow through a Distributed app, Response time, Requests and any errors or issues<p>
To enable X-Ray:
1. For EC2 - install X-Ray Agent
2. For ECS - Install X-Ray Agent in tasks
3. For Lambda - Enable Option
4. Beanstalk - Agent is preinstalled
5. API Gateway - per stage option
6. SNS & SQS can be used as well
7. IAM Permissions (e.g. Lambda execution role is provided with the permissions required to send data to X-Ray )

##  Cost Allocation Tags (4:43)
Has to be enabled per Account or Org Master Account for Organizations<p>
Tag Categories:
1. AWS-Generated (like aws:createdBy)
2. User-Defined (user:something)

Tags are added to resources IF ENABLED AT THE TIME. NOT RETROACTIVELY<p>
Tags can be used as filters in cost reports, to understand users that created by users/departments etc<p>
##  Trusted Advisor (8:35)
**Trusted Advisor** is a tool that provides real time guidance regarding best practices in relation to your resources with topics such as:
1. cost
2. security / MFA / security groups
3. fault tolerance
4. performance
5. over provisioned resources 
6. service limits etc

Works in Account Level, does not need agents to be installed, comes in three versions   
1. Free (7 core checks) - 
   1. S3 Bucket Permissions
   2. Security Groups Unrestricted access
   3. IAM use (at least 1 IAM user)
   4. MFA on root account
   5. EBS Public Snapshots
   6. RDS Public Snapshots
   7. 50 service Limit checks
2. Business Plan / Enterprise Plan
   1. +115 further checks
   2. Access via AWS Support API
   3. CloudWatch Integration
3. Enterprise Plan
   1. +Better response time


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
Autoscaling, self-healing cluster volume storage, Cross Region Replication, Multi master, global database
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
Multi Master: Supported by MSQL only
Global: Supported by many engines. Replication is done by AWS storage infrastructure (physical replication)
Cross Region Replicas: With Engine's specific way, changes are pushed to replicas on a different region (logical replication)
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
ElasticSearch is a managed implementation of Elastic Search. (ELK=Elastic Search for Search and Indexing, Kibana for Visualization and Dashboards, Logstash for Centralized Logging like CloudWatch, Logstash Agent is needed to be installed on EC2)<p>
I will use it if 
1.  I have an existing and want to migrate to AWS
2.  An ElasticSearch requirement

**It is not serverless. Servers are Injected to VPC**<p>

Use Cases (collect data to be used asap from Data Scientists):
1. Log Analytics
2. Monitoring
3. Security Analytics
4. Full text search
5. Clickstream analytics


##  [Refresher] Athena (8:52)
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the data consumed on the queries that you run.<p>

Athena is easy to use. Simply point to your data in Amazon S3, define the schema, and start querying using standard SQL. Most results are delivered within seconds. <p>
With Athena, there’s no need for complex ETL jobs to prepare your data for analysis. <p>

Athena uses "schema-on-read" which is similar to Oracle's EXTERNAL TABLES<p>
So Athena makes a select based on the SQL query defined, using as data structure the schema defined (external table definition), in this way data are transformed on the fly and can be provided also to other services as such
Source Data (e.g. S3 XML,JSON, AVRO, Parquet, ORC, Apache, CloudTrail, VPC Flow Logs) -> Read based on schema -> On the Fly Transformation and select (data are streamed ) <p>


##  [DEMO] Athena - Part 1 (14:01)
##  [DEMO] Athena - Part 2 (11:21)
##  Amazon Neptune (6:48)
A graph database. Supports Gremlin and SPARQL<p>
Supports multi-az and up to 15 read replicas<p>
Self healing fault tolerant<p>
Nodes (entities) storing Data and showing Edges (relationships between nodes<p>
Good fit for security, social media, science<p>
##  Amazon Quantum Ledger Database (QLDB) (6:21)
Immutable DB, Serverless, Changes can't be deleted or modified and are verifiable<p>
Supports Amazon Ion documents<p>
Similar to aurora in terms of replication<p>
##  SECTION QUIZ - DATABASES
# DATA ANALYTICS
##  [Refresher] Kinesis Data Streams (10:42)
Kinesis data streams are a real time streaming service within AWS designed to ingest large quantities of data and allow access to that data for consumers.<p>
Streams can scale from low throughput to near infinite data rates<p>
Public Service and Highly Available by Design, is great for Analytics and Dashboards<p>
Streams Store a 24-hour moving window of data, with a maximum of 7 days<p>
Scaling is achieved by shards added as we want higher performance<p>
1 Shard provides 1MB Ingestion and 2MB Consumption using Kinesis Data Records (1MB). These are spread into the shards of the stream <p>

SQS -> asynchronous communication, decoupling, worker pools, no window, 1 consumption group<p>
Kinesis -> Huge Scale Ingestion of Data, multiple consumers, rolling window<p>
##  Kinesis Data Firehose - Advanced (9:11)
Kinesis Data Firehose is a stream based delivery service capable of delivering high throughput streaming data to supported destinations in near realtime (60 sec).<p>
Fully serverless managed service, which allows the load of data to data lakes, data stored, analytics services, scaling automatically, resilient<p>
Can transform data using lambda
Billing is based on data passing through firehose
Delivering data to:
1. Splunk
2. Redshift
3. Elastic Search
4. S3

Minimum 1MB Fill or 60 second interval before delivering data received<p>
Firehose send directly data to destinations with the exception of Reshift that adds the data in an intermediate data before reading them<p>
##  Kinesis Data Analytics - Advanced (9:00)
Amazon Kinesis Data Analytics is the easiest way to analyze streaming data, gain actionable insights, and respond to your business and customer needs in real time.<p>
Uses Structured Query Language (SQL) and ingests from Kinesis Data Streams or FIrehose<p>
Kinedis Analytics Application can read input streams, combine them optionally with static data and produce output streams and error streams with the realtime processing output<p>
Scenarios for Kinesis Analytics:
1. Time series analytics (elections/e-sports)
2. Real time dashboards (leaderboards for games)
3. Real time metrics (Security and Response teams)

##  MapReduce 101 (10:24)
Map Reduce is a Data Analysis Architecture which allows for the huge scale, parallel processing<p>
Phases:
1. MAP: Data separated to splits. Each Split assigned to a mapper which are the main compute (e.g. count Key/Value, then Shuffle based on Keys). If the processing of a split fails, it can be retried. 
2. REDUCE: When all splits are processed, data can be recombined into Results (count per Key)-> Final Output Data

Hadoop File System (HDFS), Highly Fault tolerant, replicated storage between nodes<p>
Name Node provides the namespace for file system and controls access to HDFS<p>
Block is a segment of data on HDFS (64MB)<p>
##  EMR Architecture (13:51)
Amazon EMR is a managed implementation of Apache Hadoop for handling big data workloads using the Map Reduce framework<p>
Benefit of EMR is that it can be used both long term or for ad-hoc transient clusters<p>
Runs in one AZ in a VPC using EC2 for compute <p>
EMR can use and auto scale: Spot Instances, Instance Fleet, Reserved, On-demand<p>
Used for Big-data processing, analytics, transformation and more (used also by data pipeline product)<p>
EMR Cluster Reads and Writes data to S3<p>
EMRFS is a resilient file system supported natively within EMR, backed by S3, resilient to Core Node Failure. <p>

Every cluster has:
1. 1 Master Node. This node manages cluster and its health. Distributes workloads and ascts as the NAME node within MapReduce. Allows to SSH to the cluster. 
2. 0-N Core Nodes. They act as data nodes for HDFS based on local storage volumes  - used for extreme levels of IO -  (or EMRFS), run task trackers and run mapping and reduce tasks in the cluster. Need to be as stable as possible 
3. 0-M Task Nodes. They have no HDFS invovement and just run the tasks. Ideal for **SPOT** based scaling



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
Managed compute service for large scale data analytics and processing<p>
Used for jobs that can run without end user interaction or can be scheduled to run as resources permit<p>
Handles the underlying compute and orchestration<p>
Batch Components:
1. AWS Batch Job - A script, executable or docker container that will be run and can also be dependant on other jobs
2. Job Definition - Metadata for a Job (IAM permissions, Resource Config, Mount Points)
3. Job Queue - Jobs are submitted to a queue where they wait for comput environment capacity. Queues are associated with 1+ compute environments
4. Compute Environment Managed or Unmanaged - Configure instance type/size, vCPU amount,spot price or provide details of a compute environment i manage (ECS)

In general AWS Batch deployment in our VPC -> Add a Job and Job Definitions -> jobs are submitted to queues having different priorities -> Resources are used processing the jobs based on priority and availability<p>
Batch vs Lambda
1. Infinite vs 15m max time
2. Space unlimited (EBS) vs 512mb (for public lambda)
3. Space unlimited (EBS) vs unlimited EFS (for VPC networking Private Lambda)
4. Docker vs few programming languages
5. not serverless vs serverless
6. no time limit 

Managed vs Unmanaged 
1. Choose On-Demand, Spot Instances size/type, max spot price vs i manage everything

##  AWS Quicksight (4:08)
Quicksight is a tool used for Business Analysis and Business Intelligence, that provides Ad-Hoc analysis and Visualizations<p>
Connect Quicksight to data sources -> Transform Data -> Prepare Analysis -> Decide
Sources can be
1. Athena
2. Aurora
3. Redshift
4. Redshift Spectrum
5. S3
6. AWS IOT
7. Jira
8. Github
9. Twitter
10. Salesforce
11. MSSql Server
12. MySQL
13. Postgre
14. Spark
15. Snowflake
16. Presto
17. Terradata

##  SECTION QUIZ - DATA ANALYTICS
# APP SERVICES, CONTAINERS & SERVERLESS
##  [Refresher] Introduction to containers (17:13)
Images contain readonly layers, changes are layered onto the image using a differential architecture<p>
Dockerfile is used to build docker images. Each step creates fs layers<p>
Docker container is a Docker Image + a R/W Layer<p>
Container images are Portable, self contained, always run as expected<p>
Lightweight -Parent OS used, fs layers are shared<p>
Container only runs the application and environment it needs<p>
Provides much of the isolation VMs do<p>
Ports are exposed to the host and beyond<p>
Application stacks can be multi container<p>
##  [DEMO] [Refresher] Creating a Container Image (17:25)
##  [Refresher] ECS - Concepts (10:25)
ECS is to Containers, EC2 is to Virtual Machines<p>
ECS uses clusters running in the following modes:
1. EC2 mode (EC2 instances as Container Hosts)
2. Fargate mode (serverless way of running docker containers)

We create clusters using ECS as follows -> Create a container definition (telling ECS where the container is, DockerHub,ECR etc and also configuration such as port exposed to host) -> Create a task definition (self contained application - which means it can be comprised from many containers - e.g. an App Container, a DB container etc)<p>
Container Definition -> Pointer to where the container is stored / port exposed<p>
Task Definition -> all the rest (CPU,Memory, Compatibility Mode[EC2/Fargate] , Network Mode, **Task Role the Role the Containers can assume temporarily**)<p>
A Task can include 1-N Containers<p>
A lot of Tasks can include 1 Container<p>

ECS Service, is a configuration how many copies we want of which Task to run (adds capacity and resilience)<p>
ECS Services are deployed into Cluster<p>

##  [Refresher] ECS - Cluster Types (13:30)
EC2 and Fargate Mode Management components:
1. Scheduling 
2. Orchestration
3. ClusterManager
4. PlacementEngine

EC2 Mode -> EC2 instances run containers -> ASG controls size
Fargate Mode -> Containers are running in Fargate Shared Infrastructure

While in EC2 mode the containers are within your VPC, in Fargate mode ENIs are injected to my VPC and connectivity is done through them, it can also have Public Internet access if VPC is configured as such

EC2 mode for:
1. Large workload
2. Price conscious (with reserved pricing combined)

Fargate mode for:
1. Overhead (admin) conscious
2. Small/Burst workloads
3. Batch/Periodic workloads

##  [DEMO][Refresher] - Deploying 'container of cats' using Fargate (16:08)
Create Cluster / Create Task Definition / Add Container / Run Task of Cluster / Deregister Task Definition / Delete Cluster

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
Significantly improves latency and throughput for read-heavy application workloads<p>
Elasticache consists of:
1. Nodes (where instances of MemCache or Redis run. 1 Node - 1 Instance). Has its own DNS name and Port
2. Redis Shards (grouping of nodes - 1 to 6 nodes)
3. Clusters (1-90 shards if enabled) comprised of the Shards or the Nodes

Memcache is simple, never persisted on Disk, can have 20 Nodes in a single cluster, automatic discovery of nodes in cluster, across AZs<p>
Redis is complex, supports snapshot of data , supports partitioning data across up to 90 shardsm supports replication, supports geospatial data, works across AZs<p>

##  SECTION QUIZ - CACHING, DELIVERY AND EDGE
# MIGRATIONS & EXTENSIONS
##  The 6R's of Cloud Migration (15:45)
To migrate first we **Discover** then **Assess** and then **Prioritize** applications to migrate<p>
Ways to migrate:
1. Rehost (Lift and Shift) - FOR Minimum effort /  not taking advantage of cloud / TO GAIN IaaS, Easier to Optimize when in AWS - USUALLY USING VM Import/Export + Server Migration Service (SMS)
1. Replatform (Lift and Shift with optimization) - FOR Minimum Effort with Maximum Compatibility and Some Native Cloud. TO GAIN better IaaS without major code changes 
1. Repurchasing (move to something new eg Saas - FOR moving from self managed products to AWS managed products. TO GAIN standardization, cost, risks, admin overhead, operational excellence
1. Refactoring / Rearchitecting (take advantage of cloud) - FOR best results. TO GAIN cheaper, more scalable, better HA/FT, costs aligned with usage 
1. Retire - Do we need this? No? Dump it - FOR cases you don't need it at all
1. Retain (not worth the time/effort to migrate) - FOR cases it is not worth to move or extremely risky Complex legacy applications / hard to test 

##  Virtual Machine Migrations (8:08)
Migrating VMs and applications:<p>
We use the **Application Discovery Service** for DISCOVERY ONLY: a)**Agentless (Connector)** an OVA appliance (Open Virualization Format), integrates with VMWare and creates inventory and resource usage like CPU, limited capabilities of discovery, b)**Agent Based** discovery (within a VM) for full data gathering (network,processes,usage,performance etc), even network communication/dependency among servers<p>
Application Discovery Service can integrate with **AWS migration hub** which tracks migrations within AWS, by providing it the overall architecture of the on premises environment<p>
**SMS (Server Migration Service)** is an Agentless Connector that can migrate whole VM's to AWS of resources discovered by ADS, using Incremental replication of Live Volumes<p>
Server Migration Service supports:
1. VMWare
1. Hyper-V
1. AzureVM

SMS also supports multi-server migrations orchestration<p>
To use it we install a connector (a preconfigured VM) which can interact with the Virtual Server and access the VMs and associated storage, transfers data to S3 within AWS
These S3 data can be converted to AMIs and used to create VMs or EC2, with CFN or other means<p>

##  Database Migration Service (DMS) (11:06)
Migration options
1. Snapshot extraction, import to new instance, replicate using tools (fast, easy, near zero migration downtime)
1. For Homogeneous it is better to use a)Read replica, b)Self managed export/import (engine specific) or other tools. Only for huge data DMS , supports CDC (change data capture) - good for near zero migration downtime
1. For Heterogeneous we do two phases: a)Schema migration (AWS Schema Conversion tool), b)Data migration (Data Migration Service)

DMS is administrative heavy but very strong<p>
DMS can also merge databases. At least one DB should be in AWS<p>
DMS Billing is like EC2 billing. We pay for the Cross AZ and for the Eggress (outgoing) traffic<p>
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

DMS can provide data validation to ensure data were migrated accurately from source to target   . This happens right after a full load completes or as they occur during CDC <p>
We are able to configure the validation settings and also have access to the tables statistics during validation to understand the progress<p>
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


Schema Conversion Tool can convert schema between engines, supported for Windows, Fedora, MacOS, Ubuntu<p>

Steps to use SCT are:
1. Download and run installer for OS 
2. Configure JDBC or other driver
3. Create mapping rules
4. Convert the schema
5. Create migration assesment report
6. handle manual conversions
7. update and refresh the converted schema
8. save and apply the converted schema

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

DMS is used for a)Modernization, b)Migration and c)Replication purposes<p>
WQF (Workload Qualification Framework) can help visualizing of the timeline of the migration. It is an AMI provided by Amazon Marketplace with SCT preinstalled<p>
Best Practices exist in Playbooks<p>
We use SCT + DMS + Playbooks<p>
We use Multi AZ DMS for HA during replication<p>
DMS uses eventual consistency to replicate (CDC) by monitoring/pushing the transaction logs<p>
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
Snoball edge has on-board storage and compute poer and supports S3 API<p>
Use cases:
1. Bandwidth
1. No access to the target database/storage
Migration Process:
1. AWS SCT extract data locally and move data to an edge device
1. Ship edge device to AWS
1. Edge device automatically loads data to S3 bucket
1. AWS DMS takes the files and migrates to target data store

Files uploaded to Snowball in order to be able to be uploaded to S3 they need to be <5TB. <p>
##  [Refresher] AWS Datasync (9:27)
##  SECTION QUIZ - MIGRATIONS & EXTENSIONS
# DEPLOYMENT & MANAGEMENT
##  [Refresher] CloudFormation Refresher (10:55)
Importing Stacks and not hardcoding ARN ensures a deletion of an imported stack does not leave the stack orphan. Prefer it over hardcoded ARN<p>
cfn-init (try to reach specific end states - unlike bootstrap that runs script)<p>
cfn-signal can provide accurately if the creation has indeed been completed<p>
cfn-hup to monitor for N time after cfn-init, for changes/actions<p>
logs of cfn-init and similar are under var/log on Ubuntu<p>
AWS SAM, i can write on YAML/JSON and also test locally. Supports native transformation<p>
AWS CDK, i can write on javascript/typescript/python/java/.net. Reusability. Supports native transformation<p>
##  CloudFormation Custom Resources-PART1-THEORY (11:43)
##  CloudFormation Custom Resources-PART2-DEMO (11:35)
##  CloudFormation Nested Stacks (14:17)
##  CloudFormation Cross-Stack References (10:06)
##  CloudFormation Stack Sets-PART1-THEORY (9:21)
##  CloudFormation Stack Sets-PART2-DEMO (9:55)
##  CloudFormation Stack Roles (6:52)
##  Service Catalog (7:25)
##  CI/CD using AWS Code* (15:29)
CODE - BUILD - TEST - DEPLOY
CodeCommit - Code Build (+test) - Code Deploy
Development Pipeline orchstrates these tools easilly
Pipeline is for ONE AND ONLY ONE branch
buildspec.yml or .json (Used frode Build to build and test)
appspec.yml or .json (Used from the CodeDeploy to deploy)
CodeDeploy can deploy to:
1. Using one or more DOne or more EC2 using deployment group
2. Elastic Beanstalk or AWS OptsWorks
3. AWS Cloudformation
4. ECS or ECS (Blue/Green())
5. Service Catalogs
6. Alexa Skills Kit
7. S3

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
AWS Shield provides protection against DDoS Attacks (blocks service from legitimate users by overloading system)
**Shield Standard** is Free with **Route 53 and Cloudfront** and protects against Layr 3 and Layr 4 attacks
**Shield Advanced** provides protection to **EC2, ELB, Global Accelerator, Route 53 and CloudFront** and DDoS Response Team and Financial Insurance
WAF (Web application Firewall) is a Layer 7 protection so understands Http and Https, Like SQL Injection , Cross site scripting, Geo Blocking, Rate Awareness
WEBACL (Web Access Control List) of **WAF** is integrated with **ALB, API Gateway and CloudFront**
Rules are added to WEBACL and are evaluated when traffic arrives
Route 53 with Shield -> CF with Shield -> CF with WAF rules - WEBACL filters traffic - ALB Shield and WAF -> EC2 to ASG



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
Glue is a fully managed serverless ETL service (Extract,Transform and Load - like Talend) that helps us organize and format out data for use with e.g. Redshift<p>
AWS Glue can extract data from a source (S3,RDS,JDBC,DynamoDB,Kinesis Data Streams, Apache Kafka), clean it up, transform it and then move it to our desired datastore (e.g. S3, RDS, JDBC, Redshift, Elastic Map Reduce)<p>
AWS Glue Catalog is where we store annotate and share metadata. <p>
Avoid data silos as the Catalog is shared for the account, per region.<p>
Glue jobs can be triggered manually OR via events using Event Bridge<p>
e.g. Storing data to a Data Lake (e.g. S3) -> Define a Glue Crawler -> Point it to DataStore -> Table Definitions created<p>
e.g. Glue can generate Scala or Python script for transformation<p>
The catalog helps us create and monitor our ETL jobs, to populate the catalog we use our crawler<p>
Glue Data Catalog will contain the following information )metadata):
1. Connections
1. Crawlers
1. Databases
1. Tables
1. ETL Jobs
1. Triggers

Glue Pricing is per DPU (Data Processing Unit - 4VCPU and 16GB RAM)<p>
Glue Jobs:
1. Apache Spark Jobs
1. Streaming ETL Jobs (Spark Streaming)
1. Python Shell 

DataPipelines is what was used before Glue and is not Serverless. Requires instances to run but is similar<p>
##  Device Farm (4:19)