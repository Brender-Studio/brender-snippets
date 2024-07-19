# Render Multi camera

## Name:
render_multi_camera

## Blender version:
4.2.0 (LTS)

## Description:
Render multiple images from different cameras in a blend file.

## Use case:
- [x] Utility
- [x] Example

## Job type:
- [ ] Array
- [x] Single job

## Envs:
Use default environment variables by Brender Studio.
- EFS_BLENDER_OUTPUT_PATH
- EFS_BLENDER_FILE_PATH


## Code:

- [render_multi_camera.py](./render_multi_camera.py)


## Note:
This script renders multiple images from different cameras in a blend file. The script uses the default environment variables provided by Brender Studio to set the output path and the file path. The script can be used as a utility script to render multiple images from different cameras in a single job.

Additionally, the script can be used as an example to demonstrate how to render multiple images from different cameras in a blend file using Brender Studio.
To make the script work, remember to set up more than one camera in your Blender scene.

### Use Cases:

1. Architectural Visualization:
   In architectural rendering, it's common to showcase a building or interior design from multiple viewpoints. This script is particularly useful for generating a comprehensive set of renders that highlight different aspects of the design. For example:
   - Exterior shots from various angles (front, back, sides, aerial view)
   - Interior views of key rooms (living room, kitchen, bedrooms)
   - Detail shots of specific architectural features
   By setting up cameras at these strategic points and using this script, architects and designers can quickly generate a full set of presentation images without manually switching between cameras and rendering each view.

2. Product Photography Simulation:
   For product designers and marketers, this script can simulate a professional product photoshoot in a 3D environment. It's especially useful for:
   - Showcasing products from multiple angles (front, back, top, side views)
   - Highlighting specific features with close-up shots
   - Demonstrating scale or context with wider shots
   - Creating consistent product images for e-commerce platforms
   By setting up cameras to mimic different lens types (wide-angle, standard, macro) and positions, designers can generate a comprehensive set of product images that would typically require an extensive physical photoshoot. This approach saves time and resources, especially when working with products that are still in the design phase or when physical prototypes are not yet available.

These use cases demonstrate how the multi-camera rendering script can significantly streamline workflows in architectural visualization and product design, allowing for efficient creation of comprehensive image sets from a single Blender scene.


## Entrypoint:
render_multi_camera.py

## References (video, repo):

## Screenshots:

## Tags:

- Blender
- Render
- Camera
- Multi-camera
- Utility
- Example
