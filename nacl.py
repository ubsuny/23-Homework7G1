import numpy as np
import itertools

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
    def __init__(self, r_na, r_cl):
        '''
        Initialize the Cluster object.
        
        Parameters:
        - r_na: Positions of Na ions
        - r_cl: Positions of Cl ions
        '''
        self.positions = np.concatenate((r_na, r_cl))
        self.charges = np.concatenate([np.ones(r_na.shape[0]), np.full(r_cl.shape[0], -1)])
        self.combs = cp(np.arange(self.charges.size))
        self.chargeprods = self.charges[self.combs][:, 0] * self.charges[self.combs][:, 1]
        self.rij = np.linalg.norm(self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1)

    def Vij(self):
        '''
        Calculate a numpy vector of all potentials for the combinations.
        
        Returns:
        - Numpy vector of potentials for all combinations.
        '''
        self.Vij_ = np.zeros_like(self.rij)
        pos = self.chargeprods > 0
        neg = ~pos
        self.Vij_[pos] = KE2 / self.rij[pos] + B * (C / self.rij[pos]) ** 12
        self.Vij_[neg] = -KE2 / self.rij[neg] + ALPHA * np.exp(-self.rij[neg] / RHO) + B * (C / self.rij[neg]) ** 12
        return self.Vij_

    def V(self):
        '''
        Calculate the total potential, which is the sum of the Vij vector.
        
        Returns:
        - Total potential
        '''
        return np.sum(self.Vij())

    def get_vals(self):
        '''
        Get positions interpreted as a flat shape.
        
        Returns:
        - Flattened array of positions.
        '''
        return np.reshape(self.positions, -1)

    def set_vals(self, vals):
        '''
        Set positions using a flat shape of positions.
        
        Parameters:
        - vals: Flat shape of positions
        '''
        self.positions = vals.reshape(self.positions.shape)
        self.rij = np.linalg.norm(self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1)

    def __call__(self, vals):
        '''
        Function that scipy.optimize.minimize will call.
        
        Parameters:
        - vals: Positions
        
        Returns:
        - Potential energy
        '''
        self.set_vals(vals)
        return self.V()

   
       
