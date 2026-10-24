# Reactive active sets

After a converged AC solve, each PV bus's aggregate required Q includes its local load. If it lies outside the sum of online generator Q bounds, the bus is clamped to that bound and becomes PQ. The equations are solved again using the previous phasors. Switches are recorded with required and bounded Q. No switch-back occurs in the same study. Slack limits and P limits are not enforced. This is load flow with reactive limits, not optimal dispatch or a full generator capability-curve model.
