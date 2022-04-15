# Although this doesn't need to extend any class it has to implement two methods from class object:
# __enter__
# __exit__

class FilesManager:
    def __init__(self,name) -> None:
        self.name = name
        
    def __enter__(self):
        print('We access the file'.center(50,'-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name
    
    def __exit__(self,exception_type,exception_value,exception_trace):
        print('We close the file'.center(50,'-'))
        if self.name:
            self.name.close()