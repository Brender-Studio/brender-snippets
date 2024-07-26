# Job Array Animation Renderer With AWS Batch 

## Name:
Job Array Animation Renderer

## Blender Version:
Blender 4.2 (LTS)

## Detailed Description
This script facilitates distributed animation rendering using AWS Batch Job Array, optimized for integration with <a href="https://www.brenderstudio.com" target="_blank">Brender Studio</a>. It partitions the animation into manageable chunks and assigns each chunk to a separate job within the array, allowing for scalable and parallel processing across multiple compute resources.

Designed as a custom script for <a href="https://www.brenderstudio.com" target="_blank">Brender Studio</a>, this example demonstrates how to configure and execute a distributed rendering workflow. The script sets up the rendering parameters in Blender, calculates the frame ranges for each job, and manages the rendering process across all jobs in the array.

> **Note**: This script is designed for CPU-based rendering, ensuring compatibility with a wide range of AWS instance types. If you wish to utilize GPU-based rendering, please create a custom function to enable GPU support. Refer to the example provided in the [example_gpu_render](/examples/single_scripts/example_gpu_render/render_gpu.py) file for guidance.


Key functionalities include:
- **Scene Configuration**: Sets up the scene’s resolution and output format in Blender.
- **Frame Chunk Calculation**: Computes the frame ranges for each job based on the total animation length and job array size.
- **Rendering and Logging**: Executes the rendering of frames in chunks and logs progress for monitoring job completion.

## Entrypoint:
The entry point is the `main.py` file in the project root directory.


## Project Structure (tree):
```
job_array_animation
├── main.py
├── README.md
└── utils
    ├── __init__.py
    └── setup_render_animation.py
```


## Use Case:
- [x] Example
- [ ] Utility 

## Job Type:
- [x] Array
- [ ] Single job

## Envs:

### Default ENVS
These are the default environment variables that Brender Studio provides for your jobs:
| **Key**                            | **Value**                 | **Actions** |
| ---------------------------------- | ------------------------- | ----------- |
| **JOB_ACTION_TYPE**                | custom_render_python      | Default     |
| **EFS_MAIN_SCRIPT_PATH**           | /mnt/efs/projects/        | Default     |
| **EFS_BLENDER_FILE_PATH**          | /mnt/efs/projects/        | Default     |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Default     |
| **BLENDER_EXECUTABLE**             | /usr/bin/blender          | Default     |
| **USE_EEVEE**                      | False                     | Default     |
| **USE_GPU**                        | False                     | Default     |
| **BUCKET_NAME**                    | brender-bucket-s3-<UUID>  | Default     |
| **BUCKET_KEY**                     | <PROJECT_NAME>            | Default     |


- **`AWS_BATCH_JOB_ARRAY_SIZE`**:  Indicates the total number of jobs in the array. This helps in dividing the animation into chunks for each job. This variable is set automatically by AWS Batch and defines the size of the job array.

- **`AWS_BATCH_JOB_ARRAY_INDEX`**: Represents the index of the current job within the array. Each job uses this index to process its designated chunk of frames. This variable is also set automatically by AWS Batch and is used to identify which portion of the animation each job should render.


### Custom Environment Variables
If you need to use additional or custom environment variables for your specific use case, you can add them in the `envs` section of the Job Settings in Brender Studio. Click on `Add Custom env` and provide the variable name and value.

### Custom ENV
| **Key**                            | **Value**                 | **Actions** |
| ---------------------------------- | ------------------------- | ----------- |
| **<KEY_CUSTOM_ENV>**               | **<CUSTOM_VALUE>**        | Custom      |


> Note: Ensure that any custom environment variables you add are properly referenced and handled in your script. For instance, you can retrieve custom variables in your Python script using `os.environ.get('CUSTOM_VARIABLE_NAME')`.


## AWS Batch Environment Variables, Detailed Explanation:

- **`AWS_BATCH_JOB_ARRAY_SIZE`**: AWS Batch automatically provides this variable when running a Job Array. It represents the total number of jobs in the array and is essential for dividing the rendering workload among the jobs. You should use this value to calculate how to split your animation into appropriate segments for each job.

- **`AWS_BATCH_JOB_ARRAY_INDEX`**: This variable indicates the index of the current job within the array, starting from 0. Each job in the array will use this index to determine which portion of the animation it should render. For example, if your animation has 1000 frames and you have 10 jobs in the array, the first job (index 0) might process frames 0-99, the second job (index 1) frames 100-199, and so on.

These variables are crucial for the proper execution of distributed jobs and must be handled correctly in the script to ensure each job processes its assigned portion of the workload.


## Note:
This script is intended to be executed as part of an AWS Batch Job Array. Ensure that the necessary environment variables are properly set up before execution, otherwise the job will fail.


## References:
- [AWS Batch Job Array Documentation](https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html)
- [Brender Studio Documentation](https://brenderstudio.com/docs)