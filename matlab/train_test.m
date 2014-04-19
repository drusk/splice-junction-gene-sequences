
function [gene_train,class_train,gene_test,class_test]=...
    train_test(gene, class,ratio)

% generate trainig set

% input: ratio - training/test instances in %. So ratio = 10 
% means training on 10%, testing on 90%

rng('shuffle') % shuffle differently each time

gene_train = [];
class_train = [];
gene_test = [];
class_test = [];

unique_classes = unique(class);
for i=1:length(unique_classes)
    class_val = unique_classes(i);
    
    indices = find(ismember(class,class_val));
    [current_gene_train, current_class_train, ...
        current_gene_test, current_class_test] = ...
        split(gene(indices), class(indices), ratio);
    
    gene_train = extend(gene_train, current_gene_train);
    class_train = extend(class_train, current_class_train);
    gene_test = extend(gene_test, current_gene_test);
    class_test = extend(class_test, current_class_test);
end

end

function [gene_train, class_train, gene_test, class_test] = ...
    split(gene, class, ratio)

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

function extended = extend(matrix1, matrix2)
    extended = [matrix1; matrix2];
end