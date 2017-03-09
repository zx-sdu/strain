#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

import six
import abc
import copy

import numpy as np
import pymatgen as mg
from pymatgen.analysis.elasticity.strain import Deformation

class Strain(six.with_metaclass(abc.ABCMeta, object)):
    @abc.abstractmethod
    def apply(structure, strength_multiplier=1.):
        pass

class CartesianStrain(Strain):
    def __init__(self, deformation_matrix, pos_displacement_matrices=None):
        self.deformation = Deformation(np.eye(3) + deformation_matrix)
        self.pos_displacement_matrices = pos_displacement_matrices

    def apply(structure, strength_multiplier=1.):
        new_structure = self.deformation.apply_to_structure(structure)
        # move positions - use original cartesian positions
        if self.pos_displacement_matrices is not None:
            for idx, mat in self.pos_displacement_matrices:
                new_structure.translate_sites(
                    indices=[idx],
                    vector=np.dot(mat, struc.cart_coords[idx]),
                    frac_coords=False
                )
        return new_structure