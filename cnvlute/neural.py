import numpy as np
import scipy.io.wavfile as wav
from scipy import signal
from sklearn.neural_network import MLPRegressor
import sounddevice as sd
import sys
import pickle
import bz2
import cnvlute


class Model:
    def __init__(self, n_hidden, n_output, sampling_rate, downsample):
        self.n_hidden = n_hidden
        self.n_output = n_output
        self.sampling_rate = int(sampling_rate / float(downsample))
        self.model = MLPRegressor(hidden_layer_sizes=(n_hidden, n_output))

        
    def train(self, data):
        self.model = self.model.fit(data, data)
        prediction = self.model.predict(data)


    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction

        
    def play(self, wave):
        if (wave.shape[0] > self.n_output):
            wave = wave[:self.n_output]
        if (wave.shape[0] < self.n_output):
            np.pad(wave, [0, self.n_output], 'constant')
        sd.play(self.model.predict(np.array([wave]))[0])

        
    def process(self, input_file, output_file):
        cnvlute.utils.loadfile(input_file)
        if (wave.shape[0] > self.n_output):
            wave = wave[:self.n_output]
        if (wave.shape[0] < self.n_output):
            np.pad(wave, [0, self.n_output], 'constant')
        wav.write(output_file, self.model.predict(np.array([wave]))[0], srate)

        
    def store(self, filename):
        with open(filename, 'wb') as fd:
            pickle.dump(self, fd, protocol=pickle.HIGHEST_PROTOCOL)        
        

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
