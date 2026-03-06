# Checkpoint

Last updated: 2026-03-05

## Active

- Batch update script deployed and tested. First full sweep completed (12 targets, zero failures).
- Pre-update snapshots in place for rollback — clean up after 24h stability confirmation.
- Health check script operational on host. Weekly ceremony established.
- All core services running and documented with 5-doc pattern.

## Next

- Clean up pre-update snapshots after stability confirmation
- Address VM disk at 76% — check usage, clean up or resize
- Reverse proxy + clean URLs for all services
- Status monitoring dashboard deployment

## Later

- Password manager deployment (evaluated, not yet deployed)
- Secret management for agent VMs
- Automated boot notification sequence
- Media request flow polish (request -> download -> notification)
