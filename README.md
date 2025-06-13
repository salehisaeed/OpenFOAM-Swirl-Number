# Swirl number calculation in OpenFOAM

<!-- ![Swirl number over time](docs/figures/swirl_number_plot.png)
![Swirl number over time](docs/figures/vectors.png) -->
<p align="center">
  <img src="docs/figures/vectors.png" alt="Velocity vectors" width="45%" />
  <img src="docs/figures/swirl_number_plot.png" alt="Swirl number over time" width="45%" />
</p>

This repository provides a full pipeline for computing the swirl number in OpenFOAM.

## Theoretical Background

The **swirl number** is a dimensionless measure that quantifies the ratio of axial flux of angular momentum to axial flux of axial momentum, It is commonly computed as

$$ S = \frac{\int_A \rho u_\theta u_z r \, \mathrm{d}A}{R \int_A \rho u_z^2 \, \mathrm{d}A} $$

Where
* $\rho$ is the density
* $u\_\theta $ is the azimuthal velocity
* $u\_z $ is the axial velocity
* $r $ is the radial distance to the axis
* $R $ is a characteristic radius
* $A $ is the area of the cross-section



## 🛠️ Function Objects and Code Structure

The swirl number is computed using several modular function objects:

| File                        | Description                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------- |
| `funcObjComponents`         | Extracts components of velocity vector                                                                   |
| `funcObjCylVel`             | Transforms Cartesian velocity field to cylindrical components                                            |
| `funcObjDerivedFields`      | Computes derived fields like $\rho \mathbf{U}$                                                           |
| `funcObjTangentialMomentum` | Computes local tangential momentum                                                                       |
| `funcObjlMomentumFlux`      | Computes the axial flux of tangential and axial momentum (numerator and denominator of the swirl number) |
| `funcObjSwirlNumber`        | Aggregates numerator and denominator to compute the swirl number                                         |



## Postprocessing Output

The arbitrary surface is sampled using a `plane` geometry and processed using `surfaceFieldValue`. The Python script `compute_swirl_number.py` loads the numerator and denominator files, computes the swirl number at each time step, and plots the swirl number over time.



## Acknowledgments

This repository utilizes the OpenFOAM tutorial case `axialTurbine_rotating_oneBlade` provided by **Håkan Nilsson** (Chalmers University of Technology). The tutorial case is now part of the official OpenCFD release of OpenFOAM. For more information about the case, visit the tutorial at

```
$FOAM_TUTORIALS/incompressible/pimpleFoam/RAS/axialTurbine_rotating_oneBlade/
```
