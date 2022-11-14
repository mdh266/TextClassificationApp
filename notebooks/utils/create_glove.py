import os
import numpy as np
from typing import List, Dict

def create_embedding_matrix(
    path: str, 
    dim: int,
    voc: List[str],
    word_index: Dict[str,int]
) -> np.ndarray:
    
    if not dim in (50, 100, 200, 300):
        raise Exception("Need embedding dim to be in (50, 100, 200, 300)")
        
    path_to_glove_file = os.path.join(path, f"glove.6B.{dim}d.txt")
        
    embeddings_index = {}
    with open(path_to_glove_file) as f:
        for line in f:
            word, coefs = line.split(maxsplit=1)
            coefs = np.fromstring(coefs, "f", sep=" ")
            embeddings_index[word] = coefs

    num_tokens = len(voc) + 2
    embedding_dim = dim
    hits = 0
    misses = 0

    # Prepare embedding matrix
    embedding_matrix = np.zeros((num_tokens, embedding_dim))
    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            # Words not found in embedding index will be all-zeros.
            # This includes the representation for "padding" and "OOV"
            embedding_matrix[i] = embedding_vector
            hits += 1
        else:
            misses += 1
    
    return embedding_matrix