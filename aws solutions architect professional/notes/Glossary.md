KEY	EXPLANATION
Resources	User,Group,Role,Policy,Identity Providers stored in IAM - What is stored in IAM
Identities	Users,Groups,Roles - What identifies and groups
Entities	IAM users, Federated Users, Assumed IAM Roles - What authenticates 
Principals	Person or Application - What uses an IAM user or IAM role or root to sign in and make requests to AWS
Authentication	Principal must be authenticated. A)root - via email/pass, b)IAM user, accountID or alias/username/password, c)API or CLI access key /secret key +
Authorization	Request context is checked for policies that apply to the request, to determine allow or deny. Permission policies: Identity-based policies for own account / Resource based policies for cross account
Identity-based Policies	A)Managed Policies, A1)AWS Managed Policies, A2)Customer Managed Policies, B)Inline Policies
Resource-based Policies	Inline Policies
Account Root user	The root user account. This is not the management account (unless it is the top level/first account ever)
Organization Policy Types	1)SCP, 2)Backup, 3)AI Optout, 4)Tagging
SAML 2.0 Identity Federation	An open standard that allows to indirectly use on-premises IDs of a SAML2.0 compatible Identity Provider like MS AD, with AWS (console and CLI), using IAM roles and AWS temp credentials
Service Quotas/Limits Organization Template	Preconfigued limits we want to request changes from AWS team for new Accounts. 
RAM Resource Access Manager	Share Resources across accounts (resource share request/acceptance)
Participant Accounts	The accounts with whom a resource has been shared by another account. Can reference items but not change them (like read only access) 
Service Catalog	Self-Service Portal for end users predefined products (by admin). In general IT a Document or Database created by IT team with full service details (SLA,Products,Costs etc)
Cost Explorer 	Can show even per member account the spending for an organization
Route 53 Hosted Zones	Represent a collection of records that can be managed together, belonging to a single parent domain name and have the same hosted zone's domain name as suffix
Routing Policies	The mode Route53 uses for routing (Simple,Geolocation etc)
Gateway Endpoints	Provide Private Access (without Public Internet) to DynamoDB and S3. Prefix List is added to the Route Table of each associated subnet (multiple)
Endpoint Policy	Can define which S3 resources are allowed through that endpoint and which not. Also can limit who can access the S3 bucket (e.g. subnet1 access subnet2 not)
Interface Endpoints	Provide Private Access (without Public Internet) to all AWS Services except DynamoDB and S3. ENI added to specific subnets WITHIN ONE AZ, with SG for security. For TCP and IPv4
PrivateLink	An endpoint with which I can have access to AWS or Third Party Services from a VPC directly
Guard Duty	Continuous Monitoring Security Service, connected with Data Sources + using AI/ML for threats identification (can influence it using whitelist Ips and co
SCT (Schema Conversion Tool)	Converts Database Schema to Target Engine, majority of database code objects and functions to compatible format. Also non feasible to migrate are clearly marked to do so manually
DMS (Database Migration Service)	Used for Replication/migration of databases from On Premises to AWS or AWS to premises (less likely) without disruption of the source DB
Application Discovery Service	Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers dependency mappings, configuration,usage,behavior
CloudSearch	Provides a search solution, as a fully managed service for your site
AppSync Graph QL	AppSync which uses GraphQL allows the client to specify how the data is to be structured when returned by the server. Allows real time data access and updates (GraphQL is what React uses)
Api GW quotas Http Api	Routes/api=300, max integration timeout=30sec, stages/api=10, payload size=10MB, VPC links per region = 10, 10k-15krequests per second
API GW supported types	HTTP API, REST API, Websocket API
Cloud Formation new concepts	a)Change set ==preview of changes that will be executed by stack operations, b)Stack set == a group of stacks you manage together that can replicate a group, c)template==declarative code describing the intended state of the resources, d)stack implements and manages group of resources
Cloud Formation Drift Detection	Shows whether a template has drifted from its expected template configuration
DataSync	To copy large amounts of data automatically, on prem to aws or aws to aws. Works on NFS (linux), SMS (windows), object storage,Snowcone,S3,EFS,FSx
Backup And Restore	Up to 24h
Pilot Light	10s of minutes (runs some parts) (e.g. using DB replica)
Warm standby	Minutes (scaled down environment - outdated)
Multi Site real time	Real time
Serer Migration Service	Can replicate server volumes to AWS AMIs running in EC2. For VMWare Vsphere, Windows Hyper V, Azure. From OS: Windows Server, Windows, RHEL, SUSE, Ubuntu,Oracle Linux, Fedora, Debian
Migration Hub	Provides visibility of application migration process from a Web User Interface (status update)
Global Accelerator	Traffic is moved instead through internet, through Amazon's Private global network through Edge Locations directly
Encrypted Migrations	SMS can create AMIS for migration Encrypted
Offline Migrations	AWS Snowball Edge, Snomobile
DB migration and Recovery	DMS and CloudEndure
Run Command	
Patch Manager	
Session Manager	
SSM Agent	
Glue	
Device Farm	
Lex & Connect	
Inspector	
In place and Disposal methods	In place performs application updates on same instance, disposable rolls out new by terminating older
Hybrid Cloud	AWS+AWS Outposts or Azure +Azure stack or Google GCP +Anthos
Hybrid Environment	Public Cloud + legacy on prem environment
