% 对矩阵进行强度归一化
inputPath = './ML-Denoised/';
output = './Norm-ML/';
if ~exist(output, 'dir')
    mkdir(output);
end
load('./sumstd-20211211.mat')
n = 8;
for n1=1:n
    load([inputPath num2str(n1) '.mat'])
    Fn1 = im2double(F);
    Fn1 = Fn1 / sum(sum(Fn1)) * sumstd;
    F = Fn1;
    save([output num2str(n1) '.mat'],'F')
end
