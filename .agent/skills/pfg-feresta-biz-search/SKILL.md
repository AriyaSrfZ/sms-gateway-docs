---
name: pfg-feresta-biz-search
description: Enterprise B2B account profiling, buying committee hierarchy mapping, connection tree routing, and surgical outreach hook engine for PFG-Feresta SMS Gateway & Telecom Platform.
---

# PFG-Feresta Enterprise B2B Business Development Skill

## Overview
A specialized skill for conducting Account-Based Marketing (ABM) profiling, executive hierarchy mapping, and surgical outreach for high-volume enterprise SMS and transactional messaging accounts in Iran.

---

## 1. The 5-Parameter Qualification Heuristic

Before prospecting or writing to any target company, audit the account across the 5 approved pillars:

1. **Documented Online Latency / Delivery Complaints (اسب تروجان فنی):**
   - Search keywords: `[Brand] + ("پیامک" OR "کد تایید" OR "OTP") + ("نیومد" OR "تاخیر" OR "قطع")` on Twitter/X, CafeBazaar, Myket, and LinkedIn.
   - Threshold: At least 2 documented user delivery failure cases during market peak hours.
2. **Aggressive Financial Turnover & High Growth (گردش مالی بالا و رشد تهاجمی):**
   - Targets: 24/7 Gold & commodity trading, freight logistics, LendTech/BNPL, and mission-critical ERPs.
3. **Heavy Transactional Event Intensity (وابستگی حیاتی به پیامک تراکنشی):**
   - High ratio of OTP, invoice notifications, trade confirmations, and load assignments vs. low-value bulk advertising.
4. **Under-the-Radar / Low Vanity Brand (کاهش نفوذ رقیب / Low IEI):**
   - Avoid vanity logos with subsidized negative tariffs on competitor homepages (e.g., Kavenegar, Mediana, SMS.ir). Target unentrenched champions.
5. **Relationship Network Leverage (ضریب دسترسی سازمانی):**
   - Map connection pathways across organizational leadership: C-Suite/Board governance, Commercial/Procurement execution, and Technical de-risking.

---

## 2. ABM Account Profiling Template

Every account analysis must generate a standardized 4-part profile:

```markdown
### [Account Name] ([Legal Entity])
- **Company LinkedIn:** [URL]
- **Official Website:** [URL]
- **Industry & Business Model:** [e.g., Gold Trading, B2B Freight Logistics]
- **Operational Pain Point:** [Documented bottleneck, e.g., voice-call fallback costs or SMS queue congestion]

#### Buying Committee & Hierarchy Tree:
| Name & Identity | Corporate Title | Role in Buying Process |
| :--- | :--- | :--- |
| [Executive / Founder] | CEO / Board Member | Economic Buyer / Approver |
| [Tech Lead / Architect] | CTO / VP of Eng | Technical Champion / Evaluator |
| [Commercial / Finance] | Procurement / Sales Head | Contract Gatekeeper |

#### Connection Priority & Channel Strategy:
- **Primary Driver:** [e.g., C-Level Introduction vs. Direct Commercial Outreach]
- **Strategic Angle:** [e.g., Failover Secondary Route, Zero Switchover Downtime]

#### Surgical Outreach Hooks:
- **C-Suite Hook (Business / Revenue Protection):** "[Short tailored pitch linking SMS delay to customer churn and voice fallback costs]"
- **Tech Lead Hook (Latency / Reliability Proof):** "[Short technical pitch highlighting P99 < 2s SLA, direct SMPP, and live handset delivery webhooks]"
```

---

## 3. Surgical Outreach Hook Guidelines

### The C-Suite Rule:
- Never open with product feature lists or SMS pricing tables.
- Focus exclusively on:
  1. Preventing transaction loss during volatile market peaks.
  2. Eliminating expensive voice-call OTP fallback costs.
  3. Risk-free second route deployment (بدون قطعی روت اصلی).

### The Technical Lead Rule:
- Focus on developer-first empathy:
  1. REST API and SMPP documentation readiness in under 2 hours.
  2. Live handset delivery reports via push webhooks (نه فقط تحویل به مخابرات، بلکه تا گوشی کاربر).
  3. High-concurrency queue isolation for OTP traffic.

---

## 4. Execution Commands

To execute profiling on a new account:
1. Run `python -c "import urllib.request..."` to verify company LinkedIn company slug and official website footer links.
2. Search executive leadership using Iranian tech databases (Rasmio, Jobinja, Quera).
3. Generate the account dossier following the ABM template above.
