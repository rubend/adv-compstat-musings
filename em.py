import sys

class EM:

    def __init__ (self,model):
        self.model = model
        
    def run(self):
        'runs the EM algorithm on the model'
        
        #check if the model has been initialized? So we can print out an error?
        
        self.initialize()
        self.maximizationStep()

        while self.testConvergence():
            self.expectationStep()
            self.maximizationStep()
        print "run is finished"
            
    def testConvergence(self):
        'test the convergence on the model object'
        'True if converged, false otherwise'
        try:
            return self.model.testConvergence()
        except AttributeError:
            print 'model doesn\'t seem to have a testConvergence function'
            sys.exit()

    def initialize(self):
        'initialize the parameters'
        try:
            self.model.initialize()
        except AttributeError:
            print 'model doesn\'t seem to have an initialize function'
            sys.exit()
            
    def expectationStep(self):
        'expectation step of the EM algorithm.'
        'Here the expectation of the log-likelihood evalutated'
        'using the current estimate for the prameters is done.'
        try:
            self.model.expectationStep()
        except AttributeError:
            print 'model doesn\'t seem to have an expectationStep function'
            sys.exit()

    def maximizationStep(self):
        'maximization step of the EM algorithm'
        'it computes the parameters maximizing the expected'
        'log-likelihood found on the E step'
        try:
            self.model.maximizationStep()
        except AttributeError:
            print 'model doesn\'t seem to have a maximizationStep function'
            sys.exit()



