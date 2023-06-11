#!/usr/bin/env python
# coding: utf-8




import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta




transition_matrix = pd.read_csv("C:/spiced_projects/student-code/thyme-machine-student-code/week8/data/transition_matrix.csv")
df_allweekday_f = pd.read_csv("C:/spiced_projects/student-code/thyme-machine-student-code/week8/data/df_allweekday_f.csv")



transition_matrix.set_index("location", inplace=True)





from faker import Faker





class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation. """
    
    def __init__(self, id_cu,name,transition_matrix,location):
        self.id_cu=id_cu
        self.name = name
        self.location=location
        self.transition_matrix=transition_matrix
        self.path=['entrance', self.location]


    def __repr__(self):
        return f'Customer {self.name} (id {self.id_cu}) is in {self.location}'
    
    def next_state(self):
        ''' Propagates the customer to the next state. Returns nothing.   '''
        current_prob = self.transition_matrix.loc[self.location]
        self.location = np.random.choice(['checkout','dairy','drinks','fruit','spices'],p=current_prob)
        #np.random.choice(self.transition_matrix.columns.values, p=self.transition_matrix.loc[self.location])
    @property
    def is_active(self):
        """Returns True if the customer has not reached the checkout yet.
        """
        if self.location != 'checkout':
            return True
        else:
            return False



limit_min = 30
new_customer_min = 1.0


class Supermarket1:
    """manages multiple Customer instances that are currently in the market.    """
    
    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.list = pd.DataFrame(columns=['timestamp', 'customer_id', 'name','location'])
        
    def __repr__(self):
    
        return f"{self.get_time}"
    @property

    def get_time(self):
        hour = 7 + self.minutes // 60
        min = self.minutes % 60
        return f"{hour:02}:{min:02}:00"
        
    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            timestamp = self.get_time
            customer_name = customer.name
            customer_id = customer.id_cu
            location = customer.location
            self.list=self.list.append({'timestamp' : timestamp, 'name' : customer_name, 'customer_id' : customer_id, 'location' : location}, ignore_index=True)

    def next_minute(self): #control our customers
        """propagates all customers to the next state."""
        self.minutes += 1
        for shopper in self.customers:
            shopper.next_state()
            self.print_row(shopper)
  #poisson      
    def add_new_customers(self): #create a customer
        """randomly creates new customers."""
        n = np.random.poisson(new_customer_min)
        
        for i in range(n):
            name = Faker().name()
            id_cu = self.last_id
            section = np.random.choice(['checkout','dairy','drinks','fruit','spices'])
            shopper=Customer(id_cu,name,transition_matrix,section)
            self.customers.append(shopper) #this function in my supermarket object literally creates other objects
            self.last_id += 1
            self.print_row(shopper)
    
    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        self.customers = [i for i in self.customers if i.is_active]
        
    def print_row(self, customer):
        row = str(self) + ", " + str(customer)
        print(row)
   
if __name__ == "__main__":
    s = Supermarket1()
    for i in range(limit_min):
        s.next_minute()
        s.add_new_customers()
        s.print_customers()
        s.remove_exitsting_customers()
    s.list.to_csv('C:/spiced_projects/student-code/thyme-machine-student-code/week8/data/simulator_customer.csv')







