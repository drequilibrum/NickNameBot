import tensorflow as tf
from keras.utils import pad_sequences, to_categorical

# open the file nicknames.txt
nicks = open('nicknames.txt', encoding = 'utf-8').read()
nicks = nicks.split('\n')

# denotes the end of sequence
new_nicks = [''.join([item, '#']) for item in new_nicks]

# defining vocabulary and character/integer back and forth dictionaries
vocab = ['<pad>'] + sorted(set(' '.join(new_nicks))) 
vocab_size = len(vocab)
charId = dict([el, i] for i, el in enumerate(vocab))
idChar = dict([i, el] for i, el in enumerate(vocab))

# defining input and output sequences
inp = [item[:-1] for item in new_nicks]
out = [item[1:] for item in new_nicks]

# transforming input and output character sequences to integer sequences 
def char_to_id(name):
    name = [*name]
    name = [charId[item] for item in name]
    return name
inp = list(map(char_to_id, inp))
out = list(map(char_to_id, out))

# padding sequences to a fixed length

inp = pad_sequences(inp, padding = 'post')
out = pad_sequences(out, padding = 'post')
max_seq_len = inp.shape[1]

inp = inp.astype(np.float32)
out = out.astype(np.float32)

# turn input-output pairs into tf Dataset object shuffled and sliced into batches
train_ds = tf.data.Dataset.from_tensor_slices((inp, out)).shuffle( buffer_size = 1000).batch(128)
