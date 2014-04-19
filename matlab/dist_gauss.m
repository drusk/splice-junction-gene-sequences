function distance=dist_gauss(a, gene_train)

% input: a - test sample, gene_train -  train set
n=length(gene_train); 

distance=zeros(n,1);

for i=1:n
    dist=0;
    train=gene_train{i};
    for j=1:length(a)
        if a(j)==train(j)
           sigma=1;
        else
           sigma=0;            
        end
        weight=exp(-((j-30).^2)/20);
        dist=dist+weight*(1-sigma);
    end
    % distance from test sample to i'th train sample
    distance(i)=dist; 
end

end