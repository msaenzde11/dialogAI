from preprocessing.preprocessing import Preprocessor
from settings import PATHS

def apply_preprocessing(sent, p):
    p.set_text(sent)
    return p.get_text()

if __name__ == "__main__":

    with open(PATHS['TEXT_PATH'], 'r', encoding='utf-8') as f:
        data = f.read().splitlines() 
    
    p = Preprocessor()
    data_prep_encoder = [apply_preprocessing(x,p) for x in data]