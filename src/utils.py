import numpy as np


def pad_data(data):
    for index, wave in enumerate(data):
        if wave.shape[0] > max_len:
            data[index] = wave[0:max_len]
        if wave.shape[0] < max_len:
            data[index] = np.pad(wave, [0, max_len - wave.shape[0]], 'constant')


def load_files(filename):
    with open(filename, 'r') as fd:
        filelist = [fname.strip() for fname in fd]
    data = [np.array(wav.read(filename)[1]) for filename in filelist]
    data = [wave / float(np.absolute(wave).max()) for wave in data]
    data = np.array(data)
    return data

    
def downsample(wave, n):
    """
    wave - numpy array
    """
    # Brickwall filter to reduce aliasing.
    wave_fft = np.fft.fft(wave)
    wave_fft = wave_fft[0:(wave_fft.shape[0] / n)]
    wave = np.fft.ifft(wave_fft)
    return wave[::n]
