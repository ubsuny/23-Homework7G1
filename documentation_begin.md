# Equilibrium Configurations for Na<sub>4</sub>Cl<sub>4</sub> Tetramer Clusters

To determine the equilibrium configurations of Na<sub>4</sub>Cl<sub>4</sub> clusters for tetramers and plot their configurations with energies, we can proceed with the following steps:

1. Define the potential energy function for the Na<sub>4</sub>Cl<sub>4</sub> cluster.
   For our case the potential energy is of the form:
![Screenshot from 2023-11-26 22-12-51](https://github.com/tirthbha/23-Homework7G1/assets/143649367/afc6ae15-76d1-41ef-80e6-0ca3a6e33c25)  
The potential energy function parameters for the Na<sub>4</sub>Cl<sub>4</sub> cluster are defined as follows:
- $\ A_{ij} = 423.80 \ eV$
- $\ \rho = 0.317 \ Å$
- $\ \frac{e^2}{4 \pi \epsilon_0} = 1.44 \ eV·nm$


3. Initialize the cluster geometry to an ideal case.
4. Use an optimization algorithm to minimize the energy and find the equilibrium configuration.  
   **Note**: We will use CG algorithm for the optimization.
6. Plot the equilibrium configurations using scatter plots and label them with their energies.

# Configurations
## 1. Cubical structure
   This the first configuration among 7, with optimized potential -28.69 eV.
   ![Screenshot from 2023-11-30 14-10-05](https://github.com/tirthbha/23-Homework7G1/assets/143649367/22b9d223-0104-4127-a7b7-067413e24069)

   ## Optimization: Potential Energy vs. Optimization Steps

The graph shown below presents a visualization of how the potential energy of a sodium chloride (Na4Cl4) cluster changes over the course of an optimization process. The optimization aims to find the arrangement of ions that minimizes the potential energy of the system.  
![Screenshot from 2023-11-30 14-53-51](https://github.com/tirthbha/23-Homework7G1/assets/143649367/2418e0b3-72f0-4f0f-bc81-04f9aa1f68a9)



- **Y-Axis (Potential Energy):** This axis represents the calculated potential energy of the cluster at each step of the optimization, measured in electron volts (eV). A lower potential energy indicates a more stable configuration of the ions in the cluster.
  
- **X-Axis (Optimization Steps):** This axis shows the number of steps taken by the optimization algorithm. Each step represents an iteration where the algorithm adjusts the positions of the ions in an attempt to find a configuration with lower potential energy.
  
- **Trend:** The line in the graph, marked by circular points, traces the reduction of potential energy as the optimization progresses. Ideally, the line should show a downward trend, indicating that the algorithm is successfully finding configurations of lower potential energy.



- **Convergence:** The point at which the line levels off indicates where the algorithm has likely converged to a minimum. If the line flattens out, it suggests that further iterations do not significantly reduce the potential energy, implying the discovery of an optimal or near-optimal configuration.


The graph is instrumental in analyzing the performance of the optimization algorithm applied to the NaCl cluster. By examining the trend and the point of convergence, one can assess the effectiveness of the optimization process in finding a stable arrangement of ions with minimum potential energy.


   
# References
   -  K. Michaelian, "Evolving few-ion clusters of Na and Cl",Am. J. Phys. 66, 231 (1998)
   -  J. P. Rose and R. S. Berry, J. Chem. Phys. 96, 517–538 ~1992.
   -


## References

https://github.com/ubsuny/CompPhys/blob/main/MinMax/nacl.ipynb


  Michaelian, K. (1998). Evolving few-ion clusters of Na and Cl. American Journal of Physics, 66(3), 231–240. https://doi.org/10.1119/1.18851


