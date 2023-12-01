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
        return np.sum(self.v_ij())
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

#
