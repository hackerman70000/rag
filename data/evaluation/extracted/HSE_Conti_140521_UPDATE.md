### National Cyber Security Centre 2105161000-NCSC A part of the Department of the Environment, Climate & Communications

# **NCSC Alert**

## **Ransomware Attack on Health Sector - UPDATE** **2021-05-16**

### Status: TLP-WHITE

This document is classified using Traffic Light Protocol. Recipients may share TLP-WHITE information
[freely, without restriction. For more information on the Traffic Light Protocol, see https://www.first.org/tlp/.](https://www.first.org/tlp/)
Please treat this document in accordance with the TLP assigned.


2105161000-NCSC TLP-WHITE

## **Revision History**

|Revision|Date|Author(s)|Description|
|---|---|---|---|
|1.0|14 May 2021|CSIRT-IE|Initial Alert created regarding Ransomware attack on<br>HSE Network|
|1.1|16 May 2021|CSIRT-IE|Update regarding additional information on Analysis,<br>IoCs and Att&ck Matrix TTPs|



1

TLP-WHITE


2105161000-NCSC TLP-WHITE

## **Alert**





|Threat<br>Type|On 14/05/21 the Health Service Executive (HSE) was impacted by a Ransomware<br>attack which has affected multiple services on their network The NCSC along with the<br>.<br>HSE and partners are currently investigating this incident and an Incident Response<br>process is ongoing<br>.<br>Malicious cyber activity was also detected on the Department of Health (DoH) network<br>earlyonFridaymorning(14thMay2021) howeverduetothedeploymentoftoolsduring<br>,<br>theinvestigationprocessanattempttoexecuteransomwarewasdetectedandstopped<br>.<br>These attacks are believed to be part of the same campaign targeting the Irish health<br>sector|
|---|---|
|**Details**|**Background**<br>`•` On Thursday afternoon (13/05/21), the NCSC was made aware of potential sus-<br>picious activity on the Department of Health (DoH) network and immediately<br>launched an investigation in conjunction with the DoH and a 3rd-party security<br>provider to determine the nature and extent of any possible threat.<br>`•` Preliminary investigations indicated suspected presence of cobalt strike Beacon,<br>which is a remote access tool. Cobalt strike is often used by malicious actors in<br>order to move laterally within an environment prior to execution of a ransomware<br>payload.<br>`•` At approx 07:00 hrs on 14th May the NCSC was made aware of a signiﬁcant in-<br>cident affecting HSE systems. Initial reports indicated a human-operated ‘Conti’<br>ransomware attack that had severely disabled a number of systems and necessi-<br>tated the shutdown of the majority of other HSE systems.<br>`•` Early Friday morning (14th May 2021) malicious cyber activity was also detected<br>on the DoH network, however due to a combination of anti-virus software and<br>the deployment of tools during the investigation process an attempt to execute<br>ransomware was detected and stopped.<br>`•` The HSE took the decision to shut down all of its IT systems as a precaution in<br>order to assess and limit the impact.<br>**Response**<br>`•` The NCSC has activated its crisis response procedures and is providing support<br>and assistance to the HSE and Dept of Health in responding to and recovering<br>from the incident.|


2

TLP-WHITE


2105161000-NCSC TLP-WHITE





|Details<br>contd<br>.|• The NCSC is also continuing to monitor other networks to address the risk of<br>further attacks<br>.<br>TheNCSChavecirculatedappropriateadvicetoconstituentorganisationsfollow-<br>•<br>ing further analysis of this cyber attack<br>.<br>• The HSE have limited network connectivity to other healthcare providers as a<br>precautionary measure<br>.<br>Impact<br>• There are serious impacts to health operations and some non-emergency pro-<br>cedures are being postponed as hospitals implement their business continuity<br>plans<br>.<br>• The national vaccination programme is not affected<br>.<br>ForinformationrelatedtoHSEservices pleasevisitHSECyberAttackwebpage<br>•<br>, .|
|---|---|
|**Remediation**|**Contain**<br>1. Isolate Domain Controllers<br>2. Block egress to the internet<br>3. Create clean VLANs for rebuild and recovery operations<br>4. Block malicious IPs and domain names<br>5. Protect Privileged accounts<br>6. Harden endpoints<br>**Eradicate**<br>1. Wipe, rebuild and update all infected devices.<br>2. Ensure antivirus is up to date on all systems.<br>3. Make sure all hardware devices are patched and up to date.<br>4. Use your offsite backups to restore systems - before restoration take steps to<br>ensure your backups have not be exposed to malware.<br>**Recover** (The 5 R’s to Recovery)<br>1. Restore endpoints<br>2. Re-image devices if required<br>3. Re-set credentials<br>4. Re-Integrate Quarantined systems<br>5. Restore Services<br>Establish monitoring of the network for further suspicious activity, particular attention<br>should be placed on activity related to pre-cursor malware that may have pre-empted<br>ransomware attack (IcedID/BazarLoader/Trickbot etc.).|


3

TLP-WHITE


2105161000-NCSC TLP-WHITE





|Analysis|The NCSC have observed a variant of Conti Ransomware and inital analysis has re-<br>vealed the following:<br>• Cobalt Strike beacons discovered on systems suggest that it was used to move<br>laterally within the environment prior to executing the Conti ransomware payload<br>.<br>• Use of WMICexe to delete shadow copies:<br>.<br>cmd exe / c C:\Windows\System32\ wbem\WMIC exe shadowcopy<br>. .<br>where "ID=’{REDACTED}’" delete<br>• Internal network subnets are enumerated and results are saved to files<br>• Multiple batch files ( bat) used to copy malware to endpoints<br>.<br>• psexec exe then used to execute malicious payload on endpoints using<br>.<br>compromised user credentials<br>• Conti Ransomware v3 - 32 bit executable discovered<br>• Creates mutex:<br>YUIOGHJKCVVBNMFGHJKTYQUWIETASKDHGZBDGSKL237782321344<br>• The malware will attempt to encrypt all files with the exception of the following<br>file names:<br>CONTI _LOG .txt<br>–<br>readme .txt<br>–<br>* FEEDC<br>– .<br>* .msi<br>–<br>– * .sys<br>* .lnk<br>–<br>* dll<br>– .<br>– * .exe<br>• The malware begins by calling many bogus WinAPIs with invalid arguments to<br>intentionally throw exceptions These are handled by the malware and act as an<br>.<br>anti -emulation/sandbox evasion technique<br>• Encrypted files are renamed with a FEEDC extension<br>.|
|---|---|
|**Indicators**<br>**of Compro-**<br>**mise**|The following indicators of compromise have been observed related to this incident:<br>`•`** Conti SHA256:**<br>d21c71a090cd6759efc1f258b4d087e82c281ce65a9d76f20a24857901e694fc<br>`•`** Cobalt Strike SHA256:**<br>234e4df3d9304136224f2a6c37cb6b5f6d8336c4e105afce857832015e97f27a<br>`•`** Cobalt Strike SHA256:**<br>1429190cf3b36dae7e439b4314fe160e435ea42c0f3e6f45f8a0a33e1e12258f<br>`•`** Cobalt Strike SHA256:**<br>8837868b6279df6a700b3931c31e4542a47f7476f50484bdf907450a8d8e9408<br>`•`** Cobalt Strike SHA256:**<br>a390038e21cbf92c36987041511dcd8dcfe836ebbabee733349e0b17af9ad4eb|


4

TLP-WHITE


2105161000-NCSC TLP-WHITE





|Indicators<br>of Compro-<br>mise<br>contd<br>.|Cobalt Strike SHA256:<br>•<br>d4a1cd9de04334e989418b75f64fb2cfbacaa5b650197432ca277132677308ce<br>• Filename: EXE bat<br>_ .<br>• Filename: COPYbat<br>_ .<br>• Lazagne SHA256:<br>5a2e947aace9e081ecd2cfa7bc2e485528238555c7eeb6bcca560576d4750a50|
|---|---|
|**Mitre**<br>**ATT&CK**|`•` EXECUTION - Windows Management Instrument [T1047]<br>`•` EXECUTION - Native API [T1106]<br>`•` EXECUTION - Shared Modules [T1129]<br>`•` DEFENSE EVASION - Software Packing[T1027.002]<br>`•` DEFENSE EVASION - Masquerading[T1036]<br>`•` DEFENSE EVASION - Hidden Window[T1564.003]<br>`•` DEFENSE<br>EVASION<br>-<br>Virtualization/Sandbox<br>Evasion::System<br>Checks<br>[T1497.001]<br>`•` DISCOVERY - System Time Discovery [T1124]<br>`•` DISCOVERY - File and Directory Discovery [T1083]<br>`•` DISCOVERY - System Network Connections Discovery[T1049]<br>`•` DISCOVERY - Process Discovery [T1057]<br>`•` DISCOVERY - System Network Conﬁguration Discovery [T1016]<br>`•` DISCOVERY - System Time Discovery [T1082]<br>`•` DISCOVERY - Network Share Discovery [T1135]<br>`•` IMPACT - Data Encrypted for Impact [T1486]<br>`•` IMPACT - Inhibit System Recovery[T1490]|


5

TLP-WHITE


**DISCLAIMER:** This document is provided “as is” without
warranty of any kind, expressed or implied, including, but
not limited to, the implied warranty of fitness for a particular
purpose. NCSC-IE does not endorse any commercial
product or service, referenced in this document or otherwise.


National Cyber Security Centre
29-31 Adelaide Road,
Dublin, D02 X285,

Ireland

**Tel:** +353 (0)1 6782333
**Mail:** [certreport@decc.gov.ie](mailto:certreport@dccae.gov.ie)
**Web:** [ncsc.gov.ie](https://www.ncsc.gov.ie)
**Twitter:** [ncsc_gov_ie](https://twitter.com/ncsc_gov_ie)


