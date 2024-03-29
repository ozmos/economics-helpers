class MacroEconomics:
    """
    Calculate the inflation factor for a given period of time.
    """
    @staticmethod
    def inflation_factor(price_1, price_2):
        return price_2 / price_1
    

    """
    Calculate Aggregate Demand
    """
    @staticmethod
    def aggregate_demand(consumption,investment,government_spending,exports,imports):
        return consumption + investment + government_spending + (exports - imports)
    
    """
    Calculate GDP using expenditure formula
    """
    @staticmethod
    def expenditure_formula(consumption,investment,government_spending,exports,imports):
        return MacroEconomics.aggregate_demand(consumption,investment,government_spending,exports,imports)
    
  
    """
    Calculate consumption multiplier based on marginal propensity to consume
    (MPC)
    """
    @staticmethod
    def consumption_multiplier(mpc):
        return 1 / (1 - mpc)
    
    """
    Calculate effect on economy of government spending based on marginal 
    propensity to consume (MPC)
    """
    @staticmethod
    def mpc_spending_effect(spending,mpc):
        return spending * MacroEconomics.consumption_multiplier(mpc)