# Example: Infrastructure Operations

A Behold workspace managing physical server infrastructure — a hypervisor running multiple virtual machines and containers, each hosting a different service.

## What This Demonstrates

- **Map and territory separation:** The workspace documents infrastructure that lives on physical hardware. The agent can SSH into the host to verify state, but the workspace itself is the authoritative map.
- **Health check ceremonies:** Custom ceremony that audits service status, disk usage, and pending updates across all guests.
- **Service documentation pattern:** Each service gets a consistent 5-document structure (README, SETUP, CONFIG, REBUILD, TROUBLESHOOTING).
- **SSH-based territory verification:** The agent reaches the real infrastructure to check its own map against reality.
- **Tiered update strategy:** Security patches applied quickly with snapshots, major version upgrades planned as separate sessions.

## Workspace Structure

This example shows only the Behold state layer. The full workspace would also contain per-service documentation directories.

## Key Adaptation

The default Behold principles were extended with domain-specific additions:
- Sovereignty over convenience (self-hosted over SaaS)
- Isolation by default (one service per container)
- Rebuild from docs (if the docs can't rebuild it, the docs are incomplete)
