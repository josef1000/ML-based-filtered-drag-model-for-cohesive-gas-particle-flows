# ML-based-filtered-drag-model-for-cohesive-gas-particle-flows

* In this repository all developed and used neural networks in publication J. Tausendschön, S. Sundaresan, M. Salehi, S. Radl, Machine Learning-based filtered drag model for cohesive gas-particle flows, Manuscript submitted in revised form for publication (2023) are stored.

* As stated in the publication anisotropic drag correction is preferred over isotropic, this means that drag correction is calculated in gravitational (typically noted as $z$) and lateral (noted as $x$ or $y$) direction separately.

* All networks have the scaled sub-grid drift velocity $\overline{\phi}_s \ \tilde{v}_d \ / \( u_t \ \phi\_{s,max})$ as their output $z\_{DNN} $. The drag correction function $H_d$ is then calculated, e.g., in gravitational direction by:

$$
H\_{d,z} = 1 +
\begin{cases}
    \frac{\phi\_{s,max} \ u_t } {\overline{\phi}_s \ \tilde{u}\_{sl,z}} z_{DNN,z} & \text{if } 0.01 \leq \overline{\phi}_s \leq 0.55 \\
    0  & \text{else } 
\end{cases}
$$

* The input of the networks is then: $(1 / \Delta^*_f, \ \overline{\phi}_s / \phi\_{s,max}, \ \tilde{u}\_{sl,z}/u_t, \ \nabla_z \ \overline{p}^\*)$ 

* Models developed from 2D as well as from 3D simulations are available. The input data is min-max normalized between -1 and +1, the according values can be found in the text-files in the respective repository.

* The script usageDemo.py shows how to load and compile the saved model, normalize the input and get the prediction based on sample data.
