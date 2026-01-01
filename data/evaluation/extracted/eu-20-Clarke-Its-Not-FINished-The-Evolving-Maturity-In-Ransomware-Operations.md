## It's not FINished

Mitchell Clarke and Tom Hall


### **Mitchell Clarke**

#### § Principal Consultant § London, UK § 2.5 years at Mandiant

##### snozberries_au



2



**©2020 FireEye**


### **Tom Hall**

#### § Principal Consultant § London, UK § Five years at Mandiant

##### – thall_sec



3



**©2020 FireEye**


### **Ransomware Operation Trends**



Self


4 **©2020 FireEye**



Self
Managed








### **APT**

#### § An attacker has domain admin access to my
##### environment

#### § There are multiple persistence mechanisms § They likely stole business sensitive data



5



**©2020 FireEye**


### **APT Ransomware**

#### § An attacker has domain admin access to my
##### environment

#### § There are multiple persistence mechanisms § They likely stole business sensitive data § All of my IT infrastructure is down § I can’t function as a business



6



**©2020 FireEye**


# **REvil/Sodinokibi**


### **REvil Ransomware as a Service**

#### § First seen May 2019 § Operated by UNKN § Affiliate model:

###### – Multiple threat actors use the REvil RaaS – Affiliates are vetted and buy in – Affiliates receive 60% - 75% of payouts depending on performance



8



**©2020 FireEye**


### **REvil Ransomware as a Service**

#### § Each affiliate gains access to the RaaS platform:

###### – Malware generation – Ransom demands and payment service – Victim communications – Coin laundering



9



**©2020 FireEye**


### **Sodinokibi Ransomware**

#### § On the most part, ransomed systems remain
##### functional

###### – System-related file extensions and directories are untouched
#### § To date, no issues found in crypto § Each infected system has a unique private key:

###### – Encrypted and stored in registry – Decrypted with attacker key



10



**©2020 FireEye**


### **Time to Ransomware Deployment**

#### § It depends on the affiliate § For comprehensive domain-wide ransomware
##### deployment:

###### – Up to three to four months – Some affiliates appear to have a backlog of victims



11



**©2020 FireEye**


# **REvil/Sodinokibi**


### **Initial Compromise**

#### § Mass exploitation of high-profile vulnerabilities for
##### internet-facing infrastructure:

###### – VPN – SharePoint – RDP – Remote Access Applications
#### § Lateral movement via third parties § Credential stuffing of internet infrastructure § Phishing



**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**


**Ransomware**


**Deployment**



13



**©2020 FireEye**


**Initial Compromise**


### **Establish Foothold**

##### Depends on the affiliate:

#### § Cobalt Strike § VPN abuse § Web shells





**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**


**Ransomware**


**Deployment**



14



**©2020 FireEye**


### **Escalate Privileges**

#### § Mimikatz § ProcDump § Passwords within Group Policy Preferences § Credentials stored in domain shares § Credentials stored in user profiles:

###### – Documents, text files, etc.



**Initial Compromise**


**Establish Foothold**



**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**


**Ransomware**


**Deployment**





15



**©2020 FireEye**


### **Reconnaissance**

#### § Similar tools to what we see in APT/FIN intrusions as
##### well as Red Team engagements:

###### – Advanced IP Scanner – SoftPerfect Network Scanner – Bloodhound – Built-in Windows commands



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**



**Lateral Movement**


**Maintain Presence**


**Data Theft**


**Ransomware**


**Deployment**





16



**©2020 FireEye**


### **Lateral Movement**

#### § WMIExec § SMBExec § CrackMapExec § PsExec § RDP



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**





**Maintain Presence**


**Data Theft**


**Ransomware**


**Deployment**



17



**©2020 FireEye**


### **Maintain Presence**

#### § Cloud remote desktop software § Cobalt Strike Beacon § Web shells § VPN abuse § On-premise virtual desktop appliances



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**





**Data Theft**


**Ransomware**


**Deployment**



18



**©2020 FireEye**


### **Data Theft**

#### § Data compression tools § Cloud data synchronisation platforms



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**





**Ransomware**


**Deployment**



19



**©2020 FireEye**


### **Deploy Ransomware**

#### § Disable antivirus across entire estate



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**



20



**©2020 FireEye**


### **Deploy Ransomware**

#### § Disable antivirus across targeted systems

@echo off
REM By Robbie Ferguson // baldnerd.com
REM Removes ESET Management Agent (previously named ESET Remote Administrator
Agent) from Windows machines
REM Intended for use as GPO, but could have other applications
REM PLEASE BE MINDFUL - This will remove your connection to your ESMC/ERA server.
Depending on your policies, this could be a very bad thing.
REM This program must be run as administrator
REM Version 1.01


REM Tested successfully with:
REM - ESET Management Agent 7.0.553.0 EEE9596D-3139-4B63-B08B-3F17F0E345F0


echo "Uninstalling ESET Management Agent..."
echo "Trying version 6 and under..."
wmic product where name="ESET Remote Administrator Agent" call uninstall /nointeractive
echo "Trying version 7 and up..."
wmic product where name="ESET Management Agent" call uninstall /nointeractive



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**



21



**©2020 FireEye**


### **Deploy Ransomware**

#### § Deletion of:

###### – File Backups – Archives – Virtual Machine snapshots



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**



22



**©2020 FireEye**


### **Deploy Ransomware**

#### § Creation of open SMB file shares hosting SODINOKIBI

##### ransomware

#### § Deployment of Group Policy Objects to create
##### scheduled tasks to download and execute the SODINOKIBI ransomware

#### § PsExec for mop-up



**Initial Compromise**


**Establish Foothold**


**Escalate Privileges**


**Reconnaissance**


**Lateral Movement**


**Maintain Presence**


**Data Theft**



23



**©2020 FireEye**


24 **©2020 FireEye**


### **Ransomware Negotiation**



25



**©2020 FireEye**


### **The REvil Attack Lifecycle**
##### Overview





























26



**©2020 FireEye**


## **QAKBOT and DOPPELPAYMER**


### **Partnership Model**

#### § QAKBOT initially deployed as a banking trojan § In 2020, the partnership model is seen

###### – Ransomware developers are provided access to a compromised environment with QAKBOT – Negotiations for payment are handled by the ransomware developers themselves



28



**©2020 FireEye**


### **Ransomware Attack Life Cycle**

























29



**©2020 FireEye**


### **Initial Compromise**

#### § QAKBOT campaigns in early 2020 were seen
##### utilising unsophisticated phishing campaigns

<a href=" **https://<redacted>[.]<redacted>/direct/4345091.zip** ">
ATTACHMENT DOCUMENT</a>



30



**©2020 FireEye**


### **QAKBOT Modules**


#### § QAKBOT is a modular backdoor which allows
##### an attacker to select the capabilities required and upload through the default configuration









31



**©2020 FireEye**


### **Email Staging Module Modules**


##### § The email module is a standalone binary,
###### independent from other QAKBOT modules

##### § The module creates a directory for email staging,
###### and utilises MAPI connections to a local outlook instance

–
%USERPROFILE%\EmailStorage_<computer_name>
<username>_<timestamp>

##### § Collected data is sent to a hard coded C2 with the
###### data ZLIB compressed and base64 encoded












### **Cobalt Strike Module Modules**


#### § QAKBOT can load Cobalt Strike in two ways

###### – Arbitrary Downloads

§
The attackers can push the Cobalt Strike loader as

a file and execute locally

###### – Custom module


§
The Cobalt Strike module can be configured to

load a pre-configured DLL which downloads and
executes the Cobalt Strike payload









33



**©2020 FireEye**


### **Web Inject Module Modules**


##### § The module works by injecting the contents of the
###### below file into explorer.exe

–
<install_path>\webinjects.cb

##### § The module iterates through a list of pre-configured
###### sites and injects JavaScript elements

##### § Targeting appears related to Northern American
###### organisations, as exampled below









34



**©2020 FireEye**


### **DOPPELPAYMER**

##### § In early 2020, the following delivery mechanisms

###### were seen

–
Group Policies


§
Binaries placed in SYSVOL locations and deployed

across the domain using scripts


– PsExec


– BITS Jobs


– Scheduled Tasks


##### **Four stage process** **from delivery of** **ransomware binary to** **encryption of files**



35



**©2020 FireEye**


### **Stage 1**

###### § The DOPPELPAYMER variant enumerates all users for the local

system and changes the password

###### § The password is generated with a pre-configured string and

an MD5 hash of the computer name


– _Preconfigured string:_ TtXtE9n3


– _Computer name hash:_ 384DFCCEE8DB9F89ED2859E3F32F6AF5


– _Full password:_ TtXtE9n3&384DFCCEE8DB9F89ED2859E3F32F6AF5





36



**©2020 FireEye**


### **Stage 2**

###### § The ransomware copies a legitimate service and replaces

the original with a copy of itself


– **File** _**:**_ <random>.exe


§ _Path:_ %APPDATA%\<random>.exe


§ _Note:_ Copy of DOPPELPAYMER binary


– **Service:** <random_service>


§ _Path:_ %WINDIR%\system32\<random_service>.exe


§ _Note:_ Ransomware Service


– **Service:** <random_service>-1


§ _Path:_ %WINDIR%\system32\<random_service>.exe-1


§ _Note:_ Backup of Service







37



**©2020 FireEye**


### **Stage 3**

###### § The Boot Configuration database is altered

–
recoveryenabled: no


§
Startup repair is disabled


– safeboot: minimal


§ Ransomware service is started in safeboot


–
Group policy configured to display a ransom message prior to login









38



**©2020 FireEye**


### **Stage 4**

###### § After rebooting, the DOPPELPAYMER variant will begin

encrypting files on the system.


–
<filename>.doppeled


–
<filename>.how2decrypt.txt











39



**©2020 FireEye**


### **Takeaway**

#### § Highly effective

###### – QAKBOT has been around for a long time

#### § High impact

###### – DOPPELPAYMER removes access to systems

#### § Highly active

###### – As many as an organisation a day in periods of 2020



40



**©2020 FireEye**


# **Conclusion**


#### § Everything is increasing:

###### – Payouts – Number of victims – –

##### upwards



42



**©2020 FireEye**


#### § More stealth, less noise

###### –

#### § Tooling improvements

###### – –



43



**©2020 FireEye**


### **What’s Next?**

##### devices

###### – Too many victims –

##### intervention

###### –

§
improve security


§
improve resilience



44



**©2020 FireEye**


# **Thank you**


