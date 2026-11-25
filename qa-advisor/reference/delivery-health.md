# Delivery measurement

Measure one application or service over a stated window. Tie commits to production deployment records and deployments to incident or rollback records. Missing histories limit which metrics you can report. A pipeline definition can establish that a job exists. It does not establish how often production deployments succeeded.

| DORA measure | Evidence to collect |
| --- | --- |
| Change lead time | Commit and first corresponding production deployment timestamps |
| Deployment frequency | Production deployments per interval |
| Failed deployment recovery time | Time from a failed deployment requiring intervention to recovery |
| Change fail rate | Deployments requiring immediate intervention divided by deployments |
| Deployment rework rate | Unplanned deployments responding to production incidents divided by deployments |

Show counts with ratios and describe the classification for hotfixes. A rollback and its corrective deployment can represent one failed change and a separate rework deployment. Compare a service with its own prior windows and look at throughput alongside instability. [DORA metric definitions](https://dora.dev/guides/dora-metrics/)
