from predict import DynamicFeatures

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

if __name__ == '__main__':
	main(sys.argv[1], sys.arv[2])