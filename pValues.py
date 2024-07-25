from flippingACoin import normal_probability_above, normal_probability_below, normal_approximation_to_binomial

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    How likely are we to see a value at least as extreme as x 
    (in either direction) if our values are from an N(mu, sigma)?
    """
    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)
    
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(two_sided_p_value(529.5, mu_0, sigma_0))      # 0.062