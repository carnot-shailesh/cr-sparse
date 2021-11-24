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


from typing import NamedTuple


import jax.numpy as jnp

class FOCSOptions(NamedTuple):
    """Options for FOCS driver routine
    """
    nonneg : bool = False
    "Whether output is expected to be non-negative"
    solver : str = 'at'
    "Default first order conic solver"
    max_iters: int = 100
    "Maximum number of iterations for the solver"
    tol: float = 1e-8
    "Tolerance for convergence"
    L0 : float = 1.
    "Initial estimate of Lipschitz constant"
    Lexact: float = jnp.inf
    "Known bound of Lipschitz constant"
    alpha: float = 0.9
    "Line search increase parameter, in (0,1)"
    beta: float = 0.5
    "Backtracking parameter, in (0,1). No line search if >= 1"
    mu: float = 1
    "Strong convexity parameter"


class FOCSState(NamedTuple):
    """
    State of the FOCS method
    """
    L : float
    "Lipschitz constant estimate"
    theta: float
    ""
    x: jnp.ndarray
    ""
    A_x : jnp.ndarray
    z : jnp.ndarray
    A_z: jnp.ndarray
    f_v : float
    f_x : float
    C_x : float
    g_x: jnp.ndarray
    g_Ax: jnp.ndarray
    

