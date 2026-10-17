# SMS Gateway API Specifications & Documentation

A reference repository containing complete API specifications, payload schemas, and Postman collections for integrating enterprise SMS messaging gateways into software platforms.

## Overview

This repository provides comprehensive technical documentation for interacting with carrier-grade SMS messaging web services:

- **REST Web Service Documentation**: Interactive HTML and Markdown guides covering message dispatch, delivery status callbacks, balance inquiries, and incoming message polling.
- **Postman Collections**: Ready-to-import Postman workspace (`PersiaFava_SMS_Gateway.postman_collection.json`) with preconfigured environments and sample requests for all REST endpoints.
- **Enterprise User Manual**: Step-by-step documentation for managing lines, tariffs, scheduled campaigns, and access control.

## Documentation Index

| Resource | Format | Description |
|---|---|---|
| **Web Service Reference** | HTML | Complete REST API endpoint reference and parameter definitions. |
| **Postman Collection** | JSON | Executable collection covering authentication, single/bulk SMS, and delivery status. |
| **Operator Manual** | PDF / Markdown | Operational guide for managing gateways, sub-accounts, and reporting. |

## Supported Core Capabilities

1. **Transactional & OTP Messaging**: High-priority routing for one-time passcodes and account alerts.
2. **Bulk Message Broadcast**: Sliding-window batch submission with recipient array splitting.
3. **Delivery Reports (DLR)**: Webhook callbacks and polling endpoints for carrier acknowledgment tracking.
4. **Line & Credit Management**: Automated credit quota alerts and sender-ID verification.