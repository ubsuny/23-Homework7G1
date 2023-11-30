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

   ## Optimization: Potential Energy vs. Optimization Steps for Cube

The graph shown below presents a visualization of how the potential energy of a sodium chloride (Na4Cl4) cluster changes over the course of an optimization process. The optimization aims to find the arrangement of ions that minimizes the potential energy of the system.  
![Screenshot from 2023-11-30 14-53-51](https://github.com/tirthbha/23-Homework7G1/assets/143649367/2418e0b3-72f0-4f0f-bc81-04f9aa1f68a9)



- **Y-Axis (Potential Energy):** This axis represents the calculated potential energy of the cluster at each step of the optimization, measured in electron volts (eV). A lower potential energy indicates a more stable configuration of the ions in the cluster.
  
- **X-Axis (Optimization Steps):** This axis shows the number of steps taken by the optimization algorithm. Each step represents an iteration where the algorithm adjusts the positions of the ions in an attempt to find a configuration with lower potential energy.
  
- **Trend:** The line in the graph, marked by circular points, traces the reduction of potential energy as the optimization progresses. Ideally, the line should show a downward trend, indicating that the algorithm is successfully finding configurations of lower potential energy.



- **Convergence:** The point at which the line levels off indicates where the algorithm has likely converged to a minimum. If the line flattens out, it suggests that further iterations do not significantly reduce the potential energy, implying the discovery of an optimal or near-optimal configuration.


The graph is instrumental in analyzing the performance of the optimization algorithm applied to the NaCl cluster. By examining the trend and the point of convergence, one can assess the effectiveness of the optimization process in finding a stable arrangement of ions with minimum potential energy.
## 2. Rectangular structure

The equilibrium configuration of rectangular structure for the tetramer (Na4Cl4) with its optimization is shown in the figure below:  
![Screenshot from 2023-11-30 16-20-53](https://github.com/tirthbha/23-Homework7G1/assets/143649367/fd02f960-11c0-4d48-b392-068b8670d2e0)    

The plot illustrates the configuration of an ionic cluster consisting of sodium (Na+) and chloride (Cl-) ions. 

- **Initial Positions:** Na+ ions are depicted in blue and Cl- ions in red.
- **Optimized Positions:** After optimization, Na+ ions are shown in indigo and Cl- ions in green.


 ## Optimization: Potential Energy vs. Optimization Steps for Rectangle

The graph, shown below, effectively demonstrates how the system's potential energy is minimized over the course of the optimization process. Notably, it takes 32 steps for the algorithm to reach the minimum potential energy state. This number of steps indicates the efficiency of the optimization process in converging to the lowest energy configuration. Each point on the graph corresponds to the potential energy calculated after each optimization step, providing a clear view of the energy descent.
![Screenshot from 2023-11-30 16-21-14](https://github.com/tirthbha/23-Homework7G1/assets/143649367/4b7c40f2-b1cf-44b9-a546-997aa1e32a47)  

## 3. Distorted-Rectangular structure
The equilibrium configuration of distorted-rectangular structure for the tetramer (Na4Cl4) with its optimization is shown in the figure below:    
![Screenshot from 2023-11-30 17-11-55](https://github.com/tirthbha/23-Homework7G1/assets/143649367/fd88016f-812e-4c5b-a6d5-c3e3f394682e)  

In this configuration, we have distorted  the  initial rectangular structure by allowing slight deviation in one of the position of Na+ ion (having initial position: (0, b, a))  along three different axes (delta_x = -0.02: along length a, delta_y = 0.05: along width b, delta_z = 0.08: along height h) to get the distorted-rectangular configuration for the tetramer Na4Cl4.


 ## Optimization: Potential Energy vs. Optimization Steps for Distorted-Rectangle
 
The graph, shown below, depicts that it takes 52 steps for the algorithm to reach the minimum potential energy state. This number of steps indicates the  the lowest energy configuration of the system. Each point on the graph corresponds to the potential energy calculated after each optimization step.  
![Screenshot from 2023-11-30 17-01-36](https://github.com/tirthbha/23-Homework7G1/assets/143649367/fe559eed-893b-485a-8563-f49468fef555)



   
# References
   -  K. Michaelian, "Evolving few-ion clusters of Na and Cl",Am. J. Phys. 66, 231 (1998)
   -  J. P. Rose and R. S. Berry, J. Chem. Phys. 96, 517–538 ~1992.
   -


## References

https://github.com/ubsuny/CompPhys/blob/main/MinMax/nacl.ipynb


  Michaelian, K. (1998). Evolving few-ion clusters of Na and Cl. American Journal of Physics, 66(3), 231–240. https://doi.org/10.1119/1.18851


