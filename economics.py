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
                
    
