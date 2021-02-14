import os
import torch
from sentence_transformers import SentenceTransformer

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

class DynamicFeatures:

	def __init__(self, eparams, dparams, model_path, optim_path):
		assert os.path.isfile(model_path)
		assert os.path.isfile(optim_path)

		self.model = Contractive_LSTM_Autoencoder(**eparams, **dparams)
		self.model.load_state_dict(torch.load(model_path))
		self.embedder = SentenceTransformer('bert-base-nli-cls-token')
		self.encoder = self.model.encoder 

		self.cos_loss = torch.nn.CosineEmbeddingLoss()
		self.optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
		self.optimizer.load_state_dict(torch.load(optim_path))


def main(mp, op):
	p = 0.2

	eparams = {
    'input_size': 768,
    'hidden_size': 128,
    'batch_first': True,
    'num_layers': 2,
    'dropout': p
	}

	dparams = {
	    'input_size': 128,
	    'hidden_size': 768,
	    'batch_first': True,
	    'num_layers': 2,
	    'dropout': p,
	}

	df = DynamicFeatures(eparams, dparams, mp, op)

def update(new_title, feature, model):
	h0 = torch.tensor(feature[:len(feature)//2])
	c0 = torch.tensor(feature[len(feature)//2:])
	assert type(new_title) == str
	emb = model.embedder.encode(new_title).unsqueeze(0)
	_, (h1, c1) = model.encoder(emb, (h0, c0))
	assert h1.size()[0] == model.encoder.num_layers
	return h1[1].squeeze(0).tolist() + c1[1].squeeze(0).tolist()

def feedback(u1, u2, label, model):
	assert label.item() in [-1, 1]

	loss = self.cos_loss(u1, u2, label)
	model.optimizer.zero_grad()
    loss.backward()
    model.optimizer.step()
    return loss


if __name__ == '__main__':
	main(sys.argv[1], sys.arv[2])