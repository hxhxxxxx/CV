首先在run.py 文件中定义了四个阶段
分别是 
set device     启动设备

define model   定义模型
model=TMO().eval()

training stage 训练阶段，调整模型的参数
testing stage  测试阶段，对不同的数据集使用调好的模型来测试结果

