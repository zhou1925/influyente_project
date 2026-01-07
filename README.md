# Influyente 🚀

**Influyente** is a side project designed to simulate a social feed where influencers can purchase **Boosts** to increase their visibility and appear at the top of the feed.
The project focuses on scalability, background processing, caching, and payment integration using modern backend technologies.

---

## 🧠 Project Overview

Influyente allows influencers to:

* Purchase **Boosts** using Stripe
* Gain priority placement in the feed
* Trigger background jobs for email notifications and boost processing

The system is built to handle high traffic efficiently while preventing abuse through throttling and caching strategies.

---

## 🛠 Tech Stack

* **Backend:** Django, Django REST Framework
* **Cloud:** AWS
* **Payments:** Stripe
* **Caching & Leaderboard:** Redis
* **Message Broker:** RabbitMQ
* **Background Jobs:** Celery & Celery Beat

---

## ⚙️ Core Features

### 🔥 Boost System

* Influencers can buy boosts to increase feed ranking
* Boost priority is managed asynchronously via Celery
* Automatic expiration and scheduling handled with Celery Beat

### ⚡ Performance & Scalability

* Redis used for:

  * API response caching
  * Leaderboard/feed ranking
* Background tasks offloaded to Celery workers
* RabbitMQ used as the message broker for reliable task execution

### 📧 Email Processing

* Asynchronous email sending using Celery
* Ensures non-blocking API responses

### 🔐 Security & Rate Limiting

* API throttling enabled to:

  * Limit requests per IP
  * Reduce risk of DDoS attacks
* Secure payment handling via Stripe

---

## 🕒 Scheduled Tasks (Celery Beat)

* Boost expiration checks
* Feed recalculations
* Periodic maintenance jobs

---

## 📦 Architecture Highlights

* Decoupled background processing for scalability
* Cache-first strategy for feed and leaderboard
* Event-driven boost handling
* Production-oriented setup using AWS

---

## 🚀 Future Improvements

* Real-time feed updates using WebSockets
* Analytics dashboard for influencers
* Admin panel for boost moderation
* Horizontal scaling with multiple workers
