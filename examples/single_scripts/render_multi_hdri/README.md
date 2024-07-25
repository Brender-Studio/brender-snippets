# Render Multi HDRI 

## Name:
render_multi_hdri

## Blender version:
4.2.0 (LTS)

## Description:
Render multiple images from different HDRI files in a blend file.

## Use case:
- [ ] Utility
- [x] Example

## Job type:
- [ ] Array
- [x] Single job

## Entrypoint:
`render_multi_hdri.py`


## Envs:
Use default environment variables by Brender Studio.
- EFS_BLENDER_OUTPUT_PATH
- EFS_BLENDER_FILE_PATH


## Code:

- [render_multi_hdri.py](./render_multi_hdri.py)


## Note:
This script renders multiple images from different HDRI files in a blend file. The script uses the default environment variables provided by Brender Studio to set the output path and the file path. The script can be used as a utility script to render multiple images from different HDRI files in a single job.

If you want to use this script, remember to set up more than one HDRI file in your Blender scene.

You can use custom env variables to set the HDRI file path.

## References (video, repo):
- [N/A]

## Screenshots:
- [N/A]

