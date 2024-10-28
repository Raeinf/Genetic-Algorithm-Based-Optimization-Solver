import numpy as np


def calc_fitness(pop, coeffs):
    x, y, z = pop[:, 0], pop[:, 1], pop[:, 2]
    return coeffs[0] * x + coeffs[1] * y**2 + coeffs[2] * z**3 - coeffs[3]


def init_population(pop_size, init_low, init_high):
    return np.random.uniform(low=init_low, high=init_high, size=(pop_size, 3))


def mutate_pop(pop, mut_range):
    mut_factors = np.random.uniform(low=mut_range[0], high=mut_range[1], size=pop.shape)
    return pop * mut_factors


def find_solution(
    coeffs,
    tolerance=1e-5,
    pop_size=1000,
    mut_range=(0.9, 1.1),
    init_low=0.0,
    init_high=10000.0,
):
    gen_count = 1
    pop = init_population(pop_size, init_low, init_high)
    while True:
        fitness = np.abs(calc_fitness(pop, coeffs))
        sorted_indices = np.argsort(fitness)
        best_fitness = fitness[sorted_indices[:100]]
        best_pop = pop[sorted_indices[:100]]

        print("Gen:", gen_count)
        print("Score :", best_fitness[0])
        print("****")
        gen_count += 1

        if best_fitness[0] <= tolerance:
            return best_pop[0]

        new_pop = np.vstack([best_pop] * 100)
        pop = mutate_pop(new_pop, mut_range)


if __name__ == "__main__":
    coeffs = (1, 2, 3, 36)

    # Execute genetic algorithm to find the solution
    solution = find_solution(coeffs)
    print("result x: ", solution[0], "y: ", solution[1], "z: ", solution[2])
