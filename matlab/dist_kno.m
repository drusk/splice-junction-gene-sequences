function distance=dist_kno(a, gene_train)

% input: a - test sample, gene_train -  train set
n=length(gene_train); 

distance=zeros(n,1);

for i=1:n
    % exon-intro
    count1=0;
    train=gene_train{i};
    for j=28:36
        if j==28
            if and( or(a(j)=='A' , a(j)=='C') ,...
                    or(train(j)=='A' , train(j)=='C'))
                
                count1=count1;
            else 
                count1=count1+1;
            end         
        elseif j==33
            if and(or(a(j)=='A', a(j)=='G' ) , ...
                    or(train(j)=='A' , train(j)=='G'))
                
                count1=count1;
            else 
                count1=count1+1;
            end
        elseif a(j)~=train(j)
            count1=count1+1;
        end
    end
    % intro-exon
    count2=0;
    for j=21:32
        if j==27
            count2=count2;
        elseif j>=21 & j<=28
            if and(or(a(j)=='T' , a(j)=='C' ) ,...
                    or(train(j)=='T' , train(j)=='C'))
                
                count2=count2;
            else 
                count2=count2+1;
            end         
        elseif j==32
            if and(or(a(j)=='T' , a(j)=='G' ) ,...
                    or(train(j)=='T' , train(j)=='G'))
                
                count2=count2;
            else 
                count2=count2+1;
            end
        elseif a(j)~=train(j)
            count2=count2+1;
        end
    end
    % distance from test sample to i'th train sample is chosen as least
    % between distances to EI and IE classes. priors for EI and IE are the
    % same, equal amount in original dataset so error rates to
    % classify EI / IE should be the same. we don't take into
    % account class 'none' when there is no split. possible source of
    % additional error. could be improved, if you look into gene sequence
    
    distance(i)=min(count1,count2);
    
end

end