# Islands and references

Connected components use online branches only. Isolated buses are components. Each component must contain exactly one Slack bus; disconnected islands with their own references can be solved together because their Jacobian blocks are independent. Multiple slack buses within one component or a component without a slack are rejected before iteration. Opening a branch changes topology without deleting the equipment. No automatic reference promotion or load shedding occurs.
