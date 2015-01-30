import numpy as np
import itertools

class RBM:
  
  def __init__(self, num_visible, num_hidden, learning_rate = 0.1,\
                 max_epochs = 1000):
    self.num_hidden = num_hidden
    self.num_visible = num_visible
    self.learning_rate = learning_rate
    self.norm_dict = {}
    self.weights = 0.1 * np.random.randn(self.num_visible, self.num_hidden)    
    self.weights = np.insert(self.weights, 0, 0, axis = 0)
    self.weights = np.insert(self.weights, 0, 0, axis = 1)
    self.max_epochs = max_epochs
    self.norm_c = 0

  def fit(self, data):
    num_examples = data.shape[0]

    data = np.insert(data, 0, 1, axis = 1)

    for epoch in range(self.max_epochs):      
      pos_hidden_activations = np.dot(data, self.weights)
      pos_hidden_probs = self._logistic(pos_hidden_activations)
      pos_hidden_states = pos_hidden_probs > \
          np.random.rand(num_examples, self.num_hidden + 1)

      tmp = np.array(pos_hidden_states).astype(float)
      pos_visible_states = self.run_hidden(tmp[:,1:])

      for h,v in itertools.izip(pos_hidden_states.astype(float),
                                pos_visible_states):
        v = np.insert(v, 0, 1)
        self.norm_c += np.dot(np.dot(h.T,self.weights.T), v)
        
      pos_associations = np.dot(data.T, pos_hidden_probs)

      neg_visible_activations = np.dot(pos_hidden_states, self.weights.T)
      neg_visible_probs = self._logistic(neg_visible_activations)
      neg_visible_probs[:,0] = 1 # Fix the bias unit.
      neg_hidden_activations = np.dot(neg_visible_probs, self.weights)
      neg_hidden_probs = self._logistic(neg_hidden_activations)

      neg_associations = np.dot(neg_visible_probs.T, neg_hidden_probs)

      self.weights += self.learning_rate * \
          ((pos_associations - neg_associations) / num_examples)

      error = np.sum((data - neg_visible_probs) ** 2)
          
  def run_hidden(self, data):

    num_examples = data.shape[0]

    visible_states = np.ones((num_examples, self.num_visible + 1))

    data = np.insert(data, 0, 1, axis = 1)

    visible_activations = np.dot(data, self.weights.T)
    visible_probs = self._logistic(visible_activations)
    visible_states[:,:] = visible_probs > \
        np.random.rand(num_examples, self.num_visible + 1)

    visible_states = visible_states[:,1:]
    return visible_states

  def run_visible(self, data):
    num_examples = data.shape[0]
    
    hidden_states = np.ones((num_examples, self.num_hidden + 1))
    
    data = np.insert(data, 0, 1, axis = 1)

    hidden_activations = np.dot(data, self.weights)
    hidden_probs = self._logistic(hidden_activations)
    hidden_states[:,:] = hidden_probs > \
        np.random.rand(num_examples, self.num_hidden + 1)  
    hidden_states = hidden_states[:,1:]
    return hidden_states
  
  def predict_proba(self, X):
    hs = self.run_visible(X)
    hs = np.insert(hs, 0, 1,axis=1)
    res = []
    for i in range(len(X)):
      tmp = np.dot(hs[i],self.weights.T)
      res.append(np.dot(tmp.T,np.insert(X[i], 0, 1)))
    return np.array(res) / self.norm_c
              
  def _logistic(self, x):
    return 1.0 / (1 + np.exp(-x))
