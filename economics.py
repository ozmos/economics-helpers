class Economics:
    """
    Calculates midpoint formula used for own-price elasticity
    """
    @staticmethod
    def midpoint(q1,q2,p1,p2):
        quantity = (q2-q1) / ((q2+q1) / 2)
        price = (p2-p1) / ((p2+p1) / 2)
        return quantity / price


    """
    Calculates cross price elasticity

    Parameters
    ----------
    quantity : float
        Percentage Change in quantity of product X
    price: float
        Percentage change in price of product y
    """
    @staticmethod
    def cross_price_elasticity(quantity, price):
        coefficient = quantity / price
        type = "complement" if coefficient < 0 else "substitute"
        return { "coefficient": coefficient, "type": type }
    

    @staticmethod
    def income_elasticity(quantity, income):
        coefficient = quantity / income
        if coefficient < 0:
            type = "inferior"
        elif coefficient <= 1:
            type = "normal"
        else:
            type = "luxury"
        return { "coefficient": coefficient, "type": type }

    @staticmethod
    def slope(y1,y2,x1,x2):
        return ((y2 - y1) / (x2 - x1))

    @staticmethod
    def marginal_utility(u1,u2,q1,q2):
        return ((u2 - u1) / (q2 - q1))

    @staticmethod
    def marginal_utility_per_the_price(u1,u2,q1,q2,price):
        return Economics.marginal_utility(u1,u2,q1,q2) / price

    """
    As above but used when marginal utility is already provided
    """
    @staticmethod
    def mu_p(mu1,mu2,price):
        return (mu2 - mu1) / price

    """
    Average Product of Labour
    """
    @staticmethod
    def apl(total_output,number_of_workers):
        return total_output / number_of_workers

    """
    Marginal Product of Labour
    """
    @staticmethod
    def mpl(total_product_1,total_product_2,number_of_workers_1,number_of_workers_2):
        return (total_product_2 - total_product_1) / (number_of_workers_2 - number_of_workers_1)

    """
    Marginal Product of Labour for a table of labourers/product
    """
    @staticmethod
    def mpl_list(labour_total_products):
        prev_mpl = 0
        curr_mpl = 0
        decrease_announced = False
        for i, item in enumerate(labour_total_products):
            prev = 0 if i == 0 else labour_total_products[i - 1][1]
            curr_mpl = Economics.mpl(prev,item[1],1,2)
            decrease = prev_mpl > curr_mpl
            prev_mpl = curr_mpl
            print(f"MPL at {item[0]} workers: {Economics.mpl(prev,item[1],1,2)}")
            if decrease and not decrease_announced:
                print(f"MPL decreased after {labour_total_products[i-1][0]} labourers")
                decrease_announced = True

    """
    Average Fixed Cost (AFC)
    """
    @staticmethod
    def afc(fixed_costs, total_output):
        return fixed_costs / total_output

    """
    Average Variable Cost (AVC)
    """
    @staticmethod
    def avc(variable_costs, total_output):
        return variable_costs / total_output

    """
    Average Total Cost
    ATC = (AFC + AVC) or TC/Total output
    """
    @staticmethod
    def atc(fixed_costs, variable_costs, total_output):
        afc = Economics.afc(fixed_costs, total_output)
        avc = Economics.avc(variable_costs, total_output)
        return afc + avc

    """
    Get a cost given an ATC, another cost and total output
    """
    @staticmethod
    def reverse_cost(cost,atc,total_output):
        total_cost = atc * total_output
        return total_cost - cost

    """
    Marginal cost (MC)
    MC = change in total cost / change in output
    """
    @staticmethod
    def mc(total_cost_1,total_cost_2,total_output_1,total_output_2):
        return (total_cost_2 - total_cost_1) / (total_output_2 - total_output_1)

    """
    Average Revenue (AR)
    Per unit revenue
    """
    @staticmethod
    def ar(total_revenue,total_output):
        return total_revenue / total_output

    """
    Total Sales Revenue (TR)
    The price of an item multiplied by number of units sold
    """
    @staticmethod
    def tr(price, quantity):
        return price * quantity

    """
    Average Revenue and Total Sales Revenue
    """
    @staticmethod
    def ar_and_tr(price, quantity, total_output = None):
        if total_output is None:
            total_output = quantity
            
        tr = Economics.tr(price, quantity)
        ar = Economics.ar(tr, total_output)
        return { "Total revenue": tr, "Average Revenue": ar }

    

    

    
