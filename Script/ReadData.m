clc
clear

tic;

%读取python文件，每次读取刷新前次保存的python
clear classes
obj = py.importlib.import_module('ReadData');
py.importlib.reload(obj);

%调用python代码读取fluent保存的.cas和.dat文件
%将读取的流场信息赋值给dataset
fprintf('Reading fluent data file ...\n\n');
%读取的fluent文件请放在在平行于HDSS文件夹位置的Data文件夹下
%因为github传不了大文件喵
dataset = py.ReadData.transf_to_matlab("../Data/-2.cas");
toc;
fprintf('Finish reading!\n\n');