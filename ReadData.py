import pyvista as pv
import numpy as np

def read_dataset(file_path):
    # 读取fluent保存的.cas以及.dat文件
    dataset = pv.read(file_path);
    # 上行保读取的文件类型是分块网格，需要将其合并成非结构网格
    dataset = dataset.combine();
    return dataset

def transf_to_matlab(file_path):
    # 读取fluent保存的.cas以及.dat文件，然后将dataset传递给matlab
    # file_path = "../data/gan20.cas"; 
    dataset = read_dataset(file_path);
    return dataset

def get_pressure(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]));
    # 使用probe方法获取压力值
    #return dataset.probe(poly_data)["PRESSURE"][0]
    return poly_data.sample(dataset)["PRESSURE"][0]

def get_temperature(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]))
    return poly_data.sample(dataset)["TEMPERATURE"][0]

def get_velocity_x(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]));
    return poly_data.sample(dataset)["X_VELOCITY"][0]

def get_velocity_y(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]));
    return poly_data.sample(dataset)["Y_VELOCITY"][0]

def get_velocity_z(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]));
    return poly_data.sample(dataset)["Z_VELOCITY"][0]

def get_density(dataset, x, y, z):
    # 创建PolyData对象，包含指定坐标的单个点
    poly_data = pv.PolyData(np.array([[x, y, z]]));
    return poly_data.sample(dataset)["DENSITY"][0]