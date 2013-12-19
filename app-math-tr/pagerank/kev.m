K = 4
  
T = [1/4 2/4 0 0 1/4
     1/6 0 2/6 1/6 2/6
     0 0 0 2/4 2/4
     1/8 0 0 4/8 3/8
     0 1/2 0 1/2 0];

[evecs,evals]=eig(T');
pi=evecs(:,1) ./ sum(evecs(:,1))

pi = ones(1,K+1) / (eye(K+1) - T + ones(K+1,K+1))

x=[.5 .3 .1 .1 0];
pi = x*(T^20)
