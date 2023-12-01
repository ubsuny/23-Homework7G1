# Equilibrium Configurations Of Sodium Chloride Tetramers.
 The ground state configuration of sodium chloride is face centered cubic structure. However, when the number of ions are changed , different interesting ground state 
 configuartions are observed. The different  ground state configurations of Nacl shows various properties and have practical applications. The paper present the application 
 of genetic code to study the difficult configurations of clusters (ions pairs) with optimization to ground state configurations. For cluster of four ion pairs (Na<sub>4</sub>Cl<sub>4</sub> tetramers) there are seven
 different configurations. Out of seven the configurations with binding energy per ion of -6.7470 eV are chosen for study.
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
 Potential energy is defined in terma of attactive and repulsive Coulomb potential for different ions and same ions respectively, small dipole interacttions terms and an additional repulsive pauli energy term for 
 for chloride ions. The constants defined and potential energy is given as:
 <img width="1102" alt="Potential" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/3c164d7e-838e-4bf5-beb6-6cfc7ceb1cc6">
# Initial Position Chosen
For the last two configurations given in paper for,I have chosen square planer structure and tetrahedron structure with binding energy per ion of
-6.7470 eV. The Position for square planer structure is defined as with initial a = 0.5 nm:
```Python
a = 0.5
r_na = np.array( [ [ 0, 0, 0 ], [ a, a, 0 ], [a, 0, a ], [0, a, a]] )
r_cl = np.array( [ [ a/2, a/2, a/2 ], [ 3*a/2, a/2, a/2 ], [3*a/2, a/2, 3*a/2], [a/2, 3*a/2, 3*a/2] ] )
```
Implementing the code to obtain the initial potential energy and intial positions using defined class cluster;
```python
r = Cluster(r_na, r_cl)
vals_init = cluster.get_vals()
print('initial Na positions:\n', r_na)
print('initial Cl positions:\n', r_cl)
print('initial positions flattened shape:\n', vals_init )
print('initial V  :', cluster.V() )
```
<img width="834" alt="Initial value" src="https://github.com/pratibha77118/23-Homework7G1/assets/72980895/c56c6606-6195-45ac-bb0b-26fa03f51d48">


    

