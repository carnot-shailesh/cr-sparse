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

"""
CR.Sparse
"""

from .version import __version__

from cr.sparse._src.util import (
    promote_arg_dtypes
)

from cr.sparse._src.matrix import (
    transpose,
    hermitian,
    is_matrix,
    is_square,
    is_symmetric,
    is_hermitian,
    is_positive_definite,
    has_orthogonal_columns,
    has_orthogonal_rows,
    has_unitary_columns,
    has_unitary_rows,
)

from cr.sparse._src.norm import (
    norms_l1_cw,
    norms_l1_rw,
    norms_l2_cw,
    norms_l2_rw,
    norms_linf_cw,
    norms_linf_rw,
    sqr_norms_l2_cw,
    sqr_norms_l2_rw,


    normalize_l1_cw,
    normalize_l1_rw,
    normalize_l2_cw,
    normalize_l2_rw,
)

from cr.sparse._src.distance import (
    pairwise_sqr_l2_distances_rw,
    pairwise_sqr_l2_distances_cw,
    pairwise_l2_distances_rw,
    pairwise_l2_distances_cw,
    pdist_sqr_l2_rw,
    pdist_sqr_l2_cw,
    pdist_l2_rw,
    pdist_l2_cw,
    # Manhattan distances
    pairwise_l1_distances_rw,
    pairwise_l1_distances_cw,
    pdist_l1_rw,
    pdist_l1_cw,

    # Chebychev distance
    pairwise_linf_distances_rw,
    pairwise_linf_distances_cw,
    pdist_linf_rw,
    pdist_linf_cw
)

from cr.sparse._src.discrete.number import (
    is_integer,
    is_positive_integer,
    is_negative_integer,
    is_odd,
    is_even,
    is_odd_natural,
    is_even_natural,
    is_power_of_2,
    is_perfect_square,
    integer_factors_close_to_sqr_root
)

from cr.sparse._src.signal import (
    nonzero_values,
    nonzero_indices,
    randomize_rows,
    randomize_cols,
    largest_indices,
    hard_threshold,
    sparse_approximation,
    build_signal_from_indices_and_values,

    # row wise
    largest_indices_rw,
    take_along_rows,
    sparse_approximation_rw,

    # column wise
    largest_indices_cw,
    take_along_cols,
    sparse_approximation_cw,
)

from cr.sparse._src.signal import (

    find_first_signal_with_energy_le_rw,
    find_first_signal_with_energy_le_cw,
)


from cr.sparse._src.signalcomparison import (
    SignalsComparison,
    snrs_cw,
    snrs_rw
)
