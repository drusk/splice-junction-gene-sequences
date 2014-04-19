
function [gene_train,class_train,gene_test,class_test]=...
    train_test(gene, class,ratio)

% generate trainig set

% input: ratio - training/test instances in %. So ratio = 10 
% means training on 10%, testing on 90%

rng('shuffle') % shuffle differently each time
n=length(gene);
split=floor(ratio*n/100);

ind=randperm(n);
gene=gene(ind); % shuffled
class=class(ind);

gene_train=gene(1:split);
class_train=class(1:split);

gene_test=gene((split+1):n);
class_test=class((split+1):n);

end


