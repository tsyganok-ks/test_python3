import unittest
from test_python import DrawPlots

#Test cases to test DrawPlots methods
class TestDrawPlots(unittest.TestCase):
    def setUp(self):
        self.plots = DrawPlots()
    def test_draw_plots_wrong_path(self):
        self.assertEqual(self.plots.draw_plots('not_df.txt'), [])
    def test_draw_plots_right_path(self):
        self.assertEqual(self.plots.draw_plots('data/deviation.json')[0], 'plots//Difference in number of corners (real and predicted).png')
        #self.


if __name__ == '__main__':
    unittest.main()



