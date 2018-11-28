import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft, ifft


def equalize_size(wav1, wav2):
    if wav1.shape[0] > wav2.shape[0]:
        return wav1, pad_data(wav2, wav1.shape[0])
    else:
        return pad_data(wav1, wav2.shape[0]), wav2


def pad_data(data, max_len):
    for index, wave in enumerate(data):
        if wave.shape[0] > max_len:
            data[index] = wave[0:max_len]
        if wave.shape[0] < max_len:
            data[index] = np.pad(wave, [0, max_len - wave.shape[0]], 'constant')


def load_file(filename):
    wave = wav.read(filename)
    srate = wave[0]
    wave = wave[1]
    wave = wave / float(np.absolute(wave).max())
    return wave, srate
            

def load_files(filename):
    with open(filename, 'r') as fd:
        filelist = [fname.strip() for fname in fd]
    data = [load_file(filename) for filename in filelist]
    srate = data[0][1]
    data = [wave[0] for wave in data]
    data = np.array(data)
    return data, srate

    
def downsample(wave, n):
    """
    wave - numpy array
    """
    # Brickwall filter to reduce aliasing.
    wave_fft = fft(wave)
    wave_fft = wave_fft[0:int(wave_fft.shape[0] / n)]
    wave = ifft(wave_fft).real
    return wave[::n]
