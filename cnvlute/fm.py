import numpy as np

def fmpartial(f1, f2, f3, times1, levels1, times2, levels2, times3, levels3):
    pass

def linenv(samples, values):
    n = int(samples / float(len(values) - 1))
    env = [np.linspace(start, end, n) for (start, end) in zip(values[:-1], values[1:])]
    env = reduce(lambda s1, s2: np.concatenate(s1, s2), env)
    if len(env) > samples:
        env = env[:samples - len(env)]
    if len(env) < samples:
        np.pad(env, [0, samples - len(env)], 'constant')
    return env
