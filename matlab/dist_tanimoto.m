function distance=dist_tanimoto(a, gene_train)

% input: a - test sample, gene_train -  train set
n=length(gene_train); 
m=length(a);
distance=zeros(n,1);

for i=1:n
    count=0;
    train=gene_train{i};
    for j=1:m
        if a(j)==train(j)
            count=count+1;
        end
    end
    distance(i)=(2*m-2*count)/(2*m-count); % distance from test sample to i'th train sample
end

end