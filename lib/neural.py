import numpy as np
import scipy.io.wavfile as wav
from sklearn.neural_network import MLPRegressor
import sounddevice as sd
import sys
import pickle
import bz2


class Model:
    def __init__(self, n_hidden, n_output, sampling_rate):
        self.n_hidden = n_hidden
        self.n_output = n_output
        self.sampling_rate = sampling_rate
        self.model = MLPRegressor(hidden_layer_size=(n_hidden, n_output))

    def train(self, data):
        self.model = self.model.fit(data, data)

    def play(self, wave):
        sd.play(self.model.predict(np.array([wave]))[0])
        

if __name__ == '__main__':
    files = sys.argv[1]
    max_len = int(sys.argv[2])
    n_hidden = int(sys.argv[3])
    model_file = sys.argv[4]
    model = MLPRegressor(hidden_layer_sizes=(n_hidden, max_len))
    X = data
    y = np.array(data)
    model = model.fit(X, y)
    prediction = model.predict(data)
    with bz2.BZ2File(model_file, 'wb') as fd:
        pickle.dump(model, fd, protocol=pickle.HIGHEST_PROTOCOL)
