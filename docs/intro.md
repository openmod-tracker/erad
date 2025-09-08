# Energy Resilience Analysis for Distribution Power System

## Introduction

Understanding the impact of disaster events on people's ability to access critical service is key to designing appropriate programs to minimize the overall impact. Flooded roads, downed power lines, flooded power substation etc. could impact access to critical servies like electricity, food, health and more. The field of disaster modeling is still evolving and so is our understanding of how these events would impact our critical infrastrctures such power grid, hospitals, groceries, banks etc.

ERAD is a free, open-source Python toolkit for quantifying energy resilience in the face of hazards like earthquakes and flooding. It uses graph structures to store data and perform computation at the household level for a variety of critical services that are connected by power distribution network. It uses asset fragility curves, which are functions that relate hazard severity to survival probability for power system assets including cables, transformers, substations, roof-mounted solar panels, etc. recommended in top literature. Programs like undergrounding, microgrid, and electricity backup units for critical infrastructures may all be evaluated using metrics and compared across different neighborhoods to assess their effects on energy resilience.

To enhance data consistency and cross-platform compatibility, ERAD also integrates with the [Grid-Data-Models (GDM)](https://github.com/NREL-Distribution-Suites/grid-data-models) framework. GDM provides standardized, Pydantic-based data structures for representing distribution networks, ensuring that ERAD can seamlessly interoperate with other power system analysis tools. This integration improves interoperability by enabling direct exchange of validated network models, preserving connectivity information, and supporting temporal changes in infrastructure state. As a result, researchers and utilities can run resilience analyses in ERAD using the same distribution system models applied in power flow studies, planning tools, and other simulation platforms, significantly reducing data preparation effort and improving reproducibility.

ERAD is designed to be used by researchers, students, community stakeholders, distribution utilities to understand and possibly evaluate effectiveness of different post disaster programs to improve energy resilience. It was funded by National Renewable Energy Laboratory (NREL) and made publicy available with open license.

## Table of Contents

```{tableofcontents}
```
