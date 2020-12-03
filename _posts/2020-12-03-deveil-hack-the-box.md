---
layout: post
title: Deveil by Hack the Box
meta:
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

Nmap scan

![nmap-scan]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/nmap-scan.png "nmap-scan")

FTP with anonymous login is interesting.

Hmmm, looks like I cant connect

![ftp-error-conecting]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/ftp-error-conecting.png "ftp-error-conecting")

Lets use debug mode <code>ftp -d</code> to see if we can find out why?

![ftp-debug-mode]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/ftp-debug-mode.png "ftp-debug-mode")

Wait, why is the PORT command sending that local address.

![local-ip-address-comparison]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/local-ip-address-comparison.png "local-ip-address-comparison")

Ah of course, makes sense now. I am connecting via WSL and the local IP Address being sent to the remote FTP server is a local address which it cant use. Lets switch to passive mode <code>ftp -p</code>.

![ftp-error-conecting (1)]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/ftp-error-conecting (1).png "ftp-error-conecting (1)")

So it looks like we are in the root of the web server judging by the <code>.htm</code> extension files.

![welcome-image-webserver-root]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/welcome-image-webserver-root.png "welcome-image-webserver-root")

Lets test a theory!

![welcome-image-webserver-root]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/welcome-image-webserver-root.png "welcome-image-webserver-root")

Web request for default is server page.

![invoke-webrequest-default-server-page]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/invoke-webrequest-default-server-page.png "invoke-webrequest-default-server-page")

So it looks like we are in the root of the webserver. Let’s try and upload a webshell. First lets locate our webshells in Kali Linux.

![webshell-aspx]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/webshell-aspx.png "webshell-aspx")

Now we upload the shell

![upload-web-shell]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/upload-web-shell.png "upload-web-shell")

Looks like we are in business

![webshell-in-browser]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/webshell-in-browser.png "webshell-in-browser")

Whoami

![whoami]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/whoami.png "whoami")

Privs

![privilleges]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/privilleges.png "privilleges")

Lets try and get a better shell to the box

{% highlight PowerShell%}
netsh interface portproxy add v4tov4 listenport=9999 listenaddress=0.0.0.0 connectport=9999 connectaddress=172.27.215.201
{% endhighlight%}

![create-reverse-shell-aspx]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/create-reverse-shell-aspx.png "create-reverse-shell-aspx")

Lets upload our payload

![upload-payload]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/upload-payload.png "upload-payload")

So far so good

![payload-uploaded]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/payload-uploaded.png "payload-uploaded")


![empire-listener-stager]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/empire-listener-stager.png "empire-listener-stager")

![upload-payload]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/upload-payload.png "upload-payload")

so far so good

Lets run powerup

![powerup]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/powerup.png "powerup")

ok now lets try sherlock

![no-powerup-checks]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/no-powerup-checks.png "no-powerup-checks")

![potential-exploits]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/potential-exploits.png "potential-exploits")

looks like we have some potential exploits

Let us get a reverse shell in meterpreter

![create-reverse-shell-aspx]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/create-reverse-shell-aspx.png "create-reverse-shell-aspx")

![meterpreter-shell]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/meterpreter-shell.png "meterpreter-shell")

![local-privesc]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/local-privesc.png "local-privesc")

![local-privesc-exploit]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/local-privesc-exploit.png "local-privesc-exploit")

Standard User

![stduser]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/stduser.png "stduser")

Root user

![root-user]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/root-user.png "root-user")

Let use gain a more interactive shell using Nishang

![nishang-tcp-listener]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/nishang-tcp-listener.png "nishang-tcp-listener")

![invoke-web-shell]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/invoke-web-shell.png "invoke-web-shell")

lets download and upload the exploit

![stduser]({{ site.baseurl }}/assets/images/article-images/deveil-hack-the-box/stduser.png "stduser")