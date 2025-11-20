

from sklearn.preprocessing import FunctionTransformer

class CustomTransformers:
    def __init__(self):
        self.lowercasing = FunctionTransformer(self.lowercasing)
    
    def lowercasing(self,text):
        return text.lower()
    
    
