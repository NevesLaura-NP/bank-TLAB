
import statistics as stats

from StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()
    
    #this function checks if a value can be transformed into a float or not and will be used to skip date values on the rows
    def valid_float(self, val):
        
        try:
            float_val = float(val)
            return True
        except ValueError:
            return False
  
  
    def average01(self):
        
        averages = []

        for row in self.data:
            new_vals = [float(i) for i in row if self.valid_float(i) and self != ""]
            row_avg = round(stats.mean(new_vals), 3)
            averages.append(row_avg)

        return averages

#this code represents a less elegant look into a possible code with for loops 
    def median02(self):
        """pt2
        """
        median = []

        for row in self.data:
            row_i = []
            for i in row[1:]:
                try:
                    i = float(i)
                    row_i.append(i)
                except ValueError: 
                    continue       
            row_med = stats.median(row_i)
            median.append(row_med)

        return median

    def stddev03(self):
        """pt3
        """
        stdev = []
        
        for row in self.data:
            new_vals = [float(i) for i in row if self.valid_float(i) and self != ""]
            row_stdev = round(stats.stdev(new_vals), 3)
            stdev.append(row_stdev)
                
        return stdev
                


