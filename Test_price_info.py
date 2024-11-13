import price_info as prices

def test_total_cost_shopping():
        result = None
        expected = 46.75
        price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

        quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
        result = prices.total_cost_shopping()

        assert (result == expected)


def test_cost_of_fruit():
        result = None
        expected = 12.0
        fruitname = "apple"
        quantity = 10
        
        result = prices.cost_of_fruits(fruitname, quantity)

        assert (result == expected)
        