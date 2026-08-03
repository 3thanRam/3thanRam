# Ethan Ramsey

**Scientific machine-learning researcher working on structure-preserving
models, learned dynamics, and uncertainty in complex physical systems.**

My background is in theoretical physics, including quantum field theory,
particle physics, nonlinear dynamics, solitons, Monte Carlo methods, and
scientific computing.

I develop reproducible PyTorch experiments with controlled baselines,
multi-seed evaluation, calibrated metrics, and explicit reporting of
negative or inconclusive results. My current interests include:

- learned contour deformation and sign problems in lattice field theory;
- self-supervised world models for scientific systems;
- adaptive mathematical inductive biases;
- hierarchical and iterative latent representations; and
- uncertainty and failure detection in learned scientific models.

## Selected research

### [General Trajectory Stability Probe](https://github.com/3thanRam/General-trajectory-stability-probe)

Tests whether perturbation-derived hidden-state instability identifies
token errors beyond predictive entropy. Two particle-seed evaluations
gave AUROC differences of +0.00017 and -0.00031, providing no current
evidence of a robust advantage.

The project includes deterministic data splits, unperturbed controls,
calibration metrics, checkpoint resumption, and locked evaluation
procedures.

### [ThimbleML](https://github.com/3thanRam/ThimbleML)

A PyTorch research prototype for learning holomorphic contour
deformations of oscillatory complex integrals. The implementation uses
analytical complex Jacobians, exact low-dimensional references, and
collapse-aware importance-sampling diagnostics.

A preregistered three-architecture, three-seed experiment produced a
uniform negative result: all variants eventually underwent held-out
importance-weight collapse. The project therefore identifies a failure
of the shared phase-focused objective rather than claiming a successful
solution to the sign problem.

### [FlowReasoning](https://github.com/3thanRam/FlowReasoning)

A controlled study of repeated shared computation in a compact
language model. Four applications of a shared latent operator improved
validation BPC from 3.008 ± 0.090 to 2.501 ± 0.019 in a three-seed
Tiny Shakespeare experiment. Learned parallel branches were slower and
performed worse, providing a useful negative result for that mechanism.

This project motivates my interest in iterative and hierarchical latent
dynamics, while remaining explicit that the current benchmark tests
next-character prediction rather than reasoning.

## Scientific background

- Two completed second-year Master's programmes in fundamental and
  theoretical physics
- Quantum field theory, particle physics, nonlinear dynamics, and solitons
- Symbolic FFTLog infrastructure for redshift-space galaxy skew spectra
  during a research internship at LAPTh
- C++ Monte Carlo implementation for pure SU(2) lattice gauge theory
- Numerical work on Casimir energies and stochastic annihilation systems

## Future research direction (not yet implemented)

I am interested in combining these lines of work through adaptive
structure-preserving world models. One possible direction is a
JEPA-like scientific model whose predictor contains a holomorphic
component and a general residual, with an explicit penalty measuring
when the model departs from complex analytic structure.


<img
  align="right"
  src="https://raw.githubusercontent.com/3thanRam/3thanRam/assets/animationfull.gif"
  width="20%"
/>
