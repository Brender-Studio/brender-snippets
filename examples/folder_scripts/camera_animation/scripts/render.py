import bpy


# TODO: Implement use ARRAY SIZE and calculate the number of frames to render based on the array size AWS Batch Job

def render_animation(output_path):
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 250
    bpy.ops.render.render(animation=True)
