---
layout: post
title: Generating a New Public Key
meta: How to generate a new public key.
category: " "
image: card1-img.png
date: 2020-10-22T03:20:00.853Z
tags: " "
---
## Generating a New Public Key


{% highlight PowerShell %}
ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub
{% endhighlight %}



===========================================
https://www.ssh.com/ssh/passphrase