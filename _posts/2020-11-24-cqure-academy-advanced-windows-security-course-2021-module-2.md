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

> **Update**: In my post last session I said I hadnt been given access to the labs. I appologies, this isnt true, I had but missed the email due to filtering rules.

Todays module was all about fileless malware. Both Mike and Paula were in attendance however this module we were introduced to a new member of the Cqure staff, Adrian Denkiewicz - The subject matter expert on fileless Malware. The lesson kicked off with Paula giving her definition of fileless malware; the phrase often gets thrown around by security consultants and vendors, sometimes incorrectly, hence it was nice to have Paula's definition priot to the start of the lesson. 

##### What is fileless Malware

* (almost) No Files dropped on the disk.
* Uses registry and memory
* Living off the Land techniques
* Requires different forensics approach

We started the lesson off looking at monitoring solutions and MiniFilter Drivers commonly relied on to protect organisations against Malware. The first command we looked at was the built in windows command <code>FLTMC</code> which I had never heard of before the session.  Before we move on, for those that do not know whatt Minifilter Drivers are:

> **Minifilter Driver**: A file system filter driver (Minifilter) is an optional driver that adds value to or modifies the behavior of a file system.

The first driver in the lecture was Sysmon from Sysinternals, or momre specfically the Symon driver. It was quite interesting to see how easy it is for us to unload the driver or detach the disk being monitored :-o, apparently an approach used often in Malware. I was quite shocked to see that despite the above steps the Sysmon Driver was showing as running after running <code>sc query SysmonDrv</code> yet wasnt actually doing anything useful. 

As I mentioned, Adrian was the subject matter expert for the majority of the talk and came in around 30 minutes after Paula layed the foundations. Moving on from Paulas display of turning off Sysmon Drivr monitoring we moved on to looking at the different types of entry points used for inserting fileless malware and looked at the pros and cons of some of these types and what we can do to defend against them. During this discussion we talked about Living off the land binaries and tools we can use to test files found using these insertion points (See references for further reading) and the pros and cons of the methods.

One of the tools that we looked at for macro inspection for Office Macros was <a class="hover-link" target="_blank" href="https://github.com/decalage2/oletools ">oletools</a>

> oletools is a package of python tools to analyse Microsoft OLE2 files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics and debugging.

Prior to the session I had only used the oledump tool by legend Didier Steves, if that name doesnt ring a bell then I suggest you check out his website. His cmd.exe as a dll file has helped me out on many stolen laptop assessments. Also, on this note, check out the tool by OneLogicalMyth (see references below) he has created a beautiful HTA shell that is just as handy.

Adrian spent the majority of the session looking at variou malware hiding and deofuscation techniques and rapidly introduced us to a lot of tools. I wont go into full details as I dont think it is fair to Cqure or other students who have paid like me. Instead I will give people a few interesting things to look into and research in their own time.

* VBA macro deobfuscation technique.
* primer of the oletools suite.
* EvilClippy and PDF Stomping.
* Using HxD to hide sheets in Excel Spreadsheets.
* Decompiling PDFs and reading malicious JavaScript stored within.
* Deconstructing Kovter (Case Study of Fileless Malware in the wild).
* Injecting Null Code bytes into the registry to stop regedit from examining payloads.
* Typical shellcode functions such as <code>virtualalloc</code> and <code>memset</code>.
* Registry persisence techniques.

All I will say is check out EvilClippy and read the associated blog in the references at the bottom of the page. Adrian introduced us to this tools and some of the tecniques it can be usef for are certainly eye opening. 

If I had one gripe with the course so far I would say it is the fact the webinars go straight through with no break. It is by no means a major gripe as the sessions are recorded and are available later however when you are eagerly listening it is hard to detect a convenient point to quickly nip to the bathroom, in addition, it can take 24 hours for the recorded material to be uploaded so if you have scheduled time for the evening you might be dissapointed to have to wait to the next day to fill in some knowledge you might of missed. 

### Rating

Remember these are relative to my own experiences and prior knowledge

<dl>
<dt>Enjoyment:</dt>
<dd>7/10</dd>
<dt>Difficultry:</dt>
<dd>6/10</dd>
<dt>Labs:</dt>
<dd>7/10</dd>
</dl>

### References (and related links)

<div class="reference-container">
    <a href="https://ss64.com/nt/fltmc.html">FLTMC</a><br>
    <a href="https://lolbas-project.github.io/">Lolbas Project Github</a><br>
    <a href="http://www.decalage.info/python/oletools">Oletools</a><br>
    <a href="https://blog.didierstevens.com/programs/oledump-py/">Oledump</a><br>
    <a href="https://github.com/outflanknl/EvilClippy">EvilClippy</a><br>
    <a href="https://www.decalage.info/python/pdfid">Pdfid</a><br>
    <a href="https://github.com/dzzie/pdfstreamdumper">PDF Stream Dumper</a><br>
    <a href="https://github.com/vinaypamnani/wmie2/releases">Releases</a><br>
    <a href="https://www.dcsoft.com/products/regeditx/">Regeditx</a><br>
</div>