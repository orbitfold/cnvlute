import numpy as np
from functools import reduce
from scipy.optimize import differential_evolution
from scipy.optimize import minimize
import numpy.fft as fft
import random


def de(wave, sampling_rate, cr, f):
    a = np.array([0 for _ in range(40)])
    b = np.array([22050 for _ in range(20)] + [20 for _ in range(20)])
    population = [np.random.uniform(a, b, 40) for _ in range(100)]
    best_fitness = np.inf
    best_x = None
    for iteration in range(1000):
        for i, x_ in enumerate(population):
            y = np.array(x_)
            remainder = population[:i] + population[i + 1:]
            random.shuffle(remainder)
            a_, b_, c_ = remainder[:3]
            index = np.random.uniform(0.0, 1.0, len(population[0])) < cr
            y[index] = (a_ + f * (b_ - c_))[index]
            old_fitness = fm_fitness(y, wave, sampling_rate)
            new_fitness = fm_fitness(x_, wave, sampling_rate)
            if new_fitness < best_fitness:
                best_fitness = new_fitness
                best_x = y
            if fm_fitness(y, wave, sampling_rate) < fm_fitness(x_, wave, sampling_rate):
                population[i] = y
        print(best_fitness)
    return best_x


def diff_evol(wave, sampling_rate):
    def callback(xk, convergence):
        print(xk)
        print(fm_fitness(xk, wave, sampling_rate))
        print(convergence)
    a = [0 for _ in range(40)]
    b = [22050 for _ in range(20)] + [20 for _ in range(20)]
    bounds = list(zip(a, b))
    res = differential_evolution(fm_fitness, bounds, args=(wave, sampling_rate), tol=0.01, popsize=1, callback=callback, polish=False)
    print(res.fun)
    return fmpartial(res.x, len(wave), sampling_rate)


def nelder_mead(wave, sampling_rate):
    a = [0 for _ in range(40)]
    b = [22050 for _ in range(20)] + [20 for _ in range(20)]
    init = np.random.uniform(a, b)
    res = minimize(fm_fitness, init, args=(wave, sampling_rate))
    print(res.fun)
    return fmpartial(res.x, len(wave), sampling_rate)


def fmpartial(x, samples, sampling_rate):
    x = np.split(x, 4)
    phasor = np.linspace(0, 2.0 * np.pi, samples)
    f1s = (samples / float(sampling_rate)) * linenv(samples, x[0])
    f2s = (samples / float(sampling_rate)) * linenv(samples, x[1])
    return np.sin(phasor * f1s + np.sin(phasor * f1s) * linenv(samples, x[2])) *\
      linenv(samples, x[3])


def fm_fitness(x, wave, sampling_rate):
    guess = fmpartial(x, len(wave), sampling_rate)
    wave = fft.fft(wave)
    guess = fft.fft(guess)
    diff = wave - guess
    diff = np.sqrt((diff * diff).sum())
    return np.absolute(diff)


def linenv(samples, values):
    n = int(samples / float(len(values) - 1))
    env = np.concatenate([np.linspace(start, end, n) for (start, end) in zip(values[:-1], values[1:])])
    if len(env) > samples:
        env = env[:samples - len(env)]
    if len(env) < samples:
        env = np.pad(env, [0, samples - len(env)], 'constant')
    return env
