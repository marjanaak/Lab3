import price_info

def test_total_cost_shopping():
    test_quantitylist = {'apple': 5, 'orange':10}
    price_info.quantity_list = test_quantitylist
    assert (price_info.total_cost_shopping() == 20)

def test_cost_of_fruits():
    assert (price_info.cost_of_fruits('apple', 10) == 12.0)