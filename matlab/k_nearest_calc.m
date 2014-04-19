function class=k_nearest_calc(class_train_sort,k)

% pick k nearest classes and assisgn the one that is counted more

ref=unique(class_train_sort);
class_train=class_train_sort{1:k};
for i=1:length(ref)
    count=find(class_train==ref{i});
    vote(i)=length(count);
end

[vote,ind]=sort(vote, 'descend'); % sort votes, keep initial index

ref=ref(ind); 

class=ref{1}; % assign class that is voted more
end
