# Genetic-Algorithm-Based-Optimization-Solver

This Python project implements a genetic algorithm to solve optimization problems by iteratively evolving a population to find a solution within a given tolerance level. The algorithm optimizes values of \(x\), \(y\), and \(z\) in a function to achieve a target fitness score, using customizable coefficients.

## Project Overview

The algorithm uses principles of genetic algorithms, including:
1. **Population Initialization**: Generating an initial population of potential solutions.
2. **Fitness Calculation**: Evaluating each individual’s fitness based on a target function.
3. **Selection and Mutation**: Selecting top-performing individuals and applying mutations to simulate evolution.

The goal is to find values for \(x\), \(y\), and \(z\) that satisfy the function:
\[
f(x, y, z) = c_1 \cdot x + c_2 \cdot y^2 + c_3 \cdot z^3 - c_4
\]
where \(c_1, c_2, c_3, c_4\) are coefficients provided as inputs.
