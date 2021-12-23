""" Building Fast Queries Final Script"""
import csv
class Inventory(): 
    def __init__(self, csv_filename):
        with open(csv_filename) as f: 
            reader = csv.reader(f)
            rows = list(reader)
        
        self.header = rows[0]        
        self.rows = rows[1:]
        self.id_to_row = {}  
        self.prices = set() 

        for row in self.rows:              
            row[-1] = int(row[-1])
                                   
        for row in self.rows:                       
            self.id_to_row[row[0]] = row                                
        
        for row in self.rows:                        
            self.prices.add(row[-1])

        def row_price(rows):
            return rows[-1]
            
        self.rows_by_price = sorted(self.rows, key=row_price) 
    
    def get_laptop_from_id(self, laptop_id):  
        if laptop_id in self.id_to_row:           
            return self.id_to_row[laptop_id]
        return None                     
    
    def check_promotion_dollars(self, dollars):
        if dollars in self.prices:                   
            return True
        for price in self.prices:                    
            if dollars - price in self.prices:
                return True
        return False                                
    
    def find_laptop_with_price(self, target_price):
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                       
        
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            value = self.rows_by_price[range_middle][-1]
            
            if value == target_price:                            
                return range_middle                        
            elif value < target_price:                           
                range_start = range_middle + 1             
            else:                                          
                range_end = range_middle - 1 
        
        if self.rows_by_price[range_start][-1] != target_price:                  
            return -1                                      
        
        return range_start
    
    def find_first_laptop_more_expensive(self, target_price):
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                   

        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            price = self.rows_by_price[range_middle][-1]
            
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        
        if self.rows_by_price[range_start][-1] <= target_price:                  
            return -1                                   
        return range_start