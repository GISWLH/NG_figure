这是一个根据数据绘图的项目，主要绘制图1，图3

运行代码所需的环境base即可，因此运行py代码前无需conda activate环境
我不喜欢定义太过复杂的函数，并运行main函数，我是深度jupyter notebook用户，我喜欢直接的代码，简单的函数定义是可以接受的
使用matplotlib可视化，绘图使用Arial字体，绘图中的图片标记都用英文，Nature Style科研绘图风格
代码都放到code文件夹下
结果图都放到figure

1. 先绘制图3
读取data/Data for main figures.csv
图3是两栏a, b图
左图是SSP2-4.5，x轴是Ocean P -> Q，y轴是Ocean P -> Q的值（分为ESM和EC两个柱，即每个x是两个柱子， #fd8d3c，#bcd6e9），其中两个uncertainty是error bar，相应添加
右图是SSP5-8.5，和a一样