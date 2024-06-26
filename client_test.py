import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  
  def setUp(self):
    self.quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    self.quotes1 = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

  def test_getDataPoint_calculatePrice(self):
    """ ------------ Add the assertion below ------------ """
    expected_result = ("ABC", 120.48, 121.2, (120.48 + 121.2) / 2)
    self.assertIsInstance(getDataPoint(self.quotes[0]), tuple)
    self.assertEqual(getDataPoint(self.quotes[0]), expected_result)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    
    """ ------------ Add the assertion below ------------ """
    bid_price = self.quotes1[0]["top_bid"]["price"]
    ask_price = self.quotes1[0]["top_ask"]["price"]
    price = (bid_price + ask_price) / 2
    stock = self.quotes1[0]["stock"]

    bid_price1 = self.quotes1[1]["top_bid"]["price"]
    ask_price1 = self.quotes1[1]["top_ask"]["price"]
    price1 = (bid_price1 + ask_price1) / 2
    stock1 = self.quotes1[1]["stock"]

    self.assertEqual(getDataPoint(self.quotes1[0]), (stock, bid_price, ask_price, price))
    self.assertEqual(getDataPoint(self.quotes1[1]), (stock1, bid_price1, ask_price1, price1))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_positiveNonZero(self):
    """Tests for ratios for standard cases with non-zero inputs"""
    bid_price1 = self.quotes[0]["top_bid"]["price"]
    ask_price1 = self.quotes[0]["top_ask"]["price"]
    expected_ratio = bid_price1 / ask_price1
    self.assertEqual(getRatio(bid_price1, ask_price1), expected_ratio)

  def test_getRatio_zeroDenominator(self):
    """Test for ratio with zero denominator"""
    price_a = 10
    price_b = 0
    expected_result = None
    
    self.assertIsNone(getRatio(price_a, price_b), expected_result)



if __name__ == '__main__':
    unittest.main()
