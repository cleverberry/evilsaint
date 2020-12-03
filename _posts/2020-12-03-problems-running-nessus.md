---
layout: post
title: Problems Running Nesus
meta:
category:
  - hacking
image: card1-img.png
date: 2020-12-03
tags:
    - internal-inf
    - external-inf
    - nessus
    - scanning
    - host-discovery
    - port-scanning
permalink: blog/:title
---
<style>
  .hover-link:hover {
    
  }

  .hover-link {
    font-weight: bold;
    cursor: pointer;
    color: #05cfa3;
  }
</style>

It mentions the following:

> “When a user with an administrator account in a Windows Vista computer’s local Security Accounts Manager (SAM) database remotely connects to a Windows Vista computer, the user has no elevation potential on the remote computer and cannot perform administrative tasks. If the user wants to administer the workstation with a SAM account, the user must interactively log on to the computer to be administered.”

HKLM.

0 - build filtered token (Remote UAC enabled) 1 - build elevated token (Remote UAC disabled)

If you set the DWORD entry to 1, you will be able to connect to the admin share since the remote login is not filtered.

Obviously this is not restricted to “net use” but applies to all variations of remote account logins.

Reg add HKEY_LOCAL_MACHINE /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f

/v - name of the key /t - type of the key /f - force, no confirmation.

<ol>
<li>Click Start, click Run, type regedit, and then press ENTER.</li>
<li>Locate and then click the following registry subkey: HKEY_LOCAL_MACHINE</li>
<li>If the LocalAccountTokenFilterPolicy registry entry does not exist, follow these steps:</li>
<li>On the Edit menu, point to New, and then click DWORD Value.</li>
<li>Type LocalAccountTokenFilterPolicy, and then press ENTER.</li>
<li>Right-click LocalAccountTokenFilterPolicy, and then click Modify.</li>
<li>In the Value data box, type 1, and then click OK. Exit Registry Editor.</li>
<li>Open Explorer → select Network → Network discovery and file sharing are turned off. Network computers and devices are not visible. Click to change… → Turn on network discovery and file sharing → authorise the User Account Control (UAC) prompt.</li>
</ol>

<hr class="hr-reference">
## References
<div class="reference-container">
    <a href="https://astrix.co.uk/news/2019/11/26/nessus-professional-tips-and-tricks">Nessus Professional Tips and Tricks</a><br>
    <a href="http://download.microsoft.com/download/5/6/a/56a0ed11-e073-42f9-932b-38acd478f46d/WindowsVistaUACDevReqs.doc">Windows Vista</a><br>
    <a href="https://docs.microsoft.com/en-us/archive/blogs/vistacompatteam/uac-and-remote-logon">UAC and Remote Login</a><br>
</div>