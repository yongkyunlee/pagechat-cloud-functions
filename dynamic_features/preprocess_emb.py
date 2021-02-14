import numpy as np
import pandas as pd
import torch
import json
from sentence_transformers import SentenceTransformer

def main():
    embed = SentenceTransformer('bert-base-nli-cls-token')
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(device)
    embed = embed.to(device)
    data = pd.read_csv('uci-news-aggregator.csv')

    encoded = embed.encode(list(data['TITLE']))

    x = json.dumps(encoded.tolist())
    
    with open('embed.json', 'w') as f:
        f.write(x)

    f.close()

if __name__ == '__main__':
    main()