class docstring:
    """
    This is a documentation example for python
    """
    
    def __init__(self) -> None:
        """
        This is the class constructor
        """
        self._doc = ''
        
    def method (self, param1, param2) -> None:
        """
        This is a method of the class
        Args:
            param1 (_type_): This is the first parameter
            param2 (_type_): This is the second parameter
        """
        self._param1 = param1
        self._param2 = param2
        
if __name__ == '__main__':
    #help(docstring)
    print(docstring.__doc__)
    print(docstring.__init__.__doc__)
    print(docstring.method.__doc__)
    
    # Functions are objects in python
    print(type(docstring.method))