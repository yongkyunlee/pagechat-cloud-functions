import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
import time


class Contractive_LSTM_AutoEncoder(torch.nn.Module):
    def __init__(self, eparams, dparams):
        super().__init__()
        self.encoder = torch.nn.LSTM(**eparams)
        self.decoder = torch.nn.LSTM(**dparams)


    def forward(self, inp):
        # inp: [k, bs, d_sentence_emb]
        enc_out = self.encoder(inp)[0] # [k, bs, d_hidden]
        dec_out = self.decoder(enc_out)[0] # [k, bs, d_sentence_emb]
        return enc_out, dec_out