# Model analysis project

My project is titled **A model of investor incentive** and is about a rational investor's behavior on the stock market, given a wrong idea of the true model of earnings.
In this project, earnings can be positive or negative in each period with equal probability.
The investor believes that shocks are correlated across periods, and that they are dictated by either a mean reversion model (negative correlation) or a momentum model (positive correlation).
Investor has predefined beliefs on how likely consecutive identical- and alternating shocks are, given the market is governed by each model.
Also, investor's beliefs in how likely a regime change from model 1 to model 2 or from model 2 to model 1 is, are also predefined.

This project aims to analyze how likely investor perceives the mean reversion model to be, given:
1) Consecutive identical- and alternating shocks in an initial model.
2) Random shocks in an initial model.
3) Same analysis as 1) and 2) but given reparameterization.

The **results** of the project can be seen from running [modelproject.ipynb](modelproject.ipynb).

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires no further packages.