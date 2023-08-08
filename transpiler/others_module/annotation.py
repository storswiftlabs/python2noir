class Annotation:
    def __init__(self, line: int, content: str):
        self.line = line
        self.content = content

    def get_content(self):
        return f'// {self.content}\n'
