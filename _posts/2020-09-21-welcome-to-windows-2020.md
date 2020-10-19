---
layout: post
title: Welcome to Windows 2020
meta: This guide is going to take you through a number of components to get your machine ready for subsequent parts of this guide. 
category: coding
image: card1-img.png
date: 21 September 2020
tags: programming
---

# Welcome to Windows 2020

This guide is going to take you through a number of components to get your machine ready for subsequent parts of this guide. 

<hr>
### Table of Contents
<ol class="table-of-contents">
    <li><a href="#preparing">Preparing</a></li>
    <li><a href="#debugging">Debugging</a></li>
    <li><a href="#customisation">Customisation</a></li>
    <li><a href="#kali-machine">Kali Machine</a></li>
</ol>
<hr>

### Preparing

Hit the Windows key and type "cmd".

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/elevated-cmd-prompt.png)

Hold down `CTRL` + `SHIFT` and now hit the `Enter` key to open the command prompt as an elevated user. 

Now hit the Windows key and type "powershell"

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/elevated-powershell-prompt.png)

Hold down `CTRL` + `SHIFT` and now hit the `Enter` key to open the PowerShell prompt as an elevated user. 

Windows Version

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/winver.png)

{% include newsletter.html %}

## PowerShell Seven


Quick one-liner to install the latest version (PowerShell 7 is current at time of print) on Windows
{% highlight PowerShell %}
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
{% endhighlight %}


Follow the Wizard to the step headed "Optional Actions" and check the selection to "Enable PowerShell remoting". I also like to select "Add 'Open here' context menus to Explorer". 

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/windows-7-install-wizard-optional-actions.png)

Select the "Launch PowerShell" in the bottom left of the next wizard. 

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/windows-7-install-wizard-launch-powershell.png)

Now "Right Click" the PowerShell icon and select "Pin to taskbar". 

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/windows-7-install-wizard-pin-to-taskbard.png)

Now enter `$PSVersionTable` to confirm the version of PowerShell. 

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/windows-7-install-wizard-psversiontable.png)


@Todo 

To install on Linux
{% highlight PowerShell %}
wget https://aka.ms/install-powershell.sh; sudo bash install-powershell.sh; rm install-powershell.sh
{% endhighlight %}


## WSL

WSL version 2 is real Linux on real Windows :)


Next, we will install the Windows Subsystem for Linux and the VirtualMachinePlatform. 


Dism vs Enable-WindowsOptionalFeature


{% highlight PowerShell %}
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
{% endhighlight %}


{% highlight PowerShell %}
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart
{% endhighlight %}


![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/windows-7-enable-virtual-machine.png)


Setting version 2 of the Windows Subsystem for Linux to the default
{% highlight PowerShell %}
wsl –set-default-version 2
{% endhighlight %}

If you get an error message saying 
    
> WSL 2 requires an update to its kernel component. For information please visit https://aka.ms/wsl2kernel
    
This means you need to install the MSI another component. 

Go to [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/download-wslv2-kernel.png)

Download by clicking the link "WSL2 Linux kernel update package for x64 machines"

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/click-installer-wslv2.png)


If at this point you need to restart your virtual machine. 
{% highlight PowerShell %}
restart-computer -Confirm
{% endhighlight %}


List various versions of Linux 
{% highlight PowerShell %}
wsl --list
wsl -l -v
{% endhighlight %}

Listing versions we can see the difference

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/wsl-list-versions.png)

We will want to upgrade any wsl linux machines running version 1 (hyper-v method)

Reasons to upgrade to WSLv2
https://docs.microsoft.com/en-gb/windows/wsl/about


{% highlight PowerShell %}
wsl --set-version kali-linux 2
{% endhighlight %}

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/wslv2-conversion-in-process.png)



Run the Kali Linux Distribution
{% highlight PowerShell %}
wsl -d kali-linux
{% endhighlight %}

### Debugging

{% highlight PowerShell %}
wsl --shutdown
Dism /Online /Cleanup-Image /RestoreHealth
{% endhighlight %}


Install Code by typing `code .`

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/install-visual-studio-code.png)


Now type `code .` again and watch as Visual Stuido opens up in the Windows Host showing files from the WSL

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/visual-studio-code.png)

## Docker for Windows

Requirements

* Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 or later).
* Hyper-V and Containers Windows features must be enabled.

> **Note** - For Windows Home Edition follow this link [https://docs.docker.com/docker-for-windows/install-windows-home/](https://docs.docker.com/docker-for-windows/install-windows-home/)


1) Grab the installer [https://hub.docker.com/editions/community/docker-ce-desktop-windows/](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

2) Double-click the blue "Get Docker Desktop for Windows (stable)" button to download the executable.

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/docker-installer.png)

3) Double-Click the "Docker Desktop Installer.exe" to run the installer.

4) When prompted, ensure the Enable Hyper-V Windows Features option is selected on the Configuration page.

5) Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

> If your admin account is different to your user account, you must add the user to the docker-users group. Run Computer Management as an administrator and navigate to  Local Users and Groups > Groups > docker-users. Right-click to add the user to the group. Log out and log back in for the changes to take effect.


## Terminal App

Terminal app is seemingly turning out to be a boon for developers and those who have always looked at Windows machines with huge expectations. The open-source terminal app boasts a range of powerful features including multiple tabs, Unicode and UTF-8 character support, and GPU accelerated text rendering engine. It’s designed to be an all-in-one platform for Command Prompt, PowerShell, WSL and SSH so that developers can have seamless access to all the tools. Even better, this all-new command-line app also features custom themes and styles for a more personalized experience


https://github.com/microsoft/terminal/releases/

The new Shell


![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/new-shell.PNG)

Pin to taskbar

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/pin-new-terminal-to-taskbar.png)


### Customisation


#### Cascadia Fonts

https://github.com/microsoft/cascadia-code/releases

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/cascadia-codes.png)

Click "Install for all users"

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/install-fonts-for-all-users.png)

#### Git

Install Git for Windows
https://git-scm.com/download/win


Posh-Git adds Git status information to your prompt as well as tab-completion for Git commands, parameters, remotes, and branch names. Oh-My-Posh provides theme capabilities for your PowerShell prompt.

PSReadline lets you customize the command line editing environment in PowerShell.

{% highlight PowerShell %}
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
{% endhighlight %}

PowerShell Core
{% highlight PowerShell %}
Install-Module -Name PSReadLine -Scope CurrentUser -Force -SkipPublisherCheck
{% endhighlight %}


Oh My Posh Themes
Pick a theme https://github.com/JanDeDobbeleer/oh-my-posh#themes
{% highlight PowerShell %}
Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox
{% endhighlight %}


Customise your Kali


Install Powerline
{% highlight PowerShell %}
sudo apt install golang-go
go get -u github.com/justjanne/powerline-go
{% endhighlight %}


Install Hyper for Windows
https://releases.hyper.is/download/win

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/install-hyper-for-windows.png)

With the Hypershell open, enter the following commands
![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/hyper-shell.png)





settings.json

The settings.json file as the name suggests contains settings for the terminal application. A few of the important settings like what should be your default profile, color scheme, key bindings, etc can be found here.

To open the default.json file hold the alt key while opening settings.json file as mentioned above.

defaults.json

The defaults.json file contains all the default configuration values for the terminal. This file can be used for reference, as it is an auto-generated file and contaiSns all complete default configuration of the terminal application.






## Install Chocolatey

From an elevated PowerShell Prompt
{% highlight PowerShell %}
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
{% endhighlight %}

Confirm the installation of Chocolatey

![]({{ site.baseurl }}/assets/images/article-images/welcome-to-windows-2020/chocolatey-install-confirm-version.png)

Lets install some packages

{% highlight PowerShell %}
choco install wsl-kalilinux
{% endhighlight %}


## FireEye Commando-vm

Download the latest from:
[https://github.com/fireeye/commando-vm](https://github.com/fireeye/commando-vm)

Unzip the folder.

Use my custom profile evilsaint.json. 

<a href="evilsaint.json" target="_blank">Custom Profile</a>

My main additions are 
{% highlight PowerShell %}
{"name": "wsl.fireeye"},
{"name": "hyperv.fireeye"},
{"name": "markdownmonster"},
{"name": "wsl-ubuntu-2004"},
{"name": "wsl-archlinux"},
{"name": "wsl-debiangnulinux"},
{"name": "microsoft-windows-terminal"},
{"name": "everything"},
{% endhighlight %}

I like to remove
{% highlight PowerShell %}
{"name": "burp.free.fireeye"},
{% endhighlight %}



{% highlight PowerShell %}
cinst install <package>
{% endhighlight %}

{% highlight PowerShell %}
cup all
{% endhighlight %}




## Customising WSL


### Kali Machine


{% highlight PowerShell %}
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get clean
sudo apt-get --yes --force-yes install kali-desktop-xfce xorg xrdp
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini
sudo apt install kali-win-kex
sudo apt install kali-linux-large
{% endhighlight %}



Run two version

Run Win-KeX
* Windows mode
* seamless mode


## Customise Toys

Groupy<br>
Taskbar X<br>
T Clock<br>
Power Toys<br>
Everything<br>
Rocket / Launcher<br>
wox<br>
sharex<br>
ditto<br>

<hr class="hr-reference">
## References
<div class="reference-container">
    <a href="https://www.ivaylopavlov.com/setting-up-windows-terminal-wsl-and-oh-my-zsh/#.X2TSmz-Smud">Setting Up Windows Terminal WSL</a><br>
    <a href="https://blog.stealthbits.com/commando-vm-installation-configuration/">Commando VM Installation Configuration</a><br>
    <a href="https://www.kali.org/docs/wsl/win-kex/">Win-Kex</a><br>
</div>