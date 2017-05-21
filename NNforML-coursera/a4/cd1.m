function ret = cd1(rbm_w, visible_data)
% <rbm_w> is a matrix of size <number of hidden units> by <number of visible units>
% <visible_data> is a (possibly but not necessarily binary) matrix of size <number of visible units> by <number of data cases>
% The returned value is the gradient approximation produced by CD-1. It's of the same shape as <rbm_w>.
%    error('not yet implemented');
  visible_data = sample_bernoulli(visible_data);
  hidden_state_0 = sample_bernoulli(visible_state_to_hidden_probabilities(rbm_w, visible_data));
  d0 = configuration_goodness_gradient(visible_data, hidden_state_0);
  %rbm_w = rbm_w .- d0;
  visible_state_1 = sample_bernoulli(hidden_state_to_visible_probabilities(rbm_w, hidden_state_0));
  hidden_state_1 = visible_state_to_hidden_probabilities(rbm_w, visible_state_1);
  d1 = configuration_goodness_gradient(visible_state_1, hidden_state_1);
  ret = d0 - d1;
end
