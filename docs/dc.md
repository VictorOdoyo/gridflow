# DC power flow

Online branch flow is `(theta_from-theta_to-shift)/(x tap)`. Angles and shifts are radians internally. Resistance, reactive demand, voltage magnitude changes and charging are omitted. Bus shunt conductance is treated as constant MW at 1 pu. Each island reference retains its specified angle. The returned zero loss is a model assumption, not an AC-loss estimate. MW/rating utilization is only an approximate proxy for MVA thermal loading.
