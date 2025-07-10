---
date: '2025-07-12T18:51:55-07:00'
draft: true
title: "Why I Plan To Build My Own Router (and Why You Might Want To Too!)"
tags: ["homelab", "router", "diy", "pfsense", "opensource"]
affiliate: false
---

I remember a time when I didn't what freak a router was. It was literally a black box to me that did the networking. That's all I needed to know. 

The first router my family had -- it was the all-in-one unit supplied by our ISP SBC Global Net (basically AT&T). It was a lockdown piece of shit. 

The first actual router we bought as family was one I foudn recomended in PC Magazine -- The Linkssy WRT54G. We used that router for nearly a decade. It was a good router. 

Its interesting how companies often forget their own products, especially the ones that make them great. The Linksyss WRT54G was unparallleed in its capabilities. I remember modinfying one with my roommate to utilize openwrt sometime after gruadating college. We continued to use the WRT54G for another 3 years. It was not until 2017 that the router finally couldnt handle it anymore. It simply did not have the processing power to handle the bandwitch required after the advent of Internet of Things. 

Then I heard about the TP-Link Archer C7/C8/C9. When introduced, it was pretty good. For its price point, it beat out the compitition from Netgear, Linksys, and Dlink. Perhaps only Asus came close. But it did not age well. Not even 5 years later, it was struggling to keep up. The psuedo communists over at TP-Link china in their communist wisedom elected to not design the dam thing with opensource (ie. openwrt or tomatowrt) in mind. So it pretty much became the back router in storage. 

Sometime in the 2010s, Linksys broguht back the nostalgia of the WRT54G as the WRT3200ACM. I procured one during the pandemic and immediatley noted that the the legend was back. And it was amazing.

Now 5 years alter, its struggling again albiet its now properly 10 years into its product cycle. 

So what offerings do we have now? 

In the entry level offerings (<$100), we have:

Mid tier ($100-$300):

Highend ($300+)

Personally I'm not impressesd by these specs. Its 2025 -- almost a quarter century since the WRT54G was released. And I must say that the folks at Cisco and Linksys are cheating us! At this rate, we'll see 16GB of ram and octacores in consumer routers in the year 2050. 

My personal pain point has always been the lockdown UI/UX of the consumer routers. As someone who has specialized network mappings, having the ability to export and save those configurations is a must. Because why would anyone wanto rebuild the network mappings again from sracth. Why would anyone want to have to manually input ip and mac addresses manually? 

For whatever reason, consumer router coampnies dont design their software with ease of use in mind (think about iXsystems, the company behind TrueNAS, included a config exporter for TrueNAS -- it makes moving/migrating to a another TrueNAS install or systesm as easy as exporting and importing a config file). My TP-Link Arhcer C9 lacked this feature. As does the Linksys WRT3200ACM router im currently using. 

You know what doesnt lack this feature? Or rather who? The opensource community. PFsense!. 

THus for the my next proeject, I am looking to build a pfsense router either from a community recommended office pc box (i.e. Lenovi Thinkcentre series) or from scratch using an ITX motherboard anad existing components.








I’ve always been a tinkerer—especially when it comes to computers. I vividly remember the first PC my family owned in 1995. I’d tag along with my dad to brick-and-mortar computer stores during the golden age of the PC, watching him and his friend spend hours building and configuring that machine. That moment planted the seed.

That, and *Prince of Persia*.  
<img src="humble-beginings.jpg" alt="humble beginings" style="max-width: 300px; display: block; margin: 0; border-radius: 8px;">

As I got older, my passion only deepened. I saved my allowance and birthday money for years before finally building my first PC as a teenager: a humble Pentium 4 (non-HT) based Celeron with 512 MB of RAM, an 80 GB hard drive, and an ATI Radeon 9200. Total cost? Just under $700. Even back then, the components I picked outperformed the generic builds sold by Dell, HP, and Compaq.

So it’s no surprise I took the same DIY approach when it came to NAS units.

---