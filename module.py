"""
This module contains the definition of a Cluster class that represents a cluster of ions
and their optimization to an equilibrium configuration using the BFGS algorithm.
"""
import itertools
import numpy as np

ke2 = 1.44 # eV-nm   Coulomb force charge
alpha = 1.09e3  # eV      parameter of model
rho = 0.0317    # nm      parameter of model
p = 1.0         # eV      regular
c = 0.01        # nm

def cp(l):
    """Generate all pairs of indices for the elements in list `l`."""
    return np.fromiter(itertools.chain(*itertools.combinations(l, 2)), dtype=int).reshape(-1, 2)

class Cluster:
    """Represents a cluster of ions."""

    def __init__(self, r_na, r_cl):
        """
        Initialize the Cluster with positions of Na+ and Cl- ions.
        """
        self.positions = np.concatenate((r_na, r_cl))
        self.charges = np.concatenate([np.ones(r_na.shape[0]), np.full(r_cl.shape[0], -1)])
        self.combs = cp(np.arange(self.charges.size))
        self.chargeprods = self.charges[self.combs][:, 0] * self.charges[self.combs][:, 1]
        self.rij = np.linalg.norm(
            self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1
        )
        self.potentials_per_step = []
        self.vij_ = None  # Initialize the attribute for later use

    def callback(self, xk):
        """Capture the potential at each step."""
        self.set_vals(xk)
        self.potentials_per_step.append(self.V())

    def Vij(self):
        '''Calculate a numpy vector of all of the potentials of the combinations'''
        self.Vij_ = np.zeros_like(self.rij)
        pos = self.chargeprods>0
        neg = ~pos
        self.Vij_[pos] = ke2 / self.rij[pos] + p*(c/self.rij[pos])**12
        self.Vij_[neg] =-ke2 / self.rij[neg] + alpha*np.exp(-self.rij[neg]/rho) + p*(c/self.rij[neg])**12
        return self.Vij_

    def V(self):
        """Return the total potential, which is a sum of the Vij vector."""
        return np.sum(self.Vij())

    def get_vals(self):
        """Return positions interpreted as a flat shape."""
        return np.reshape(self.positions, -1)

    def set_vals(self, vals):
        """Set a flat shape of positions, used by __call__."""
        self.positions = vals.reshape(self.positions.shape)
        self.rij = np.linalg.norm(
            self.positions[self.combs][:, 0] - self.positions[self.combs][:, 1], axis=1
        )

    def __call__(self, vals):
        """Function that scipy.optimize.minimize will call."""
        self.set_vals(vals)
        return self.V()
