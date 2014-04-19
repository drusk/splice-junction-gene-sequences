clear

filename='../data/splice.data';

[class,gene,~]=importdata(filename);

accuracy=zeros(10,4);

% priors calculation

nums_ei=0;
nums_ie=0;
nums_nn=0;
C=zeros(3);

for i=1:length(class)
    if class{i}=='EI'
        nums_ei=nums_ei+1;
    elseif class{i}=='IE'
        nums_ie=nums_ie+1;
    else nums_nn=nums_nn+1;
    end
end

P_EI=nums_ei/length(class);
P_IE=nums_ie/length(class);
P_N=nums_nn/length(class);


 k=3;
 iter=1;

%     
for runs=1:10

[gene_train,class_train,gene_test,class_test]=train_test(gene, class,10); % get train and test sets with ratio train / test

n=length(gene_test); 

% k - nearest neighbour

   
for i=1:n
    
a=gene_test{i}; % take i'th test sample

distance=dist_tanimoto(a, gene_train); % calculate distances to train sets

[distance,ind]=sort(distance, 'ascend'); % sort distance, keep initial index

gene_train_sort=gene_train(ind); % sort gene_train according to associated distance
class_train_sort=class_train(ind);  % sort class_train according to associated distance

class_kn{i,1}=k_nearest_calc(class_train_sort,k); % assign class as for the k-nearest neighbour

end


% accuracy calculation
correct=0;
for i=1:n
    if class_kn{i}==class_test{i}
        correct=correct+1;
    end
end

accuracy(runs,iter) = 100*correct/n; 

sort_ord={'EI','IE','N'};
C1=confusionmat(class_test,class_kn,'order',sort_ord);
C=C+C1;
end

C=C./runs 
