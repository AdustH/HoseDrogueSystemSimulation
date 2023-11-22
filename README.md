# HoseDrogueSystemSimulation

A simple simulation of a hose-drogue system.

本程序的目标是对本课题组梁师兄做的matlab simulink的一个remake and expand :blush:

	推倒重做的原因是梁师兄原程序需要将fluent保存的.cas导入到tecplot里，用tecplot再导出整整七个.dat文件
	再用一堆matlab脚本进行读取制表传递进simulink
	
前置工作所需文件大概如下图所示:disappointed_relieved:

![Image text](https://github.com/AdustH/img/blob/main/HD_readme_img.png?raw=true)

本人太菜了，matlab纯新手，看了大半天看的头都要晕了:sob:
然后在向室友请教matlab读取上面这个tecplot处理过的.dat文件的过程中，他告诉了我一个神中神的python库pyvista，可以直接读取fluent保存的.cas和.dat:open_mouth:
我去，一段程序全搞定了，太牛啦:laughing:
	
	推倒重做的另一个原因是梁师兄原程序后面提取流场数据的时候采用的是自编的流场搜索方法，即单元网格搜索法
	（源码是课题组祖传的fortran代码，梁师兄把这段在simulink中实现了）
	而通过pyvista库，可以直接通过输入坐标来获取流场信息，导致整个simulink的输入都发生了改变，所以不如索性remake一下
本人编程小白，我很脆弱，写的代码烂不要骂我:confounded:
## 致谢
- 首先感谢我的师兄，**邹gy师兄**，~~有一天他去somewhere偷学了关于simulink的基础概念~~，他希望能够将simulink应用到我们课题组中，所以邹师兄可以算是课题组simulink的**发起人**
- 其次感谢我的师兄，**梁zf师兄**，邹师兄作为编程苦手想要完成这么一个软管锥套的仿真有些许的困难，于是找到了与他同级的梁zf同学，也就是我的梁师兄与他进行协作，负责具体的编程帮他使用matlab实现他的一些ideas。进过小半年艰苦的开发，梁师兄终于整出来了我手中的那一份simulink程序，也是本工程的基础，所以梁师兄可以算是课题组simulink的**奠基人**
- 同时我还要感谢我的室友，[Chenyu Bao](https://github.com/bcynuaa)  ，他太懂编程了:smirk:，我的科研外置大脑，yyds
