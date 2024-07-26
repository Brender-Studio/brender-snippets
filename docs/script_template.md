# Script Template

Please fill out the following basic template for any scripts being added to the brender-snippets repository.

You can copy this template and paste it into the new script's `README.md` file or reference it in the example script's `README.md` file.

## Name (H1):

Enter the name of the script

## Author:

Enter the author's name

## Blender Version:

Specify the Blender version compatible with the script

## Screenshots(optional):

Include relevant screenshots

## Script Description:

Briefly describe what the script does

## Detailed Description (optional):

Provide a detailed description of the script's functionality

## Key Features and Parameters (optional):

List the key features and parameters of the script

## Entrypoint:

Define the entry point of the script

## Use Case:

Indicate the use case of the script

- [ ] Utility
- [ ] Example

## Job Type:

Indicate the type of job the script performs

- [ ] Array
- [ ] Single job

## Envs:

### Default ENVS

| Key                            | Description                                                                                                                                                                    | Env Type       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| JOB_ACTION_TYPE                | Defines the job action type. Brender Studio Docker image uses this variable to determine the action type of the job.                                                           | Brender-Studio |
| EFS_MAIN_SCRIPT_PATH           | Path to the main script in EFS.                                                                                                                                                | Brender-Studio |
| EFS_BLENDER_FILE_PATH          | Path to the .blend file in EFS.                                                                                                                                                | Brender-Studio |
| EFS_BLENDER_OUTPUT_FOLDER_PATH | Path to the output folder in EFS. Useful for saving the rendered images using Brender Studio logic. All contents of this folder are uploaded to S3 after the job is completed. | Brender-Studio |
| BLENDER_EXECUTABLE             | Path to the Blender executable.                                                                                                                                                | Brender-Studio |
| USE_EEVEE                      | Determines if the Eevee render engine is used. Docker image activates a virtual display for Eevee rendering (xvfb).                                                            | Brender-Studio |
| USE_GPU                        | Determines if GPU is used for rendering. No logic is implemented in the Docker image to use the GPU. Users can use this variable to implement their own logic.                 | Brender-Studio |
| BUCKET_NAME                    | Name of the S3 bucket.                                                                                                                                                         | Brender-Studio |
| BUCKET_KEY                     | Project key in S3. It is the project name provided by the user in the form.                                                                                                    | Brender-Studio |
| AWS_BATCH_JOB_ARRAY_INDEX      | Index of the job in the AWS Batch job array. Useful for identifying the job in the array.                                                                                      | AWS Batch      |
| AWS_BATCH_JOB_ARRAY_SIZE       | Size of the job array in AWS Batch. Useful for identifying the size of the job array.                                                                                          | AWS Batch      |
| AWS_BATCH_JOB_ID               | ID of the AWS Batch job.                                                                                                                                                       | AWS Batch      |
| AWS_BATCH_JOB_ATTEMPT          | Attempt number of the AWS Batch job.                                                                                                                                           | AWS Batch      |
| AWS_BATCH_CE_NAME              | Compute environment name of the AWS Batch job.                                                                                                                                 | AWS Batch      |
| AWS_BATCH_JQ_NAME              | Job queue name of the AWS Batch job.                                                                                                                                           | AWS Batch      |

### Custom ENV

| **Key**              | **Value**          | **Env Type** |
| -------------------- | ------------------ | ------------ |
| **<KEY_CUSTOM_ENV>** | **<CUSTOM_VALUE>** | Custom       |


> NOTE: NOTE: Only mention Envs used in your script.

## Usage (optional):

Provide instructions on how to use the script

## Note(optional):

Any additional notes about the script

## References:

Provide references like videos or related repositories
