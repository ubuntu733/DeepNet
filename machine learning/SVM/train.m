clear;
load('train1.mat');
[m,n]=size(test);
c=0.6;
tol=0.002;
traindata=test;
trainlabel=label;
svm=SMO(traindata,trainlabel,c,tol);
svm.train(100);