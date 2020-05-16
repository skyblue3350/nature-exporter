from prometheus_client import Gauge

definitions = {
    "coefficient": "係数",
    "cumulative_electric_energy_effective_digits": "積算電力有効桁数",
    "normal_direction_cumulative_electric_energy": "積算電力計測値（正方向）",
    "cumulative_electric_energy_unit": "積算電力量単位",
    "reverse_direction_cumulative_electric_energy": "積算電力計測値（逆方向）",
    "measured_instantaneous": "瞬時電力計測値",
}

metrics = {}
for label, desc in definitions.items():
    metrics[label] = Gauge(label, desc, ["epc"])
