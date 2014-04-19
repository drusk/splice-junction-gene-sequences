function distance=dist(a, gene_train)

% input: a - test sample, gene_train -  train set
n=length(gene_train); 

distance=zeros(n,1);

for i=1:n
    count=0;
    train=gene_train{i};
    for j=1:length(a)
        if a(j)~=train(j)
            count=count+1;
        end
    end
    % distance from test sample to i'th train sample
    distance(i)=count; 
end

end