class RenderConfig:
    def __init__(self, output_path, render_type):
        self.output_path = output_path
        # self.array_size = array_size
        # self.job_index = job_index
        self.render_type = render_type
        self.resolution_x = 1920
        self.resolution_y = 1080
        self.file_format = 'PNG'
        # self.cycles_device = 'CPU' # 'CPU' or 'GPU'
        self.samples = 10