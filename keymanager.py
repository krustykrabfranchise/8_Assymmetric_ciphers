import os
import pickle

def save_key(filename, key):
    with open(filename, 'wb') as f:
        pickle.dump(key, f)

def get_key(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def make_keys():
    private_key = os.urandom(16)
    public_key = os.urandom(16)
    
    return private_key, public_key

source_private = "private.pem"
source_public = "public.pem"

if not os.path.exists(source_private) or not os.path.exists(source_public):
    private_key, public_key = make_keys()
    save_key(source_private, private_key)
    save_key(source_public, public_key)
else:
    private_key = get_key(source_private)
    public_key = get_key(source_public)
