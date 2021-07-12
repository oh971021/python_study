

import warnings

MUTABLE = ['radius']
IMMUTABLE = ['diameter', 'circumference', 'area']

class Circle:
    pi = 3.1415
    
    def __init__(self, r):
        self.radius = r
        
    def diameter(self):
        return self.radius * 2
    
    def __setattr__(self, name, value):
        if name in ['diameter']:
            warnings.warn("불가")
        return super().__setattr__(name, value)
