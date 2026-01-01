#### **`THREAT ALERT`**

# THREAT ALERT: GootLoader - SEO Poisoning and Large Payloads Leading to Compromise

Cybereason issues Threat Alerts to inform customers of emerging impacting threats.


The Cybereason Incident Response (IR) team documented such critical attack


scenarios, which started from a GootLoader infection to ultimately deploy more


capabilities. Cybereason Threat Alerts summarize these threats and provide practical


recommendations for protecting against them.

### KEY DETAILS


    - **GootLoader has security evasion in mind :** Cybereason IR team observed


payloads with large size (40MB and more) as well as masquerading with


legitimate JavaScript code, in order to evade security mechanisms.


    - **Aggressive threat actor** : The threat actor displayed fast-moving behaviors,


quickly heading to control the network it infected, and getting elevated


privileges in less than 4 hours.


    - **Deployment of additional C2 frameworks** : Cybereason IR team observed


post-infection frameworks being deployed : Cobalt Strike and SystemBC,


which is usually leveraged for data exfiltration.


**●** **SEO Poisoning techniques used:** Cybereason’s IR team discovered SEO


Poisoning techniques used to spread malware. It works when the threat actors


create fraudulent [websites. Essentially, threat actors optimize fraudulent](https://www.linkedin.com/pulse/what-seo-poisoning-falcongaze-company/)


websites to appear higher in search engine results. It is likely the higher the


search engines results, the more likely victims will click on the links.


    - **Post-exploitation activities detected by Cybereason** : Cybereason Defense


Platform generates detections upon these infections and post-exploitation


actions.


cybereason.com


Cybereason Threat Alerts


  - **Severe Threat:** Cybereason’s IR team assesses the threat level as SEVERE


given the potential of the attacks.


**●** **Targeting English-Speaking Countries:** GootLoader targets companies in


English-speaking countries, primarily including the United States, United


Kingdom and Australia.


**●** **Target Industries Including Healthcare and Finance:** Targeted attacks have


been more prominent against healthcare and finance organizations.

### WHAT'S HAPPENING?


During the month of December 2022, the Cybereason Incident Response (IR) team


[investigated an incident which involved new deployment methods of GootLoader,](https://malpedia.caad.fkie.fraunhofer.de/details/js.gootloader)


observed [recently in other cases.](https://www.esentire.com/blog/gootloader-striking-with-a-new-infection-technique)


The following observation were made regarding the infection methods used :


  - Hosting of the infection payload on a compromised Wordpress website, acting


[as a water-hole and leveraging Search Engine Optimization (SEO)](https://www.cyber.nj.gov/garden_state_cyber_threat_highlight/seo-poisoning-what-is-in-your-search-results) (MITRE


[Stage Capabilities: SEO Poisoning) poisoning techniques to lure victims into](https://attack.mitre.org/techniques/T1608/006/)


downloading the malicious payloads


    - SEO Poisoning and Google service abuse in general has been


[documented a lot recently, which indicates this infection vector is](https://www.bleepingcomputer.com/news/security/hackers-push-malware-via-google-search-ads-for-vlc-7-zip-ccleaner/)


becoming common for threat actors


  - Cybereason IR team observed the deployment of GootLoader through


heavily-obfuscated JavaScript files with an outstanding file size (over 40


Megabytes)


On top of the new techniques utilized to load GootLoader, the post-infection


methods that the threat actor carried out stand out :


  - [Cybereason first observed Cobalt Strike](https://www.cybereason.com/blog/threat-analysis-report-all-paths-lead-to-cobalt-strike-icedid-emotet-and-qbot) deployment, which leveraged DLL


Hijacking, on top of a VLC MediaPlayer executable


Cybereason Threat Alerts


    - Cobalt Strike is an adversary simulation framework with the primary use


case of assisting red team operations, nowadays being leveraged by


threat actor for post-infection activities


  - [Cybereason then identified SystemBC](https://malpedia.caad.fkie.fraunhofer.de/details/win.systembc) being leveraged by the threat actor


    - SystemBC is a proxy malware leveraging SOCKS5 and often utilized


during the exfiltration phase of the attack


**Gootkit / GootLoader**


**Gootkit** initially started as a banking Trojan, back in 2014. It was only in 2021 when


the actors behind this piece of malware _moonlighted_ and switched from a banker


Trojan to a malware loader, then leading to the **GootLoader** name. Security firm


[Mandiant named the threat actor operating GootLoader “UNC2565”.](https://www.mandiant.com/resources/blog/tracking-evolution-gootloader-operations)


[The Sophos researchers were the first to name this malware family Gootloader.](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


GootLoader generally relies on JavaScript for their infections. It also uses SEO


poisoning techniques to place its infected pages in internet browser search results.


That way, it will change how potential victims see them by presenting different


websites whenever your link is clicked.


**SEO Poisoning and malicious Google Ads explained with an example**


SEO Poisoning and Google service abuse like Google Ads is becoming a trend


amongst malware operators to distribute their payloads.


As explained above, threat actors create websites or populate web forums or similar


websites with specific keywords and links, leading to a website hosting the infected


file.


Cybereason Threat Alerts


_Screenshots extracted from thedfirreport.com_


Search engine Ads are also leveraged so as to provide a link to the infected piece of


malware (fake software for instance) on top of the search engine.


We provided an example below when searching for Rufus Pro, a USB boot disk


[creator tool, on the search engine DuckDuckGo. The frst resulti](https://duckduckgo.com/) served is the


legitimate Rufus software page, the second being the SEO Poisoning phishing


domain.



i



i



i


Cybereason Threat Alerts


This page seems to be taken down, but another related page is still up,


However the download links to a malicious payload:


  - [https://transfer[.]sh/get/7i8rkw/Rufus_Pro_signed.exe (VT link provided)](https://www.virustotal.com/gui/file/65bd249c23ec3bf1bd53aa88edda1e149fd530df655e83a6d4c4237a0da9259a/detection)


  - This appears to be a sample of Lumma Stealer


Cybereason Threat Alerts


**Relation with Wordpress-enabled websites**


Most of the domains configured in the GootLoader PowerShell stage #2 script had


one commonality : they displayed a “ _/xmlrpc.php_ '' relation in VirusTotal.


Intelligence teams have continuously observed GootLoader leveraging compromised


Wordpress websites to use as C2 servers.


**Post-infection Activities**


Following the GootLoader infection, the Cybereason IR team observed hands-on


keyboard activities which led to further deployment of attack frameworks, Cobalt


Strike and SystemBC.


The threat actor leveraged these frameworks following the infection phase and


during the lateral movement phase.


Cybereason Threat Alerts

### ANALYSIS

#### Overall Attack Path


This diagram below describes the observed attack path during this investigation.

#### Initial Infection (Patient Zero)

##### Infection Diagram


The Cybereason IR team created a diagram to visualize the infection process, since it


involves multiple loading stages :


Cybereason Threat Alerts


When we dynamically execute the JS file in a controlled lab environment, we


observed the following process tree, including the execution of _wscript.exe_,


_cscript.exe_ and finally _powershell.exe_, with a unusual character case :


_Infection process tree as shown in the Cybereason Defense Platform_


In the next subchapters, we detail each step observed in this process tree, starting


from the initial JavaScript execution to end with the execution of PowerShell code.

##### Initial Payload (ZIP file) and SEO Poisoning


The infection in this case started from an infected website hosting the malicious


payload : an archive file with a “.zip” extension. It is worthy to mention that the threat


actor behind GootLoader leveraged SEO poisoning to enable its victims to download


the malware.


**ZIP file containing a JavaScript File**


Upon the ZIP file decompression, a JS file is offered, waiting for the victim to click on


it and execute it.


Cybereason Threat Alerts


This will result in wscript.exe executing the stage #1 payload, followed by another


stage #2 payload, a Javascript file with a **size of 40MB** (yes, you read it right, it’s 40

Megabytes). The filesize is meant to throw off security mechanisms.


The key points resulting from this analysis are the following :


  - Existence of **multiple layers of obfuscation**


  - Existence of **multiple JavaScript loops that makes the execution longer**,


probably acting as an **anti-sandbox** mechanism


  **Creation of large files to evade security mechanisms** (40 MB files for the


second stage of JavaScript)

##### Stage #1 - Initial GootLoader JavaScript Analysis (144KB JavaScript file) - Persistence





This chapter describes the initial JavaScript payload execution. This piece of code is


designed to load the next stage of the attack (a 40 MB JavaScript file) and establish


persistence on the machine through the creation of a scheduled task.


This file contains legacy code from the chroma.js library but also includes additional


custom code added by the threat actor.


_Extract from the stage #1 JavaScript file_


**The full process to deobfuscate the JavaScript stage #1 file is available** **in the**


**appendix of this document** .


The deobfuscation process is the following :


  - Through a _diff_ utility, extract the malicious code from the legitimate JS library,


chroma.js


  - Dynamically extract the obfuscated JavaScript by modifying the existing code


and logging the main decoding function


  - Beautify the resulting codes, which result in three pieces of code :


    The first one we already analyzed, and identifies it calls again the real6()


function


    - The second one is new : it contains **references to WScript** and must


execute persistence actions on the machine


    - The third one is actually an extract of the **second stage of JavaScript**


that we will analyze in the next subchapter


We beautified the second decoded piece of code and analyzed its content after


changing all the calls to another _substring_ obfuscation function :


Cybereason Threat Alerts


We identified the following actions from this code, which we modified by adding


comments and changing variable names :


  - The script checks for the existence of a task named “Customer Engineering”


through WScript calls


  - The script write the second JavaScript code stage and insert random set of


strings to make the file more heavy (this explains the 40MB resulting

JavaScript file observed initially)


Cybereason Threat Alerts


- The script creates and run a scheduled task for persistence, named “ _Customer_


_Engineering_ ” through WScript calls, and configure it to execute the recently

created JavaScript file that we called Stage 2 JavaScript





At this stage, the **execution flow will be redirected to the created second stage**

**JavaScript Gootloader file**, through the **scheduled task** execution.

##### Stage #2 - Second Stage GootLoader JavaScript Analysis (40 MB JavaScript file)


This chapter describes the infection stage related to the execution of a JavaScript


payload, starting from the executable _wscript.exe,_ and triggered through a


scheduled task as described above.


In the appendix, we detail the process of deobfuscation of the file and come up with


a way to extract the later infection stage from this Javascript file .


The JavaScript file size is extremely large : **40 MB** . As analyzed before, most of the

content of the file was automatically generated and can be removed as junk code.


Cybereason Threat Alerts


**The full process to deobfuscate the JavaScript stage #2 file is available** **in the**


**appendix of this document** .


The deobfuscation process is the following :


  Extract the actual malicious code from the file by removing the generated

large JavaScript junk code in the file


  Simplify the code and dynamically extract the code as done for the first


Javascript stage. We identified the following obfuscation methods :


    Use of variable for fixed integer values


    Creation of a table of function to complexify the execution flow


    String obfuscation through specific encoding


    - String concatenation


    - Function name obfuscation


    - Additional junk code (useless loops)


As a result, we obtain a decoded version of the code, which we pass through


_js_beautify_ to arrive at the last stage of JavaScript, where we can observe the


PowerShell code as a variable. We still need to remove another layer of obfuscation,


detailed in the appendix.


_Last stage of Javascript obfuscation, showing the execution of PowerShell_


The script contains a call of _cscript_ if the file exists, which explains the execution flow


of wscript.exe to cscript.exe, to powershell.exe.


This code explains why the created “ _POwErsHeLl_ ” process does not contain any


[argument : the PowerShell code is passed as StdIn](https://en.wikipedia.org/wiki/Standard_streams) or “Standard Input”.


Cybereason Threat Alerts

##### Stage #3 - GootLoader PowerShell Analysis


The final stage of GootLoader involved the execution of PowerShell code after its


extraction through the previous JavaScript executions. Let’s start with the actual


code, which we already cleaned up and simplified, through ChatGPT and manual


changes :


_ChatGPT AI result after asking to reformat the PowerShell code_


_ChatGPT (Chat Generative Pre-trained Transformer) is a chatbot launched by_


_OpenAI in November 2022. It is built on top of OpenAI's GPT-3 family of large_


_language models, and is fine-tuned (an approach to transfer learning) with both_


_supervised and reinforcement learning techniques. It is advised not to input any_


_sensitive data in ChatGPT._


We also ask ChatGPT to rename the variables :


Cybereason Threat Alerts


_ChatGPT output after asking to rename the variables_


Cybereason Threat Alerts


The last part of the PowerShell code contains the actual calls to the main function,


using C2 URLs as argument :


_Cleaned PowerShell stage #3 code_


The _xmlrpc.php_ URL is typical for Wordpress and indicates that the GootLoader C2


list matches with compromised Wordpress websites.


The PowerShell code can be synthetized as :


  - Executing a main loop which calls a “Command and Control” function every


20 seconds, with random GootLoader C2 URLs as parameter


  - The main “Command and Control” function acts as following :


    - Execute **system discovery calls** in order to obtain the environment


variables, list of system processes, list of processes titles, list of desktop


items and list of disks on the victim machine




Cybereason Threat Alerts


    - It then **compress and encode** the output of the system discovery calls


    - It creates a **web request to the C2 URLs** passes as parameter to the


function, sending the discovery calls outputs as **cookie parameter**


    - Obtain the response from the C2 and **evaluate its content as**


**PowerShell code** through the [iex() or Invoke-Expression function](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-expression?view=powershell-7.3)


This gives the threat actor the possibility to remotely control the victim machine as


well as gathering system data.


This discovery process is meant for the threat actor to carefully select their targets


and spend time on the most interesting ones from their point of view.

##### Synthesis


At this stage, the threat actor has :


  - Persistence on the victim machine through the “Custom Engineering”


scheduled task


  - System information gathered from the last decoded PowerShell code snippet,


which we called “Stage 3”


  - Remote control over the machine through the same code and through the


attacker-controlled C2 servers


On top of that, the attacker has resilience over the C2 as 10 different compromised


websites are configured for the specific analyzed GootLoader payload.





Following the initial infection, Cybereason observed multiple GootLoader processes


creations, over **seven days** .


Cybereason Threat Alerts


After seven days, Cybereason identified a new child process spawned from the


GootLoader _POwErsHeLl_ process.

#### Cobalt Strike


Cobalt Strike is an adversary simulation framework with the primary use case of


assisting red team operations. However, Cobalt Strike is also actively used by


malicious actors for conducting post-intrusion malicious activities.


Cobalt Strike is a modular framework with an extensive set of features that are useful


to malicious actors, such as command execution, process injection, and credential


theft.


During this incident, the threat actor loaded Cobalt Strike through the initial


communication established from the GootLoader infection. The actor then spreaded


Cobalt Strike over three other machines, through remote service creation.


[The loading method of Cobalt Strike identified used DLL hijacking](https://www.cybereason.com/blog/threat-analysis-report-dll-side-loading-widely-abused) to load the


beacon through a malicious DLL and a legitimate VLC media player executable.


Below is the overview of the first identified Cobalt Strike activity :


_First observed Cobalt Strike activity_


Cybereason Threat Alerts


##### DLL Hijacking





This chapter explains how the threat actor leveraged a vulnerability in VLC media


player to side-load a Cobalt Strike DLL. We explain how DLL hijacking is leveraged in


[a previously published Purple Team Series article.](https://www.cybereason.com/blog/threat-analysis-report-dll-side-loading-widely-abused)


The threat actor loaded Cobalt Strike through the following process :


  - Execution of the image “msdtc.exe”, which is actually a legitimate version of


VLC (SHA1 hash 0dc20b2f11118d5c0cc46b082d7f5dc060276157)


  - The created msdtc.exe process (VLC Media Player) tries to load _libvlc.dll_ . If it


can’t be loaded, it will display the following message :


  - The _libvlc.dll_ (SHA1 - e3dc0927f5cf07865587dc75ff8106eb1d161829) file that is


stored in the same directory as mdtsc.exe contains **malicious instructions**


configured to be executed from this list of exports


Cybereason Threat Alerts


_Exports list from the malicious DLL_


  - Once loaded, Cobalt Strike will execute and live within the _msdtc.exe_ process,


loaded from the _libvlc.dll_ malicious file


  - The threat actor will generally migrate to another process, leveraging Cobalt


Strike capabilities and showing a process injection to another legitimate


process (in the screenshot below, explorer.exe)


This results in the following process tree as viewed in the Cybereason console :


_Process tree resulting from the threat actor leveraging GootLoader to initiate a_


_Cobalt Strike infection_

##### Cobalt Strike DLL Analysis


Once the Cybereason team understood that the “ _libvlc.dll_ ” is Cobalt Strike, the team


analyzed it further.


[What is generally done for Cobalt Strike beacon is to extract its configuration, which](https://www.cobaltstrike.com/features/)


was done automatically through a Sandbox :


Cybereason Threat Alerts


_Extraction of the Cobalt Strike configuration_


Cybereason Threat Alerts


From this beacon extracted configuration, one can see many indicators of


compromise, including :


  - A C2 IP address, 193.106.191[.]202


  A specific URL masquerading as jquery JavaScript file


  - Default spawn location to dllhost.exe processes


[One can observe that the threat actor leveraged a Malleable C2 proflei](https://www.cobaltstrike.com/blog/malleable-command-and-control/) to complicate


detection attempts.

##### Post-infection


The loaded Cobalt Strike process, once migrated to the legitimate process


explorer.exe, will execute many actions such as :


  - BloodHound Active Directory discovery through a PowerShell version named


PSHound


_File events showing the explorer.exe process (injected with Cobalt Strike) dropping_


_BloodHound related files_


  - Internal network scanning



i



i


Cybereason Threat Alerts

#### Lateral Movement

##### Overview


During the attack, the threat actor gained more space and access by moving laterally


from patient zero to other machines in the environment


Some of the known general ways for lateral movement can be seen in the below


screenshot but in this particular case, the attacker moved laterally via remote service


creation through SMB(PSEXEC). PsExec allows for remote command execution (and


receipt of resulting output) over a named pipe with the Server Message Block (SMB)


protocol.


_Diagram showing the different lateral movement mechanisms in-use (source :_


_[https://thedfrreport.com/2022/05/09/seoi](https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/)_ _-poisoning-a-gootloader-story/)_



_i_



_i_


Cybereason Threat Alerts


The following diagram shows the lateral movements between the patient zero and


the next victim machine, and, as a second step, between this machine and the last


machine compromised :


_Diagram showing lateral movements of the threat actor_


Cybereason Threat Alerts


Below is the timeline of the events observed during the lateral movement phase :
















|Machine|Time|Action|Comment|
|---|---|---|---|
|**LATMOV1**|20:44:41|(services.exe->powershell.exe)<br>powershell.exe -nop -w hidden -c<br>Set-MpPreference<br>-**DisableRealtimeMonitoring** $true|Microsoft Defender<br>is disabled|
|**LATMOV1**|20:45:09|A service was installed on the system.<br>Service Name: ddeeff1. Service File Name:<br>C:\Windows\Temp\**msdtc.exe**.|Cobalt Strike<br>loaded through<br>DLL hijacking|
|**LATMOV1**|20:48:15|Powershell.exe -windowstyle hidden<br>-ExecutionPolicy Bypass -File<br>C:\Users\User\AppData\Local\**son.ps1**|SystemBC<br>deployment|
|**LATMOV2**|20:54:14|A service was installed on the system.<br>Service Name: cdefgh3. Service File Name:<br>powershell.exe -nop -w hidden -c<br>Set-MpPreference<br>-**DisableRealtimeMonitoring** $true. Service|Microsoft Defender<br>is disabled|
|**LATMOV2**|20:55:14|A service was installed on the system.<br>Service Name: bcdef2. Service File Name:<br>**C:\temp\msdtc.exe**. LocalSystem|Cobalt Strike<br>loaded through<br>DLL hijacking|
|**LATMOV2**|21:07:05|A service was installed on the system.<br>Service Name: abcdef1. Service File Name:<br>Powershell.exe -windowstyle hidden<br>-ExecutionPolicy Bypass -File** C:\temp\rz.ps1**.|Remote<br>deployment of<br>Cobalt Strike to<br>other machines|
|**LATMOV1**|21:08:10|**PsExec.exe** fle is dropped on LATMOV1|PsExec client|
|**LATMOV2**|21:10:18|A service was installed on the system.<br>Service Name:** PSEXESVC**.|PsExec-related<br>service|
|**LATMOV2**|21:10:20|Registry changed to: Started from:<br>Powershell -WindowStyle Hidden -File<br>**C:\temp\rz.ps1**|PowerShell rz.ps1<br>script execution<br>through PsExec|
|**LATMOV3**|21:17:11|Powershell.exe -nop -w hidden -c<br>Set-MpPreference<br>-**DisableRealtimeMonitoring** $true|Microsoft Defender<br>is disabled|
|**LATMOV3**|21:21:37|(cmd.exe->powershell.exe) powershell -nop<br>-w hidden -encodedcommand<br>JABzAD0ATgBlAHcALQB[...]|Cobalt Strike<br>deployment - SMB<br>beacon|



Through the attack timeline, Cybereason observed that the remote service creation


happened right after the malicious service was installed on the system and also right


Cybereason Threat Alerts


after the powershell script “ _rz.ps1_ ” which most likely is associated with the remote


deployment of Cobalt Strike to the next machine laterally moved to.


On top of the deployment of Cobalt Strike through the creation of a remote service,


we observe that the threat actor attempts to disable Microsoft Defender through a


PowerShell command.




##### Remote Service Creation

From the _PATIENTZERO_ machine, the threat actor leveraged file share functionalities

to first drop the files to be executed :


_File events showing a remote file creation on the machine the attacker laterally_


_moved to_


Ten seconds later, service is installed on the remote machine, infecting it with Cobalt


Strike


Three minutes later, it deployed a PowerShell file named “ _son.ps1_ ”, which happened


to be SystemBC, PowerShell version. This part of the compromise is described in the


next chapter.


Twenty minutes laters, the attacker dropped a file named “ _rz.ps_ 1” on the remote


machine.


Cybereason Threat Alerts

##### PsExec


Approximately 25 minutes later, the PsExec service was installed on the machine,


allowing the threat actor to run system commands on it, from the initially


compromised machine.


2 seconds after the PSEXESVC service creation, Cybereason observed the launch of


the PowerShell script _rz.ps1_ .

#### SystemBC

##### SystemBC Introduction


The threat actor executed a PowerShell script named _son.ps1_ on one machine. Upon


further investigation, it appeared that file was oriented toward data exfiltration and


control, providing a proxy channel for the threat actor.


Cybereason identified this file to be SystemBC, PowerShell version, as uncovered and


documented in an [article by Jason Reaves and Joshua Platt in March 2022.](https://medium.com/walmartglobaltech/systembc-powershell-version-68c9aad0f85c)


SystemBC is a proxy malware leveraging SOCKS5. Based on screenshots used in ads


on an underground marketplace, [Proofpoint decided to call it SystemBC.](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)


SystemBC has been observed occasionally, but more pronounced since June 2019.


Cybereason identified SystemBC in recent QBot infections as well.


This file creates persistence on the machine through the following run key :


  - "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" 

socks5_powershell


It also creates a covert channel from the infected host to the C2 server.


Cybereason Threat Alerts

##### Powershell Analysis


The _son.ps1_ script provided attackers with an encrypted shell communication (using


RC-4 encryption algorithm) from an infected host to their command & control server.


_Extract from the son.ps1 script code_


This script defines a function cryptf2 that uses the RC4 encryption algorithm to


encrypt a given buffer of data. The function takes in a password, the length of the


password, the data to be encrypted, the starting position in the data at which to


begin the encryption, and the size of the data to be encrypted. The function then


initializes an array $rc4 with the values 0 through 255, and uses the RC4 algorithm to


encrypt the specified data using the provided password.


Cybereason Threat Alerts


The script also defines a hash table $newconnct which takes in parameters to be


used to establish a connection to the c2 server and send the encrypted data. The


parameters include an array of bytes $sArray, an integer $perem2, an IP address $ip,


a port number $newport, an array of bytes $xorec_, a script block $s, and two more


arrays of bytes $w and $r


Printing all the variables initially collected by the script shows the data that includes


context of the execution, language and powershell version information.

##### Persistence


The script creates a registry key for persistence and is capable of removing this entry


when instructed. The destination in the entry references the location of the original


file.


_Extract from the son.ps1 script_


This registry key will automatically launch _son.ps1_ through the Powershell.exe utility


at each new user session, allowing persistence to the threat actor.


According to our log, executions of SystemBC, Powershell version, were observed


during more than 3 hours on the same machine, LATMOV1.


Cybereason Threat Alerts

### CYBEREASON RECOMMENDATIONS


The Cybereason Defense Platform can detect and prevent GootLoader, Cobalt Strike


or SystemBC post-exploitations. Cybereason recommends the following actions:


  - **Enhance Cybereason sensor policies :** Set the Cybereason Anti-Ransomware


protection mode to Prevent. More information for Cybereason customers can


be found here.


  - **Enable Variant Payload Protection in your Cybereason sensor policy** :


Upgrade to a version that has VPP and enable VPP, as this will completely


prevent the ransomware execution. VPP is supported in version 21.2.100 and


above (Beta, and disabled by default) and 22.1.183 and above (GA, and enabled


by default). More information can be found on The NEST.


  - **Compromised user blocking** : Block users involved in the attack, in order to


stop or at least slow down attacker propagation over the network


  - **Identify and block malicious network connections** : Identify network flows

toward malicious IP/domains identified in the reports and block connections


to stop the attacker from controlling the compromises machines


  - **Reset Active Directory access** : If Domain controllers were accessed by the


attacker and potentially all accounts have been stolen, it is recommended


that, when rebuilding the network, all AD accesses are reset. Important note :


krbtgt account needs to be reset twice and in a timely fashion.


  - **Engage Incident Response** : It is important to investigate thoroughly the


actions of the attacker to be sure not to miss any activity and patch what is


needed to patch.


  - **Compromised machine cleansing** : Isolate and re-image all infected


machines, to limit the risk of a second compromise or the attacker still getting


access to the network afterwards.


Cybereason Threat Alerts

#### Indicator of Compromise (IoC)


It is recommended to block the following domains and IP addresses using your

network infrastructure:


Associated Domains:


  - GootLoader C2 (compromise Wordpress websites)


    alikgriffin[.]com

    - auribluz[.]com

    - unitexfashion[.]in

    - azimut-service[.]co[.]rs

    - creator[.]co

    - fcer[.]org

    significadodeloscolores[.]com

    - crimsoncoward[.]com

    - account[.]vuzf[.]bg

    - timoconnor[.]com[.]au


User Agent:

  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/107.0.0.0 Safari/537.36"


Associated IPs:


  - 193[.]106.191.292 : Cobalt Strike C2


Add the following hashes to the blocklist in your Cybereason environment:
Associated Hashes (SHA1):


  - Libvlc.dll - e3dc0927f5cf07865587dc75ff8106eb1d161829


Cybereason Threat Alerts


Yara Rule - SystemBC PowerShell version


rule script_detection {


meta:

description = "detects a ps1 script containing required keywords and functions
for rc4 communications to a remote host - systembc_socks_powershell"

author = "Analyst"
strings:

$keyword1 = "cryptf2"
$keyword2 = "xorec"
$keyword3 = "ipaddress"
$keyword4 = "dport"
$keyword5 = "rc4"
$keyword6 = "perem"
$keyword7 = "bxor"
condition:

all of them and file.ext == "ps1"
}

## CYBEREASON DEFENSE PLATFORM


The Cybereason Defense Platform is designed to prevent and detect advanced
attacks and techniques. The recommendations above, in conjunction with
Cybereason's unique protection for malware will provide you unparalleled visibility
into this highly sophisticated attack.


Cybereason Threat Alerts

### ABOUT THE RESEARCHERS


Loïc Castel, IR Investigator, Cybereason IR Team


Loïc Castel is a Security Analyst with the Cybereason IR team. Loïc


analyses and researches critical incidents and cybercriminals, in order


to better detect compromises. In his career, Loïc worked as a security


auditor in well-known organizations such as ANSSI (French National


Agency for the Security of Information Systems) and as Lead Digital


Forensics & Incident Response at Atos. Loïc loves digital forensics and


incident response, but is also interested in offensive aspects such as


vulnerability research.


Jakes Jansen, IR Investigator Cybereason IR Team


Jakes is an Incident Response consultant and has been with


Cybereason for a total of 3 years specializing in IR, Reverse Engineering


and Threat Hunting. With over 16 years of Infosec experience in other


roles, Jakes was among other roles, responsible for building and


leading DFIR teams that have handled large scale investigations for


government and multinational private entities, including financial


institutions, manufacturing and telecommunications. Jakes also has experience in internal


threat investigations, mobile phone analysis, syndicate cases and data analysis expected with


eDiscovery during corporate acquisitions.


Nitin Grover, IR Investigator, Cybereason IR Team


Cyber Security Specialist with over 5 years of multi-geographical


experience in protecting the organizations from various cyber security


attacks. Reducing security risks by 70-80% for the clients by providing


them with optimal Vulnerability Assessments,Detailed Log Analysis,


Security Strategies, Risk Management Solutions, Credential Risk


Assessments, SIEM Solutions that include continuous threat


monitoring and malicious activity detection capabilities. Performing


Incident Response Analysis and Digital Forensic investigations for clients on a security


incident to ensure immediate containment, recovery and no business disruption.


Cybereason Threat Alerts


Cybereason Threat Alerts

### Appendix 1 - JavaScript Files Analysis

#### Stage #1


Our first action as an analyst is to extract the custom code from the JavaScript file,


related to GootLoader. It’s as simple as to obtain the legacy chroma.js library and


executing the following _diff_ command on a Linux machine :


_Extracting the custom added code from GootLoader by removing the legacy_


_chroma.js code_


We end up with a 32.7 kB file which already looks more suspicious :


Cybereason Threat Alerts


_Extract from the resulting code after the diff command_


The first function to be executed is at the end of the script and named _safe4()_ .


Cybereason Threat Alerts


_Extract from the JavaScript file named “How many states have mutual combat_


_laws”_


This _safe4()_ function tries to execute a function that is not implemented, _oxygen4()_,


to eventually call the function in the catch() part of the call, _birdc()_ .


_Extract from the JavaScript file named “How many states have mutual combat_


_laws”_


The _birdc()_ function is at the center of things. The first call to _puhvpjb()_ has no


resulting effect and is there as a distraction. It then iterates over a counter (a variable


Cybereason Threat Alerts


named _thickb2_ ), trying to call the function from the function array named _ilyojl_,


defined in the rest of the code.


We extracted the variable definitions from the code and moved them at the

beginning of the file :


_Variable definitions extracted from the original GootLoader sample_


We indeed confirm that five array values actually match with a function definition.


Since the counter is incremented, the last function should be _arev()_, which has the


higher index, 6552237.


At this step, we decide to approach this with a dynamic analysis. We added a


console.log() call to each function call from the function array and a console.log() call


to the variable that is last set in the arev() function :


Cybereason Threat Alerts


_Modified arev() function_


Upon execution, we end up with what seems to be new obfuscated code :


_Dynamically obtained second stage of JavaScript code_


Upon a quick code beautification, we conclude that the _real6()_ function must


decode its parameter, before _yahphxn()_ evaluates its result.


_Beautified code obtained from the previous execution_


Since the real6() function is the one handling the code deobfuscation, we logged the


content of the returned value of _real6()_ and print it :


Cybereason Threat Alerts


_real6() is in fact the azwka() function, that we edit with console.log() calls_


Cybereason Threat Alerts


_Extract from the execution of real6() function_


We end up with 3 different decoded results :


    The first one we already analyzed, and identifies it calls again the real6()


function


    - The second one is new : it contains **references to WScript** and must


execute persistence actions on the machine


    - The third one is actually an extract of the **second stage of JavaScript**


that we will analyze in the next subchapter


We beautify the second decode result and analyze its content :


Cybereason Threat Alerts


_Beautified version of the decode code from the real6() function_


The _x()_ function is used as a substring function that will extracts parts of the long


_DTWIfy_ string as each result is separated by the “|” character and the text is shifted by


its position ( " _rsSubFolde_ ” becomes " _SubFolders_ ” as it’s in the second position).


Using a simple regular expression-based Python script, we replace the x(int) calls


with their actual value resulting from the x() function :


Cybereason Threat Alerts


_Python script created in order to replace x() calls with a readable value_


Cybereason Threat Alerts


_Extract from the code after the x() call replacements_


This makes much more sense and we identify the following actions from this code,


which we modified by adding comments and changing variable names :


  - The script checks for the existence of a task named “Customer Engineering”


through WScript calls


Cybereason Threat Alerts


- The script write the second JavaScript code stage and insert random set of


strings to make the file more heavy (this explains the 40MB resulting


JavaScript file observed initially)


- The script creates and run a scheduled task for persistence, named “ _Customer_


_Engineering_ ” through WScript calls, and configure it to execute the recently


created JavaScript file that we called Stage 2 JavaScript


Cybereason Threat Alerts


At this stage, the **execution flow will be redirected to the created second stage**

**JavaScript Gootloader file**, through the **scheduled task** execution.


Cybereason Threat Alerts

#### Stage #2


In this section, we describe the process of deobfuscation of the file and come up with


a way to extract the later infection stage from this Javascript file .


The JavaScript file size is extremely large : 40 MB. As analyzed before, most of the

content of the file was automatically generated and can be removed as junk code.


_Opening the Blueprint Reading.js file in VIM_


Our first action is to remove the junk part. After identifying the last piece of actual


code being _crgql(3428)_, we extract the part preceding that call and export it to a new


file.


Cybereason Threat Alerts

```
>>> f = open("Blueprint Reading.js")

>>> s=f.read()

>>> js_code = s.split("crgql(3428);")[0]

>>> f2 = open("payload.js","w")

>>> f2.write(js_code+"crgql(3428);")

>>> f2.close()

```

We beautify the resulting payload.js file with js_beautify and get this as a result :


_Content of beautified_payload.js_


The content of the code is clearer now. We identified the following obfuscation


methods :


    Use of variable for fixed integer values


    Creation of a table of function to complexify the execution flow


    String obfuscation through specific encoding


    - String concatenation


Cybereason Threat Alerts


    - Function name obfuscation


    - Additional junk code (useless loops)


We simplified the code a little bit by replacing the identifying the function names

and replacing the fixed integers directly with their value.


Analyzing this resulting code allows us to identify the main function, which is an


infinite loop, trying to execute functions from the table named _msrlq_ (renamed as


_function_table_ for clarity), looping through a counter we renamed _counter_ :


_Main function after code clean-up_


This function iterates through the table, which is created function after function. We


collected the different function_table variable changes into five lines, that we


ordered to give us the order of execution of each function :


Cybereason Threat Alerts


_Function_table definitions_


The issue with the main function that we named “execute_function_table” is that it


loops infinitely. We can patch that to stop after _hqcen_ function has been executed.


At this point, we think there is another layer of obfuscation and run the Javascript


code after doing two patches :


  - Change the while() loop to stop at 100.000 (arbitrary decision)


  - Patch the _hqcen()_ function to log the content of the variables


_hqcen() function after patching to show the content of the variables_


We end up with this code and will need to re-process it as it’s again obfuscated :


Cybereason Threat Alerts


_Result of the execution_


The _jobm[3]_ function is obviously an evaluation of the content passed as parameter.


This code, once deobfuscated a bit, shows it call _jobm[3]_ function again, to evaluate


the content of the following string :


Cybereason Threat Alerts


_Deobfuscated stage #2 JavaScript_


We then proceed to execute the _barl()_ function that should decode its parameter’s


content. As a result, we obtain a decoded version of the code, which we pass through


_js_beautify_ to arrive to the last stage of JavaScript, where we can finally see the


PowerShell code as a variable :


_Deobfuscated string showing the PowerShell code_


And here are new obfuscation tricks again, this time using the V variable that will be


deconstructed to create other variables. We proceed to replace every call of V


substring to the string equivalence:


Cybereason Threat Alerts


_Last stage of Javascript obfuscation_


This is where we see the execution of Powershell through hiding its payload from the


command line by using StdIn.WriteLine.


We also notice the call of _cscript_ if the file exists, which explains the execution flow of


wscript.exe to cscript.exe, to powershell.exe.


The python code to automatically replace the V variables is the following :

```
f = open("stage3_beautified.js")

s = f.read()

import re

V =

'cReaTEobjectstdInwScRIpt.ShElLlastIndexOfexeCPOwErsHeLlScRIPtFuLLnAm
EsearchSHEll.applIcATionWRiteliNeSHElLEXeCuteOPENcscriptfullNAMEslice
\\slEep'

def replace_js(match):

  match = match.group()

  n = re.match(r"V\[T\]\(([^,]+), ([^\)]+)\)",match)

  str_position = int(eval(n.groups()[0]))

  str_len = int(eval(n.groups()[1]))

  return V[str_position:str_position+str_len]

sub = re.sub(r"V\[T\]\([^,]+, [^\)]+\)", replace_js, s)

print(sub)

```

