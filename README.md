---
title: OpenEnv Email Env
emoji: 📧
sdk: docker
app_port: 7860
---

# OpenEnv Email Triage Environment

## Overview
This environment simulates a real-world email inbox where an AI agent must:
- Read emails
- Reply appropriately
- Manage urgency
- Optimize steps

## Tasks

### Easy
Reply to urgent email.

### Medium
Reply with fewer steps.

### Hard
Efficient handling with optimal policy.

## Action Space
- reply
- archive
- escalate

## Observation Space
- inbox
- drafted responses
- step count

## Reward
+1 correct reply  
Episode ends after 3 steps  

## Run

docker build -t openenv .
docker run openenv