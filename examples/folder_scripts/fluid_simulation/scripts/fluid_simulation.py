import bpy

def setup_fluid_simulation():
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    domain = bpy.context.object
    bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
    domain.modifiers['Fluid'].fluid_type = 'DOMAIN'

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
    flow = bpy.context.object
    bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
    flow.modifiers['Fluid'].fluid_type = 'FLOW'
    flow.modifiers['Fluid'].flow_settings.flow_type = 'SMOKE'
