# ML-based-filtered-drag-model-for-cohesive-gas-particle-flows

In this repository all developed and used neural networks in publication ..... are stored.

As stated in the publication anisotropic drag correction is preferred over isotropic, this means that drag correction is calculated in gravitational (typically noted as $z$) and lateral (noted as $x$ or $y$) separately.

All NN's have the sub-grid drift velocity $\tilde{v}_d$ as output. The drag correction function $H_d$ is then calculated

by $H_d  =  $

The NN's differ in their input:

(i) for four marker networks: $f_{DNN} (1 / \Delta^*_f, \overline{\phi}_s / \phi\_{s,max}, \tilde{u}\_{sl,z}/u_t,$ $\overline{p}^* )$


$\overline{x}^*$
