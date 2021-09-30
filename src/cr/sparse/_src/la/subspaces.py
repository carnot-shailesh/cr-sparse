# Copyright 2021 CR.Sparse Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import jax.numpy as jnp
from jax import jit, lax

from .svd_utils import singular_values

def orth_complement(A, B):
    """Returns the orthogonal complement of A in B
    """
    rank_a = A.shape[1]
    C = jnp.hstack([A, B])
    Q, R = jnp.linalg.qr(C)
    return Q[:, rank_a:]

def principal_angles_cos(A, B):
    """Returns the cosines of principal angles between two subspaces 

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (jax.numpy.ndarray): The list of principal angles between two subspaces 
            from smallest to the largest.
    """
    AH = jnp.conjugate(A.T)
    M = AH @ B
    s = singular_values(M)
    # ensure that the singular values are below 1
    return jnp.minimum(1, s)

principal_angles_cos_jit = jit(principal_angles_cos)

def principal_angles_rad(A, B):
    """Returns the principal angles between two subspaces in radians

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (jax.numpy.ndarray): The list of principal angles between two subspaces 
            from smallest to the largest.
    """
    angles = principal_angles_cos(A, B)
    return jnp.arccos(angles)

principal_angles_rad_jit = jit(principal_angles_rad)

def principal_angles_deg(A, B):
    """Returns the principal angles between two subspaces in degrees

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (jax.numpy.ndarray): The list of principal angles between two subspaces 
            from smallest to the largest.
    """
    angles = principal_angles_rad(A, B)
    return jnp.rad2deg(angles)

principal_angles_deg_jit = jit(principal_angles_deg)

def smallest_principal_angle_cos(A, B):
    """Returns the cosine of smallest principal angle between two subspaces 

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (float): Cosine of the smallest principal angle between the two subspaces
    """
    angles = principal_angles_cos(A, B)
    return angles[0]

smallest_principal_angle_cos_jit = jit(smallest_principal_angle_cos)

def smallest_principal_angle_rad(A, B):
    """Returns the smallest principal angle between two subspaces in radians

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (float): The smallest principal angle between the two subspaces in radians
    """
    angle = smallest_principal_angle_cos(A, B)
    return jnp.arccos(angle)

smallest_principal_angle_rad_jit = jit(smallest_principal_angle_rad)

def smallest_principal_angle_deg(A, B):
    """Returns the smallest principal angle between two subspaces in degrees

    Args:
        A (jax.numpy.ndarray): ONB for the first subspace
        B (jax.numpy.ndarray): ONB for the second subspace

    Returns:
        (float): The smallest principal angle between the two subspaces in degrees
    """
    angle = smallest_principal_angle_rad(A, B)
    return jnp.rad2deg(angle)

smallest_principal_angle_deg_jit = jit(smallest_principal_angle_deg)

def smallest_principal_angles_cos(subspaces):
    """Returns the smallest principal angles between each pair of subspaces

    Args:
        A (:obj:`list` of :obj:`jax.numpy.ndarray`): ONBs for the subspaces

    Returns:
        (jax.numpy.ndarray): A symmetric matrix containing the cosine of the 
            smallest principal angles between each pair of subspaces
    """
    k = len(subspaces)
    result = jnp.eye(k)
    for i in range(k):
        A = subspaces[i]
        for j in range(i, k):
            B = subspaces[j]
            angle = smallest_principal_angle_cos_jit(A, B)
            result = result.at[i,j].set(angle)
            result = result.at[j,i].set(angle)
    return result


smallest_principal_angles_cos_jit = jit(smallest_principal_angles_cos)

def smallest_principal_angles_rad(subspaces):
    """Returns the smallest principal angles between each pair of subspaces in radians

    Args:
        A (:obj:`list` of :obj:`jax.numpy.ndarray`): ONBs for the subspaces

    Returns:
        (jax.numpy.ndarray): A symmetric matrix containing the 
            smallest principal angles between each pair of subspaces in radians
    """
    result = smallest_principal_angles_cos(subspaces)
    return jnp.arccos(result)

smallest_principal_angles_rad_jit = jit(smallest_principal_angles_rad)

def smallest_principal_angles_deg(subspaces):
    """Returns the smallest principal angles between each pair of subspaces in degrees

    Args:
        A (:obj:`list` of :obj:`jax.numpy.ndarray`): ONBs for the subspaces

    Returns:
        (jax.numpy.ndarray): A symmetric matrix containing the 
            smallest principal angles between each pair of subspaces in degrees
    """
    result = smallest_principal_angles_rad(subspaces)
    return jnp.rad2deg(result)

smallest_principal_angles_deg_jit = jit(smallest_principal_angles_deg)
