---
title: "The Router That I Remember Fondly (And Why I’m Building My Own)"
date: '2025-07-06T18:51:55-07:00'
draft: false
topics: ["Homelab"]
tags: ["networking", "homelab", "opensource", "pfsense", "linksys"]
description: "From the legendary WRT54G to locked-down firmware nightmares, here's why I'm ditching consumer routers and building my own pfSense box."
---

My first router came bundled with our ISP—**SBCGlobal**, later acquired by AT&T. It was a locked-down, underwhelming piece of junk. My first *real* router, though, was a legend: the **Linksys WRT54G**, recommended by *PC Magazine*. My family used that thing for nearly a decade. It was rock solid.

<img src="linksys-wrt54g.jpg" alt="the legend" style="max-width: 300px; display: block; margin: 0; border-radius: 8px;">

Funny how companies forget what made them great. The WRT54G was ahead of its time. Years later, after college, my roommate and I pulled one out of the trash and resurrected it. We modded it with **OpenWRT**, and it ran for another three years until 2017—when it could no longer keep up. Its single-core processor simply couldn’t handle modern bandwidth demands, let alone the explosion of smart devices and IoT.

Linksys discontinuation of this line is akin to Ford abandoning the Taurus...only bringing it back later. 

---

## When Promise Meets Disappointment

Next came the **TP-Link Archer C7/C8/C9** era. At launch, these were strong contenders—especially at their price point. They regularly outperformed routers from Netgear, D-Link, and even Linksys. ASUS came close, but TP-Link had the edge in price-to-performance.

Unfortunately, that promise faded fast. Within five years, they were showing their age. Worse, TP-Link’s decision to lock down the firmware made open-source support a nightmare. No OpenWRT, no Tomato—just headaches. (Eventually, DD-WRT became available, but it felt like an afterthought.)

<img src="tplink-archer-c8.jpg" alt="a new challenger emerges" style="max-width: 300px; display: block; margin: 0; border-radius: 8px;">

Ironically, TP-Link is a Chinese company—and yet, their product went *against* any spirit of collectivism or community. No sharing, no support, and minimal configurability. You’d expect a little more openness, but I guess it’s only communal when it’s convenient. That once-promising router now sits in storage—exiled like a fallen comrade.

---

## The Return of a Classic

In the mid-2010s, Linksys tried to recapture the magic with the **WRT3200ACM**—a spiritual successor to the WRT54G. I picked one up during the pandemic, and for a while, it felt like the legend was back. And to be fair, it held its own for years.

But five years later, it’s starting to show its limits again—occasional issues with the 5GHz band, for example. Still, not bad for a router approaching its ten-year mark. Alas, there is no real sucesssor to the WRT3200ACM offered by Linkssys that I am aware of.

Again, Linksys discontinuation of this line is akin to Ford abandoning the Taurus...for the 2nd time (they really did this)!


<img src="linksys-wrt3200acm.jpg" alt="the legend returns" style="max-width: 300px; display: block; margin: 0; border-radius: 8px;">

---

## 📡 Router Spec Breakdown
---

### 🔹 Linksys WRT54G  
*The early-2000s classic that set the standard*

| Spec                    | Details                                         |
|-------------------------|-------------------------------------------------|
| **Release Year**        | ~2002                                           |
| **Wi-Fi Standard**      | 802.11b/g (2.4GHz only)                         |
| **Wi-Fi Speed**         | Up to 54 Mbps                                   |
| **CPU**                 | Broadcom BCM5352 @ 200 MHz                      |
| **RAM**                 | 16 MB (early), 8 MB (later)                     |
| **Flash Storage**       | 4 MB (or 2 MB on cost-reduced versions)         |
| **Ethernet Ports**      | 1 WAN + 4 LAN (10/100 Mbps)                     |
| **Antenna**             | 2x external 2 dBi                               |
| **Open-Source Support** | Excellent (OpenWRT, DD-WRT, Tomato)             |
| **Notes**               | Revered for hackability, especially versions 1–4 |
| **Cost**                | $180 |
---

### 🔹 TP-Link Archer C8  
*A solid mid-2010s performer that aged poorly*

| Spec                    | Details                                         |
|-------------------------|-------------------------------------------------|
| **Release Year**        | ~2014                                           |
| **Wi-Fi Standard**      | 802.11ac (dual-band: 2.4GHz + 5GHz)             |
| **Wi-Fi Speed**         | AC1750 (450 Mbps + 1300 Mbps)                   |
| **CPU**                 | Broadcom BCM4708A0 @ 800 MHz (dual-core)       |
| **RAM**                 | 128 MB                                          |
| **Flash Storage**       | 16 MB                                           |
| **Ethernet Ports**      | 1 WAN + 4 LAN (Gigabit)                         |
| **USB Ports**           | 1x USB 3.0, 1x USB 2.0                          |
| **Antenna**             | 3x external                                     |
| **Open-Source Support** | Poor (locked bootloader on most models)         |
| **Notes**               | Strong start, but firmware lock-in killed its longevity |
| **Cost**                | $100 |
---

### 🔹 Linksys WRT3200ACM  
*The spiritual successor, with caveats*

| Spec                    | Details                                         |
|-------------------------|-------------------------------------------------|
| **Release Year**        | 2016                                            |
| **Wi-Fi Standard**      | 802.11ac (dual-band, MU-MIMO support)          |
| **Wi-Fi Speed**         | AC3200 (600 Mbps + 2600 Mbps theoretical)      |
| **CPU**                 | Marvell Armada 88F6820 @ 1.8 GHz (dual-core)   |
| **RAM**                 | 512 MB DDR3                                     |
| **Flash Storage**       | 256 MB NAND                                     |
| **Ethernet Ports**      | 1 WAN + 4 LAN (Gigabit)                         |
| **USB Ports**           | 1x USB 3.0, 1x combo eSATA/USB 2.0              |
| **Antenna**             | 4x external high-performance                    |
| **Open-Source Support** | Very good (OpenWRT supported, but finicky)      |
| **Notes**               | Marketed to enthusiasts, but plagued by Marvell Wi-Fi driver issues (which affected feasability of opensource firmwares like openwrt and ddwrt|
| **Cost**                | $250 |

---

### 🔹 ASUS RT‑AX5400  
*A modern dual-band Wi-Fi 6 router with solid internals*

| Spec                    | Details                                         |
|-------------------------|-------------------------------------------------|
| **Release Year**        | 2023                                            |
| **Wi-Fi Standard**      | Wi-Fi 6 (802.11ax), dual-band                  |
| **Max Speed**           | AX5400 (574 Mbps + 4804 Mbps)                  |
| **CPU**                 | Triple-core @ 1.5 GHz                          |
| **RAM**                 | 512 MB                                          |
| **Flash**               | 256 MB                                          |
| **Ethernet**            | 1× 2.5 GbE WAN + 4× 1 GbE LAN                  |
| **USB Ports**           | 1x USB 3.2 Gen 1                               |
| **Firmware**            | AsusWRT (AiProtection, AiMesh support)         |
| **Notes**               | Great performance for the price, but firmware remains closed-source |
| **Cost**                | $120 |

## What I Really Want in a Router

Here’s what I actually care about in a modern router:

- ✅ Dual 2.5GbE ports (not one token 2.5GbE + 4x 1GbE gimmick)
- ✅ Quad-core CPU @ 2.0 GHz or better
- ✅ At least 1 GB of RAM
- ✅ Open-source firmware support
- ✅ The ability to **export and import configurations and mappings**

These aren’t outlandish demands—they’re just **basic features for power users**. But almost no consumer router on the market delivers this combination out of the box consistently other than NetGate and maybe Ubiquiti though both are considered prosumer if not enterprise and thus quite pricy some even costing as much as $600 or $900.

---

## 🔍 The State of Consumer Routers in 2025

Let’s take a snapshot of what’s available right now:

### 🔹 Asus RT‑BE58U

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2024                                         |
| **Wi‑Fi Standard** | Wi‑Fi 7 (802.11be), dual-band              |
| **Max Speed**    | ~3.6 Gbps (688 + 2882 Mbps)                  |
| **CPU**          | Quad‑core @ 2.0 GHz                          |
| **RAM**          | 1 GB                                         |
| **Flash**        | 256 MB                                       |

---

### 🔹 Netgear Nighthawk RS300

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2025                                         |
| **Wi‑Fi Standard** | Wi‑Fi 7, tri-band (2.4/5/6 GHz)            |
| **Max Speed**    | ~9.3 Gbps                                    |
| **CPU**          | Quad‑core @ 2.0 GHz                          |
| **RAM**          | 2 GB                                         |
| **Flash**        | 512 MB NAND                                  |

---

### 🔹 Netgear Nighthawk Pro Gaming XR1000

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2021                                         |
| **Wi‑Fi Standard** | Wi‑Fi 6 (AX5400), dual-band               |
| **Max Speed**    | ~5.4 Gbps (600 + 4800 Mbps)                  |
| **CPU**          | Triple‑core @ 1.5 GHz                        |
| **RAM / Flash**  | Not specified officially                     |

---

### 🔹 TP-Link BE3600 (Archer BE3600)

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2024                                         |
| **Wi‑Fi Standard** | Wi‑Fi 7, dual-band                         |
| **Max Speed**    | ~3.6 Gbps                                    |
| **CPU**          | Quad‑core @ ~2.0 GHz                         |
| **RAM**          | 2 GB DDR4                                    |
| **Flash**        | 256 MB                                       |

---

### 🔹 TP-Link Archer AX55

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2022                                         |
| **Wi‑Fi Standard** | Wi‑Fi 6 (AX3000), dual-band               |
| **Max Speed**    | ~2.976 Gbps                                  |
| **CPU**          | Dual‑core @ 1.0 GHz (Qualcomm IPQ0518)       |
| **RAM**          | 512 MB                                       |
| **Flash**        | 128 MB                                       |

---

### 🔹 Asus RT‑BE96U

| Spec             | Details                                      |
|------------------|----------------------------------------------|
| **Release Year** | 2024                                         |
| **Wi‑Fi Standard** | Wi‑Fi 7 (tri-band: 2.4 / 5 / 6 GHz)        |
| **Max Speed**    | ~18.7 Gbps                                   |
| **CPU**          | Quad‑core @ 2.6 GHz                          |
| **RAM**          | 2 GB DDR4                                    |
| **Flash**        | 256 MB                                       |

---

### 🧩 Market Summary

- **Entry-level (< $100)**  
  Still mostly plastic boxes with questionable firmware support, aging chipsets, and no forward-thinking features.

- **Mid-tier ($100–$300)**  
  More capable hardware, but UI/UX remains clunky. Still no standard config backup/export tools (like what if I wanted to export configs between makes and models). Monitoring features are weak.

- **High-end ($300+)**  
  You're mostly paying for marketing: “mesh,” “gaming,” RGB antennas. Hardware’s better, but it rarely gives you real control.

---

## What Manufacturers Are Pushing (That I Don’t Want)

- **Mesh systems**: These are often brand-locked and exist to sell you *more* hardware. It reminds me of early 2000s Wi-Fi gear—where a Linksys adapter worked best with a Linksys router and a NetGear adapter best with a NetGear router. I suspect this is probalby due to differences in firmware and perhaps lack of standards across manufactuers. 


- **Wi-Fi 6E and 7**: Honestly? I don’t even know what version I’m on. Probably Wi-Fi 5. The naming conventions are confusing, and the benefits aren’t clear to me. It just comes off as marketing nonsense to me. Something to get me hyped up to buy a new router thinking my old one is obsolete. 

- **Tri-band & “gaming” routers**: Just marketing bloat, in most cases. Unless you're in a multi-floor household with dozens of high-throughput devices, the extra bands do very little. And the extra antennas look sily. I'd rather have more RAM and CPU. Or atleast a router that looks ornamental like a Excalibur (Sword In The Stone), Taj Mahal, Stone Henge. I'd even take an Eiffel Tower looking router if its all about big pointy antennas. 


Indeed, ChatGPT concurs:
> In the early 2000s, Wi-Fi gear from the same brand often worked better together because:  
>  
> - **Standards were immature** – many devices used draft or inconsistent versions of 802.11b/g.  
> - **Vendors added proprietary features** (like Linksys “SpeedBooster”) that only worked with matching hardware.  
> - **Firmware and driver quality varied**, leading to bugs and compatibility issues.  
> - **Security protocols like WPA** weren’t consistently supported across brands.  
>  
> As a result, pairing a Linksys adapter with a Linksys router often gave more stable and faster connections than mixing brands. This issue largely faded by the 2010s as Wi-Fi standards matured and interoperability improved.

Why manufactuers insist on pushing mesh products in closed ecosystems? Short term profits. You buy their mesh router, you end up buying their mesh nodes. No mix and matching manufactuers makes and models with one another. Closed ecosystem --> more profits.

Why manufactuers market Wifi 6 and Wifi 7 instead of giving us more RAM? We'd probably upgrade less often otherwise. Create scarcity when ample supply (of RAM) exists. Theres no arugment against power draw here -- its nelgible. no argument against cost either -- RAM gets significantly cheaper every year. 

Why manufacturers insist on designing gaming routers to resemble alien warships is beyond me. It feels like a form of aesthetic gatekeeping—signaling that unless your gear looks aggressive and overdesigned, you’re not a “real” gamer or as I would say enthusisast. 

Modern consumer routers often feel like they’re designed for obsolescence from the moment of inception—overhyped with flashy aesthetics, underpowered internals, and a locked-down firmware that resists improvement or longevity.

Real enthusiasts are ahead of the curve, they're early adopters, and they don't like limitations. Honestly, are we getting what we really want? I know I am not. 

---

It’s been nearly 25 years since the WRT54G, and while we’ve gotten faster speeds and flashier packaging, core user freedoms and hardware flexibility have regressed. We head aimlessly towards faster speeds be it wifi 7, 8 or 9 and or 2.5Gbe and 10Gbe ethernet connections while neglicting usability (configs) and adequte system resources. 

Don’t even get me started on the **deceptive hardware revisions**. A model may advertise a certain CPU or RAM size, only for newer batches to quietly downgrade those specs—without any clear distinctions other than the SKUs. 

## The Real Problem: Locked-Down UI and Vendor Lock-In

My biggest frustration with modern consumer routers isn’t just the hardware—it’s the software.

Most router interfaces are clunky, shallow, and locked down. Want to back up your config? Good luck. Want to reflash it with OpenWRT? Better hope your model wasn’t quietly locked with a signed bootloader or worse -- gets bricked during the process. Want to restore IP/MAC assignments or VLAN mappings after a reset? You’ll probably have to do it all manually unless the manufacturer kindly included some way to import or export configs. Even then, good luck accomplishing this across different manufacturers let alone different models within the same manufacturer. There is absolutely no standardization in the industry. 

Meanwhile, NAS platforms like **TrueNAS** from iXsystems let you export and restore full system configurations in seconds. That’s what I expect in 2025. Yet routers like my **TP-Link Archer C8** and even my more recent **Linksys WRT3200ACM** don’t consistently offer this basic functionality.

Why is this so rare? 

---

## Enter Open Source: pfSense

The open-source community gets it right. Specifically, **pfSense**.

With pfSense, you get:

- ✅ Full configuration export/import
- ✅ VLANs, traffic shaping, firewall rules—without artificial limits
- ✅ Logs and monitoring tools that are actually useful
- ✅ Documentation and community support that doesn’t leave you guessing

Instead of marketing gimmicks and firmware restrictions, pfSense gives you **control**—which is all I’ve ever really wanted from a router.

---

## What’s Next for Me

So, I’m building my own router.

I’ll either:

- Repurpose a community-favorite office PC like the **Lenovo ThinkCentre**, or  
- Build a small-form-factor ITX box using spare parts.

Either way, I’m done with closed ecosystems that treat configurability like an afterthought.

<img src="lotr-meme.jpg" alt="a new era" style="max-width: 300px; display: block; margin: 0; border-radius: 8px;">

---

## What I Want In My Router

- ✅ 2x 2.5GbE ports  
- ✅ Quad-core Intel (7th/8th gen, T-series preferred)  
- ✅ 8 GB DDR4 RAM  
- ✅ pfSense with full config export/import  
- ✅ My existing ASUS RT-AX5400 will serve as a Wi-Fi access point

Rather than build everything from scratch (which can easily drive costs over $100), I’m aiming for a used **Lenovo ThinkCentre M920q**—highly recommended by the pfSense community for its reliability, efficiency, and mod potential.

---

### 🔹 Custom pfSense Router: Lenovo ThinkCentre M920q Mod

| Spec               | Details                                                  |
|--------------------|----------------------------------------------------------|
| **Built Year**     | 2025                                                     |
| **Wi-Fi Support**  | N/A (wired only—uses separate AP)                        |
| **CPU**            | Intel Core i5‑8500T @ 2.1 GHz (6-core)                   |
| **RAM**            | 8 GB DDR4                                                |
| **Storage**        | 256 GB NVMe SSD                                          |
| **Ethernet Ports** | 1×1 GbE (onboard) + 2×2.5 GbE (PCIe mod)                 |
| **Firmware**       | pfSense                                                  |
| **Notes**          | Everything I wanted that Linksys, TP-Link, and Netgear refused to give me |
| **Anticiapted Total Cost**| $300 |

---

## Why I’m Avoiding Cheap “pfSense Boxes”

Many Chinese manufacturers now sell barebones mini-PCs marketed as "pfSense-ready." They’re compact and affordable—but there’s a common theme in user reviews: **poor thermal design**.

Most of these boxes rely entirely on passive cooling, with no fans, no airflow planning, and no margin for heat spikes. They often fail within a couple of years. Whether it’s bad design, cost-cutting, or just laziness, it’s a dealbreaker for something meant to run 24/7.

The **ThinkCentre M920q**, on the other hand, is small but well-built. Sure, it’s not perfect—its compact form limits airflow—but at least it has **active cooling** and a track record of reliability.

I estimate it will cost me approximatley $10/yr more to run than a regular consumer grade router. But what it gets me in peformance, features, and configurabiltiy makes up for that cost. If it ends up being useful for a adecade, it more than makes up for the extra cost. Indeed, I do not expect 10Gbe ethernet to become affordable for some time -- manufacturers are have just started introducing 2.5Gbe in their latest offerings of the past 2 years...it will be some time before 10Gbe becomes normalized. 

---

## Wrapping Up

Consumer routers have come a long way in some areas—but they’ve regressed in others. Configurability, transparency, and user empowerment have been traded for lock-in, glossy dashboards, and firmware gimmicks. Aesthetics comes at the price of performance. 

So I’m building something better because the market can't deliver what I desire. 

Stay tuned: I’ll be documenting the full build and config process soon. Who knows, maybe I'll ask someone to 3d print me a Linksys WRT54G housing or repurpose and old one. 