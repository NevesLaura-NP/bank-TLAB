
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()
    

    def valid_float(self, val):
        
        try:
            float_val = float(val)
            return True
        except ValueError:
            return False
        
        
    def average01(self):
        
        averages = []

        for row in self.data:
            new_vals = [float(price) for price in row if self.valid_float(price)]
            if new_vals:
                row_avg = round(stats.mean(new_vals), 3)
                averages.append(row_avg)

        return averages


    def median02(self):
        """pt2
        """
        median = []

        for row in self.data:
            new_vals = [float(price) for price in row if self.valid_float(price)]
            if new_vals:
                row_med = stats.median(new_vals)
                median.append(row_med)

        return median

    def stddev03(self):
        """pt3
        """
        stdev = []
        
        for row in self.data:
            new_vals = [float(price) for price in row if self.valid_float(price)]
            if new_vals:
                row_stdev = round(stats.stdev(new_vals), 3)
                stdev.append(row_stdev)
                
        return stdev
                


