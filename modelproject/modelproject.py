from types import SimpleNamespace
import numpy as np
from matplotlib import pyplot as plt

class InvestorForecast:

    def __init__(self):

        par = self.par = SimpleNamespace()

        par.pi_L = 0.4
        par.pi_H = 0.6
        par.lam_1 = 0.4
        par.lam_2 = 0.4
        par.q_ini = 0.5
    
    def forecast(self, old_y, new_y, q):
        """
        Forecast function
        
        Input:
        old_y: Shock in previous period
        new_y: Shock in current period

        Output: Investor's belief in q-value for the coming period
        """
        if old_y == new_y:
            new_q = (self.par.pi_L * ((1-self.par.lam_1) * q + self.par.lam_2 * (1-q))) / (self.par.pi_L * ((1-self.par.lam_1) * q + self.par.lam_2 * (1-q)) + self.par.pi_H * (self.par.lam_1*q + (1-self.par.lam_2) * (1-q)))
        else:
            new_q = ((1-self.par.pi_L) * ((1-self.par.lam_1) * q + self.par.lam_2 * (1-q))) / ((1-self.par.pi_L) * ((1-self.par.lam_1) * q + self.par.lam_2 * (1-q)) + (1-self.par.pi_H) * (self.par.lam_1 * q + (1-self.par.lam_2) * (1 - q)))
        return new_q
    
    def convergence(self, old_y, new_y, conDetails = True):
        """
        Convergence of q-value
        
        Input:
        old_y: Shock in previous period
        new_y: Shock in current period
        conDetails: Unless changed to False, will print detailed convergence and plots of the convergence

        Output: Convergence of investor's belief in q-value
        """
    # printDetails allows to not print the deatiled convergence and plots when comparing reparameterization
        max_iterations = 100
        tolerance = 1e-6
        q_values = [self.par.q_ini]
        if conDetails:
            print("Iteration\tq\t\tnew_q")
        for i in range(max_iterations):
            old_q = q_values[-1]
            new_q = self.forecast(old_y, new_y, old_q)
            q_values.append(new_q)
            if conDetails:
                print(f"{i+1}\t\t{old_q:.6f}\t{new_q:.6f}")
            if abs(new_q - old_q) < tolerance:
                break
        
        if conDetails:
            plt.plot(range(len(q_values)), q_values, marker='o', linestyle='-')
            plt.xlabel('Iteration')
            plt.ylabel('q Value')
            plt.title('Convergence of q')
            plt.grid(True)
            plt.show()

        return q_values
    
    def simulate(self, n, simDetails = True):
        """
        Simulation of q-value given n random shocks
        
        Input:
        n: number of shocks
        simDeatils: Unless changed to False, will print detailed simulation and plots of the q-value

        Output: Simulated q-value for the coming period, depending on previous- and current periods q-value.
        """
    # simDetails allows to not print the deatiled simulation and plots when comparing reparameterization
        old_y = 1
        q_values = []
        q = self.par.q_ini
        for i in range(n):
            new_y = np.random.choice([-1, 1])
            q_values.append(self.forecast(old_y,new_y,q))
            if simDetails:
                print(f"Period {i+1:2}: old_y = {old_y:2}, new_y = {new_y:2}, q = {q_values[i]:.2f}")
            old_y = new_y
            q = q_values[i]

        if simDetails:
            plt.plot(range(1, n+1), q_values, marker='o', linestyle='--')
            plt.xlabel('Iteration')
            plt.ylabel('q Value')
            plt.title('q Value for Each Iteration')
            plt.grid(True)
            plt.show()

        return q_values