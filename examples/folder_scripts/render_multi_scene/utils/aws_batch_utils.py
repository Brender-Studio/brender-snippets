import os

def get_aws_batch_info():
    output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    # array_size = int(os.environ.get('AWS_BATCH_JOB_ARRAY_SIZE', 1))
    # job_index = int(os.environ.get('AWS_BATCH_JOB_ARRAY_INDEX', 0))
    render_type = os.environ.get('RENDER_TYPE', 'auto').lower()  # 'auto', 'frame', or 'animation'
    
    return output_path, render_type