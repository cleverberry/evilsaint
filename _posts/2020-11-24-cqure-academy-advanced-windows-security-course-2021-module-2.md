---
layout: post
title: "Cqure Academy: Advanced Windows Security Course 2021 - Module 2"
meta: Todays module was all about fileless malware. Both Mike and Paula were in attendance and this module were were introduced to a new member of the Cqure staff member Adrian Denkiewicz.
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

Todays module was all about fileless malware. Both Mike and Paula were in attendance and this module were were introduced to a new member of the Cqure staff member Adrian Denkiewicz. 

The lesson kicked off with Paula giving her definition of fileless malware; the phrase gets thrown around so much that it was nice to define the Cqure interpretation before the start of the lesson. 

First command we looked at is the windows build in tool <code>FLTMC</code> which I had never heard of before the session.  We used the FLTMC command to unload the SysmonDrv build into the Windows host and turn off potential error logging and event reporting... very cool

Adrian was the subject matter expert for the majority of the talk and came in around 30 minutes after course starts after Paula laying the foundations. I like Adrians definition of fileless malware so I will repeat the slide buillet points below

##### What fileless means
<ul>
<li>(Almost) No files dropped on the disk</li>
<li>Uses registry and memory</li>
<li>Living off the Land techniques</li>
<li>Requires different forensics approaches</li>
</ul>

> My favourite website for living of the land binaries is: https://lolbas-project.github.io/

After looking at turning off monitoring and talking about what fileless malware means the moved on to types of entry points used for inserting fileless malware and looked at the pros and cons of some of these types and what we can do to defend.  

One of the tools that we looked at for macro inspection for Office Macros was <a class="hover-link" target="_blank" href="https://github.com/decalage2/oletools ">oletools</a>

> oletools is a package of python tools to analyse Microsoft OLE2 files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics and debugging.