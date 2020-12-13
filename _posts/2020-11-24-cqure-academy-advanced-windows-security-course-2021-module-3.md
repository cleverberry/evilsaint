---
layout: post
title: "Cqure Academy: Advanced Windows Security Course 2021 - Module 3"
meta: Tonight's session certainly stepped it up a notch from module 2. This was my favourite module so far. 
category:
  - hacking
image: card1-img.png
date: 2020-11-24T03:39:00.301Z
tags:
  - courses
  - windows
  - cqure
  - advanced
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

  ul > li {
    font-size: 18px;
  }
</style>

Tonight's session certainly stepped it up a notch from module 2. This was my favourite module so far.  Frequent presenter Mike came back for this session but instead of Paula we were introduced to a new member of the Cqure team Milosz Piasecki. 

Topics covered in this were module were "Certificates and Public Key Infrastructure". Mike kicked things off with some background on the topic. Typically, Cryptography and PKI lectures can be quite dry but I felt Mike covered the introduction to the topic well, I would probably go as far to say, that for the time spent to coverage gained this was probably the best lecture on the topic I have come across. Before my readership start declaring I have a man crush on Mike, let me go justify my opinion and explain what I liked about this lecture. 

We started off with the basics and defined a few terms that often get confused, Encoding, Encryption, Hashing, Signing and then we moved on to understanding the mathmatics behind Asymmetric Cryptography, we looked a Diffie-Hellman-Merkle key exchange and RSA. I really liked this, for agest I have understood the difference between aysemetric and symetric algorithms but had never taken the time to look into the maths behind them. 

With the basic theory understood we moved on to PKI Infrastructure, this section started out with a look at Digital Certificates and moved on to looking at Root and Subordinate CAs, verifying the chain and then we moved on to comprimising the security of the domain from being able to edit the templates for the PKI. 

Obviously I have heavily summarised the above and I would hate to make it sound like something you could pick up from a few YouTube videos. In fact I recall Mike joking about the fact he had talked for an hour and 16 minutes before passing over to Milosz.

Handing over to Milosz; Mike had explained how PKI had worked and how we can abused it. Milosz dealt with the topics such as why use PKI and how we can keep it secure. One interesting part was how to use PKI infrastructure to allow trusted Macros, signed binaries and how to immplement the with AppLocker rules.  As someone always focused on the offensive it was quite refreshing to hear some advanced technical analysics on defending and so hats off to Cqure for including this in the course.  

### Rating

Remember these are relative to my own experiences and prior knowledge

<dl>
<dt>Enjoyment:</dt>
<dd>7.5/10</dd>
<dt>Difficultry:</dt>
<dd>8/10</dd>
<dt>Labs:</dt>
<dd>7/10</dd>
</dl>

### References

https://en.wikipedia.org/wiki/X.509
https://www.ssl.com/faqs/what-is-an-x-509-certificate/
https://social.technet.microsoft.com/wiki/contents/articles/7421.active-directory-certificate-services-ad-cs-public-key-infrastructure-pki-design-guide.aspx
