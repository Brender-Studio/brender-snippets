import bpy

def create_camera_path(path_data):
    curve_data = bpy.data.curves.new('CameraPath', type='CURVE')
    curve_data.dimensions = '3D'
    
    spline = curve_data.splines.new('NURBS')
    spline.points.add(len(path_data) - 1)
    
    for i, coord in enumerate(path_data):
        x, y, z = coord
        spline.points[i].co = (x, y, z, 1)

    curve_object = bpy.data.objects.new('CameraPath', curve_data)
    bpy.context.scene.collection.objects.link(curve_object)

    return curve_object
