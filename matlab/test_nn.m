
clear
filename='../data/splice.data';

[class,gene,~]=importdata(filename);

[gene_train,class_train,gene_test,class_test]=train_test(gene, class,50); % get train and test sets

n=length(gene_test); 

% nearest neighbour

for i=1:n
    
a=gene_test{i}; % take i'th test sample

distance=dist_calc_gauss(a, gene_train); % calculate distances to train sets

[distance,ind]=sort(distance, 'ascend'); % sort distance, keep initial index

gene_train_sort=gene_train(ind); % sort gene_train according to associated distance
class_train_sort=class_train(ind);  % sort class_train according to associated distance

class_nn{i,1}=class_train_sort{1}; % assign class as for the nearest neighbour

end

% accuracy calculation
correct=0;
for i=1:n
    if class_nn{i}==class_test{i}
        correct=correct+1;
    end
end

accuracy = 100*correct/n



