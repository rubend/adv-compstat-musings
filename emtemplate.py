import sys

class emtemplate:
    def testConvergence(self):
        'test the convergence on the model object'
        'True if converged, false otherwise'
        pass
    
    def initialize(self):
        'initialize the parameters'
        pass
            
    def expectationStep(self):
        'expectation step of the EM algorithm.'
        'Here the expectation of the log-likelihood evalutated'
        'using the current estimate for the prameters is done.'
        pass

    def maximizationStep(self):
        'maximization step of the EM algorithm'
        'it computes the parameters maximizing the expected'
        'log-likelihood found on the E step'
        pass


