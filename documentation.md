# Equilibrium Configurations Of Sodium Chloride Tetramers.
 The ground state configuration of sodium chloride is face centered cubic structure. However, when the number of ions are changed , different interesting ground state 
 configurations are observed. The different  ground state configurations of Nacl shows various properties and have practical applications. The paper presents the application 
 of genetic code to study the difficult configurations of clusters (ions pairs) with optimization to ground state configurations. For cluster of four ion pairs (Na<sub>4</sub>Cl<sub>4</sub> tetramers) there are seven
 different configurations[^1 ]. Out of seven the configurations with binding energy per ion of -6.7470 eV are chosen for study.
 <img width="555" alt="structure_Na_Cl" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/8204398c-e1a2-4daf-8755-707ce0ae4433">
# Objective
- To study the structure of (Na<sub>4</sub>Cl<sub>4</sub> tetramers equilibrium configurations using 3D plot.
- Starting with arbitrary positions for Na and chloride ion.
- Optimizing the potential energy to get the optimized potential value.
- Positions of Na and Cl ions are estimated after optimizations.
- Optimized positions for ions are observed.
  # Library used
  - Numpy
  - Matplotlib with toolkits
  - Scipy.optimize.
# Potential Energy with Parameters
 Potential energy is defined in terma of attactive and repulsive Coulomb potential for different ions and same ions respectively, small dipole interacttions terms and an additional repulsive Pauli  repulsive energy term 
 for chloride ions. The constants defined and potential energy is given as[^1]:
 <img width="1102" alt="Potential" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/3c164d7e-838e-4bf5-beb6-6cfc7ceb1cc6">
# Initial Position Chosen
For the last two configurations given in paper,I have chosen square planer structure and tetrahedron structure with binding energy per ion of
-6.7470 eV[^1]. The position for square planer structure is defined as with initial a = 0.5 nm:
```Python
a = 0.5
r_na = np.array( [ [ 0, 0, 0 ], [ a, a, 0 ], [a, 0, a ], [0, a, a]] )
r_cl = np.array( [ [ a/2, a/2, a/2 ], [ 3*a/2, a/2, a/2 ], [3*a/2, a/2, 3*a/2], [a/2, 3*a/2, 3*a/2] ] )
```
Implementing the code to obtain the initial potential energy and intial positions using defined class cluster[^2];
```python
r = Cluster(r_na, r_cl)
vals_init = cluster.get_vals()
print('initial Na positions:\n', r_na)
print('initial Cl positions:\n', r_cl)
print('initial positions flattened shape:\n', vals_init )
print('initial V  :', cluster.V() )
```
<img width="834" alt="Initial value" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/c56c6606-6195-45ac-bb0b-26fa03f51d48">

Further using molecular simulation technique, system is optimized to its minimum potential state using the code to get the optimized potential energy value and optimized position of sodium and chloride ion is obtained[^2].

```python
res = scipy.optimize.minimize( fun=cluster, x0=vals_init, tol=1e-3, method="BFGS")
cluster.set_vals(res.x)  # For some reason, "minimize" is not updating the class at the last iteration
print ("Final optimized cluster positions")
print(cluster.positions)
print("Final potential:", res.fun)
```
<img width="1179" alt="Final Potential" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/e3baa4ee-5f4f-4f79-9ccf-171f4891d0bc">

The final positions of sodium and chloride ions after optimizations are plotted using matplot.lib library toolkits for 3D visualizations. 
<img width="776" alt="config_1" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/d27abb29-3de0-4240-abe5-565dda620c3e">

Similarly on using the code defined above the initial position defined for second structure chosen is;
```python
a = 0.5
r_na = np.array( [ [ 0, 0, 0 ], [ 0, 0, 2*a ], [0, a, a ], [0, 2*a, -0.5*a]] )
r_cl = np.array( [ [ 0, 0, a], [ 0, a, 2*a], [a, a, 0], [a, -a, 0] ] )
```
The initial potential value before optimization is equal to -11.89 eV.

Further the optimized value of potential and positions of sodium and chloride ions are;
<img width="711" alt="Final Position" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/5d3c58b5-4916-4e69-bdde-60c5728c0328">

The final positions of sodium and chloride ions after optimizations are plotted using matplot.lib library toolkits for 3D visualizations. 
<img width="675" alt="Final_plot_2" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/9e241ac1-7d6c-4737-a9a8-c0a69509ab38">

Thus on studying the two different structures for sodium chloride tetramers, it is observed that the value of optimized potential energy for both configuration is approximately equal as expected. However, the value of binding energy per ion for both configurations are not comparable to the value -6.7470 eV from paper. One possible reason for this anamoly might be due to the arbitrary value of position of sodium and chloride ions chosen while initializing. Further observation of final 
optimized positions gives somewhat comparable results for the positioning of sodium and chloride ion to that shown figure 4 of paper[^1].

# Pylinting 
Based on the differnt functions defined to calculate the final optimized potential and positions of sodium and chloride ions using the position and charge attribues, brief description of how code works is explained here:
The code is defined in such a way which initializes the objects of the class with attributes r_na and r_cl representing the properties of the cluster class. Further the position of sodium and chloride ions are concatenated to assign the results to the respective attributes. The line checks all possible combination from the array defined for both attributes. On computing the distance betweent the pair of ions, the result is stored in position attribute. The potentials is calculated based on the conditions: for pairs of positive charges potential is calulated using combination of Coulombic and Lennard_Jones terms and for pairs with negative charges potential is calculated using the combination of Coulombic, Pauli repulsion and Lennard Jones terms. Finally is total potential is calculated using the sum of all elements in the vector using np.sum. Finally, the final position and total potential energy is updated.

```python
"""
Defining Cluster class and related functions.
"""
import itertools
import numpy as np

# Constants
KE2 = 197 / 137  # eV-nm   Coulomb force charge
ALPHA = 1.09e3  # eV      parameter of the model
RHO = 0.0321    # nm      parameter of the model
B = 1.0         # eV      regular
C = 0.01

def cp(l):
    """
    Generate combinations of elements from the input list l.
    
    Parameters:
    - l: List of elements
    
    Returns:
    - Combinations of elements taken two at a time.
    """
    return np.fromiter(itertools.chain(*itertools.combinations(l, 2)), dtype=int).reshape(-1, 2)

class Cluster:
    """
    Class with positions and charges.
    """
    def __init__(self, na_positions, cl_positions):
        '''
        Initialize the Cluster object.
        
        Parameters:
        - na_positions: Positions of Na ions
        - cl_positions: Positions of Cl ions
        '''
        self.positions = np.hstack((na_positions, cl_positions))
        self.charges = np.hstack([np.ones(na_positions.shape[0]), np.full(cl_positions.shape[0], -1)])
        self.combs = cp(np.arange(self.charges.size))
        self.charge_prods = self.charges[self.combs][:, 0] * self.charges[self.combs][:, 1]
        self.rij = np.linalg.norm(self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1)
        self.v_ij_ = None

    def v_ij(self):
        '''
        Calculate numpy vectors for combinations.
        
        Returns:
        - Numpy vector of potentials.
        '''
        self.v_ij_ = np.zeros_like(self.rij)
        pos = self.charge_prods > 0
        neg = ~pos
        self.v_ij_[pos] = KE2 / self.rij[pos] + B * (C / self.rij[pos]) ** 12
        self.v_ij_[neg] = -KE2 / self.rij[neg] + ALPHA * np.exp(-self.rij[neg] / RHO) + B * (C / self.rij[neg]) ** 12
        return self.v_ij_

    def v(self):
        '''
        Total potential as sum of v_ij vector.
        
        Returns:
        - Total potential
        '''
        return np.sum(self.v_ij_)

    def get_vals(self):
        '''
        Positions interpreted as a flat shape.
        
        Returns:
        - Flattened array of positions.
        '''
        return np.reshape(self.positions, -1)

    def set_vals(self, vals):
        '''
        Set positions.
        
        Parameters:
        - vals: Flat shape of positions
        '''
        self.positions = vals.reshape(self.positions.shape)
        self.rij = np.linalg.norm(self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1)

    def __call__(self, vals):
        '''
        Function with scipy.optimize.minimize as call.
        
        Parameters:
        - vals: Positions
        
        Returns:
        - Potential energy
        '''
        self.set_vals(vals)
        return self.v()
```

The result for pylint is given below:

<img width="750" alt="pylint" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/94e34ca6-d723-4647-b5ea-026dcec2ae6d">

## References

[^2]: https://github.com/ubsuny/CompPhys/blob/main/MinMax/nacl.ipynb
[^1]: Michaelian, K. (1998). Evolving few-ion clusters of Na and Cl. American Journal of Physics, 66(3), 231–240. https://doi.org/10.1119/1.18851



















    

