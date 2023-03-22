# ML-based-filtered-drag-model-for-cohesive-gas-particle-flows

In this repository all developed and used neural networks in publication ..... are stored.

As stated in the publication anisotropic drag correction is preferred over isotropic, this means that drag correction is calculated in gravitational (typically noted as $z$) and lateral (noted as $x$ or $y$) separately.

All NN's have the sub-grid drift velocity $\tilde{v}_d$ as output. The drag correction function $H_d$ is then calculated by

$$
H_d = 1 +
\begin{cases}
    \phi\_{s,max} \ u_t \ / \ (\overline{\phi}_s \ \tilde{v}_d) & \text{if } 0.01 \leq \overline{\phi}_s \leq 0.55 \\
    0  & \text{else } 
\end{cases}
$$


The NN's differ in their input:

(i) for four marker networks: $f_{DNN} (1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*)$ 

(ii) for five marker networks: $f_{DNN} (1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*, \ Bo)$ 

(iii) for six marker networks: $f_{DNN} (1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*, \ \dot{\gamma}_s)$ 

or $f_{DNN} (1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*, \ \dot{\gamma}\_{sl})$ 

or $f_{DNN} (1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*, \ |\tilde{u}\_{sl,xy}|)$ 
