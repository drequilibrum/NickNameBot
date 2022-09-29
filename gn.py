from tensorflow.nn import softmax
from keras.utils import pad_sequences
import pickle
import numpy as np
from mapping import charId, idChar

vocab_size = len(charId)
def generate_name(model, start):
    chars = list(start)
    c = 0
    i = 0
    while c != '#':
        ids = [charId[char] for char in chars]
        ids_padded = pad_sequences([ids], value = 0.0, padding = 'post', maxlen = 30)
        probs = softmax(model.predict(ids_padded, verbose = 0))[0][i].numpy()
        probs = probs/sum(probs)
        d = np.random.choice(vocab_size, p = probs)
        if d != 0:
            c = idChar[d]
            chars.append(c)
            i = i + 1 
    return ''.join(chars).replace('#','')
def print_on_epoch(epoch,_):
    if epoch % 5 == 0:
        
        print('Names generated after epoch {}:\n'.format(epoch))

        for i in range(5):
            generate_name(model)

