import pyvista

filename = "filestl.stl"
filename.split("/")[-1]  # omit the path
'42400-IDGH.stl'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()