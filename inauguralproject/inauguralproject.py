from types import SimpleNamespace
import numpy as np
from scipy import optimize

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
        return x1A**self.par.alpha * x2A**(1-self.par.alpha)

    def utility_B(self,x1B,x2B):
        return x1B**self.par.beta * x2B**(1-self.par.beta)

    def demand_A(self,p1):
    # Returns a tuple of demand for good 1 and 2 for consumer A
        I_A = self.par.w1A*p1 + self.par.w2A
        demand_bundle_A = (self.par.alpha*I_A/p1, (1-self.par.alpha)*I_A)
        return demand_bundle_A
        
    def demand_B(self,p1):
        I_B = self.par.w1B*p1 + self.par.w2B
        demand_bundle_B = (self.par.beta*I_B/p1, (1-self.par.beta)*I_B)
        return demand_bundle_B
    
    def exchange_lens(self, N):
        exchange_lens = []
        for i in range(N+1):
            x1A = i/N
            for j in range(N+1):
                x2A = j/N
                if self.utility_A(x1A, x2A) >= self.utility_A(self.par.w1A, self.par.w2A) and self.utility_B(1-x1A, 1-x2A) >= self.utility_B(self.par.w1B, self.par.w2B):
                    exchange_lens.append([x1A, x2A])
        return exchange_lens

    def check_market_clearing(self,p1):
    # a eps1 and eps2 = 0 when markets clear

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
    
    def find_equilibrium_iter(self, p1_guess, details = True):
    # Equilibrium price for good 1 is found using iteration
        t = 0
        p1 = p1_guess
        eps = 1e-6
        kappa = 0.1
        maxiter = 500

        while True:
            # Excess demand
            x1A,x2A = self.demand_A(p1)
            x1B,x2B = self.demand_B(p1)
            
            E1 = x1A + x1B - 1
            E2 = x2A + x2B - 1

            if np.abs(E1) < eps or t >= maxiter:
                if details:
                    print(f'{t:3d}: p1 = {p1:12.8f} -> excess demand for good 1-> {E1:14.8f}')
                    print(f'{t:3d}: p2 = {1:12.8f} -> excess demand for good 2-> {E2:14.8f}')
                return x1A, x2A

            p1 += kappa * E1/2

            t += 1



    
      

    
            



