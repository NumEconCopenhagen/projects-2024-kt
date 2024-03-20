from types import SimpleNamespace

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1-par.w1A
        par.w2B = 1-par.w2A

    def utility_A(self,x1A,x2A):
        return x1A**self.par.alpha * x2A**self.par.alpha

    def utility_B(self,x1B,x2B):
        return x1B**self.par.beta * x2B**self.par.beta

    def demand_A(self,p1):
        I_A = self.par.w1A*p1 + self.par.w2A
        demand_bundle_A = (self.par.alpha*I_A/p1, (1-self.par.alpha)*I_A)
        return demand_bundle_A
        
    def demand_B(self,p1):
        I_B = self.par.w1B*p1 + self.par.w2B
        demand_bundle_B = (self.par.beta*I_B/p1, (1-self.par.beta)*I_B)
        return demand_bundle_B

    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2