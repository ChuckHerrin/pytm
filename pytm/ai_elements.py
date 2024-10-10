from pytm.pytm import Element

class AIModel(Element):
    """
    Represents an AI or Machine Learning model.
    """
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.isExposed = kwargs.get('isExposed', False)
        self.isTrainedWithSensitiveData = kwargs.get('isTrainedWithSensitiveData', False)
        self.hasRobustTraining = kwargs.get('hasRobustTraining', False)
        self.hasInputValidation = kwargs.get('hasInputValidation', False)
        self.hasOutputFiltering = kwargs.get('hasOutputFiltering', False)
        self.authenticatesSource = kwargs.get('authenticatesSource', False)

class Dataset(Element):
    """
    Represents a dataset used for training AI models.
    """
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.isPublic = kwargs.get('isPublic', False)
        self.containsSensitiveData = kwargs.get('containsSensitiveData', False)
        self.isValidated = kwargs.get('isValidated', True)
