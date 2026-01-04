class Calculator:
    """
    A calculator class demonstrating the use of class methods and static methods.
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers together.
        
        This is a static method that doesn't need access to class or instance data.
        It's a utility function that logically belongs to the Calculator class.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers together.
        
        This is a class method that has access to class attributes via the cls parameter.
        It can access and modify class-level data.
        
        Args:
            cls: Reference to the class itself
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b