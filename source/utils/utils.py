import tensorflow as tf

def read_text2tf(paths):
    return tf.data.TextLineDataset(path)


def create_vocabulary(data)
    tokenizer = tfds.features.text.Tokenizer()
    vocabulary_set = set()
    for text_tensor in all_labeled_data:
        some_tokens = tokenizer.tokenize(text_tensor.numpy())
    vocabulary_set.update(some_tokens)
    vocab_size = len(vocabulary_set)
    return vocabulary_set, vocab_size