class RenderConfig:
    def __init__(self, output_path, array_size, job_index, render_type):
        self.output_path = output_path
        self.array_size = array_size
        self.job_index = job_index
        self.render_type = render_type
        self.resolution_x = 1920
        self.resolution_y = 1080
        self.file_format = 'PNG'