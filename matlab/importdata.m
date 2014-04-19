function [class,gene, donor]=importdata(name)

formatSpec = '%3s%24s%s%[^\n\r]';
component = textscan(fopen(name,'r'), formatSpec, 'Delimiter', ',', 'WhiteSpace', '               ', 'EmptyValue' ,NaN, 'ReturnOnError', false);
class = component {:,1};
donor = component {:, 2};
gene = component {:,3};

end
