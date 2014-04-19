clear 
close all

[~, ~, results10_90] = xlsread('D:\UVIC\535 pattern rec\Project\results.xls','results','B4:F8');
[~, ~, results50_50] = xlsread('D:\UVIC\535 pattern rec\Project\results.xls','results','B11:F15');
[~, ~, results90_10] = xlsread('D:\UVIC\535 pattern rec\Project\results.xls','results','B18:F22');
results = [results10_90;results50_50;results90_10;];
results(cellfun(@(x) ~isempty(x) && isnumeric(x) && isnan(x),results)) = {''};

row=[2;7;12];
figure
for i=1:3

k=row(i);
l1(1:4)=results{k,2:end}; % black
gauss(1:4)=results{(k+1),2:end}; % red 
kno(1:4)=results{(k+2),2:end}; % green
tanimo(1:4)=results{(k+3),2:end}; % blue

plot (l1,'k')
hold on
plot (gauss,'r')
hold on
plot (kno, 'g')
hold on
plot (kno, 'b')
hold on
% axis([0 4 50 100])

end

grid on
hold off