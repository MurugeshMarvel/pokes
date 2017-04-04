import theano.tensor as T
import theano

class rnn:
	def __init__(self, inp_dim, out_dim, hidden_no, act_func = 'tanh'):
		self.inp_dim = inp_dim
		self.out_dim = out_dim
		self.hidden_no = hidden_no
		