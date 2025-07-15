from gdm.quantities import Distance

import math

from erad.quantities import Speed, Acceleration
import erad.models.fragility_curve as frag
from erad.enums import AssetTypes

DEFAULT_FRAGILTY_CURVES = [
    frag.HazardFragilityCurves(
        asset_state_param='peak_ground_velocity',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(40, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(40, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(60, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(50, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(.5, "cm/s"), Speed(40, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(50, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.5, "cm/s"), Speed(45, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(.5, "cm/s"), Speed(35, "cm/s"), 2]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(.55, "cm/s"), Speed(65, "cm/s"), 1/0.55]),
            ),
        ]
    ),
    frag.HazardFragilityCurves(
        asset_state_param='peak_ground_acceleration',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.8, 'm/s**2'), Acceleration(0.40 * 9.81, 'm/s**2'), 1 / 0.80]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.8, 'm/s**2'), Acceleration(0.40 * 9.81, 'm/s**2'), 1 / 0.80]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.5, 'm/s**2'), Acceleration(0.45 * 9.81, 'm/s**2'), 1 / 0.50]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.55, 'm/s**2'), Acceleration(0.50 * 9.81, 'm/s**2'), 1 / 0.55]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.6, 'm/s**2'), Acceleration(0.40 * 9.81, 'm/s**2'), 1 / 0.6]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.8, 'm/s**2'), Acceleration(1.0 * 9.81, 'm/s**2'), 1 / 0.8]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.45, 'm/s**2'), Acceleration(0.45 * 9.81, 'm/s**2'), 1 / 0.45]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.5, 'm/s**2'), Acceleration(0.40 * 9.81, 'm/s**2'), 1 / 0.5]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.6, 'm/s**2'), Acceleration(0.40 * 9.81, 'm/s**2'), 1 / 0.6]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.8, 'm/s**2'), Acceleration(0.50 * 9.81, 'm/s**2'), 1 / 0.70]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.5, 'm/s**2'), Acceleration(0.50 * 9.81, 'm/s**2'), 1 / 0.50]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.6, 'm/s**2'), Acceleration(0.60 * 9.81, 'm/s**2'), 1 / 0.60]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.4, 'm/s**2'), Acceleration(0.35 * 9.81, 'm/s**2'), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Acceleration(0.55, 'm/s**2'), Acceleration(0.80 * 9.81, 'm/s**2'), 1 / 0.55]),
            ),
        ]
    ),
    frag.HazardFragilityCurves(
        asset_state_param='wind_speed',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.45, "m/s"), Speed(50, "m/s"), 1 / 0.45]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.45, "m/s"), Speed(50, "m/s"), 1 / 0.45]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(50, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(45, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(45, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(55, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.3, "m/s"), Speed(55, "m/s"), 1 / 0.3]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(55, "m/s"), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(50, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.3, "m/s"), Speed(45, "m/s"), 1 / 0.30]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.54, "m/s"), Speed(55, "m/s"), 1 / 0.54]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(50, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(55, "m/s"), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(60, "m/s"), 1 / 0.40]),
            ),
        ]
    ),
    frag.HazardFragilityCurves(
        asset_state_param='flood_velocity',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(1.5, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(1.5, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(2.0, "m/s"), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(3.5, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(3.0, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(2.0, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(2.0, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(2.0, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(1.5, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.3, "m/s"), Speed(2.5, "m/s"), 1 / 0.30]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.4, "m/s"), Speed(1.5, "m/s"), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.35, "m/s"), Speed(3.5, "m/s"), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.40, "m/s"), Speed(3.0, "m/s"), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Speed(0.40, "m/s"), Speed(2.0, "m/s"), 1 / 0.4]),
            ),
        ]
    ),
    frag.HazardFragilityCurves(
        asset_state_param='flood_depth',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(0.50, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(0.50, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.40, 'm'), Distance(1.0, 'm'), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(1.0, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(1.0, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.8, 'm'), Distance(1.0, 'm'), 1 / 0.8]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(0.6, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.40, 'm'), Distance(1.0, 'm'), 1 / 0.4]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.35, 'm'), Distance(0.6, 'm'), 1 / 0.35]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.30, 'm'), Distance(0.8, 'm'), 1 / 0.3]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.40, 'm'), Distance(1.0, 'm'), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.30, 'm'), Distance(1.8, 'm'), 1 / 0.3]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.40, 'm'), Distance(2.2, 'm'), 1 / 0.40]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "lognorm", parameters = [Distance(0.25, 'm'), Distance(0.8, 'm'), 1 / 0.25]),
            ),
        ]
    ),
    frag.HazardFragilityCurves(
        asset_state_param='fire_boundary_dist',
        curves=[
            frag.FragilityCurve(
                asset_type=AssetTypes.switch,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.65, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.battery_storage,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.65, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.5, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.5, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_poles,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(1.0, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.distribution_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.1, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.solar_panels,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.55, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.substation,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.7, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_mad_mount,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.9, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transformer_pole_mount,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(1.0, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_junction_box,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.55, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_overhead_lines,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(1.1, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_tower,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.7, "km"), 0.95]),
            ),
            frag.FragilityCurve(
                asset_type=AssetTypes.transmission_underground_cables,
                prob_function=frag.ProbabilityFunction(distribution = "expon", parameters = [Distance(0.15, "km"), 0.95]),
            ),
        ]
    )
]