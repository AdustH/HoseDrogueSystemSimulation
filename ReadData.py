import pyvista 
import numpy 
import pyvista
import numpy
#使用pyvista库从目标文件夹中读取fluent保存的.cas和.dat文件
#因为pyvista的Unstructured Grid类型无法在simulink中作为参数传递
#所以这里将dataset设定为本程序下的全局变量，
dataset = pyvista.read("../data/gan20.cas")
# 上行保读取的文件类型是分块网格，需要将其合并成非结构网格
dataset = dataset.combine()

def get_pressure( x, y, z):
 # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]))
        # 使用probe方法获取压力值
        # return dataset.probe(poly_data)["PRESSURE"][0]
        return poly_data.sample(dataset)["PRESSURE"][0]
   
def get_velocity_x(x, y, z):
        # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]));
        return poly_data.sample(dataset)["X_VELOCITY"][0]

def get_velocity_y(x, y, z):
        # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]));
        return poly_data.sample(dataset)["Y_VELOCITY"][0]

def get_velocity_z(x, y, z):
        # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]));
        return poly_data.sample(dataset)["Z_VELOCITY"][0]

def get_temperature(x, y, z):
        # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]))
        return poly_data.sample(dataset)["TEMPERATURE"][0]

def get_density(x, y, z):
        # 创建PolyData对象，包含指定坐标的单个点
        poly_data = pyvista.PolyData(numpy.array([[x, y, z]]));
        return poly_data.sample(dataset)["DENSITY"][0]