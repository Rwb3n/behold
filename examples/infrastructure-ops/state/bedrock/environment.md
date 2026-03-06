# Environment

## Infrastructure

Hypervisor host running multiple containers and virtual machines. Agent reaches the host via SSH and guests via the host's management commands.

## Access Pattern

```
Agent (this workspace)
  |
  SSH (key-based)
  |
  v
Hypervisor Host
  |
  +-- Container management commands (exec into guests)
  +-- VM guest agent commands (exec into VMs)
  |
  X-- Firewall (web UI only, no SSH)
```

## Directory Map

```
state/              State system (bedrock, shelf, flow)
services/           Per-service documentation (5-doc pattern)
topology/           Network topology, IP assignments
hardware/           Physical equipment specs
decisions/          ADRs, lessons learned, session logs
scripts/            Operational scripts (health check, batch update)
```

## Useful Commands

```bash
# SSH to host
ssh admin@host

# Check all guest status
ssh admin@host 'guest-status --all'

# Run health check
ssh admin@host 'bash /opt/health-check.sh'

# Run batch updates (with snapshots)
ssh admin@host 'bash /opt/batch-update.sh --dry-run'
```
