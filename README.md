# VortexLab — Quantum Fluid Simulation

This project implements a numerical simulator for vortex dynamics in Bose–Einstein condensates using the Gross–Pitaevskii equation (GPE).

## Technologies Used

- **Language:** Python 3.x
- **Libraries:** NumPy (FFT), Matplotlib (Visualization and Animation), Tkinter (GUI)
- **Numerical Method:** Split-Step Fourier Method (SSFM)

## Features

- Simulation of topological vortices on grids up to 256×256
- Real-time graphical interface for transport and interaction control
- Edge stabilization using fourth-order absorbing boundary masks
- Experimental framework for studying nonlinear and topological dynamics

## Running the Project

### 1. Install dependencies

```bash
pip install numpy matplotlib
```

### 2. Run the main application

```bash
python3 main.py
```

## Project Goals

The project explores:
- vortex stability,
- topological defect dynamics,
- transport phenomena,
- and numerical behavior in discretized quantum fluid systems.

## Project Status

Experimental computational physics framework under active development.
