def generate_name(model, start):
    chars = list(start)
    c = 0
    i = 0
    while c != '#':
        ids = [charId[char] for char in chars]
        ids_padded = pad_sequences([ids], value = 0.0, padding = 'post', maxlen = max_seq_len)
        probs = tf.nn.softmax(model.predict(ids_padded, verbose = 0))[0][i].numpy()
        probs = probs/sum(probs)
        d = np.random.choice(vocab_size, p = probs)
        if d != 0:
            c = idChar[d]
            chars.append(c)
            i = i + 1 
    print(''.join(chars).replace('#',''))
def print_on_epoch(epoch,_):
    if epoch % 5 == 0:
        
        print('Names generated after epoch {}:\n'.format(epoch))

        for i in range(5):
            generate_name(model)
name_generator = LambdaCallback(on_epoch_end = print_on_epoch)

model.fit(train_ds, epochs = 300, callbacks=[name_generator], verbose = 1)
