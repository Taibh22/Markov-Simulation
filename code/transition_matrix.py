#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import cv2
import seaborn as sns
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta


# In[10]:


#pip install opencv-python


# In[3]:


transition_matrix = pd.read_csv("C:/spiced_projects/student-code/thyme-machine-student-code/week8/data/transition_matrix.csv")


# In[4]:


transition_matrix


# In[5]:


transition_matrix.set_index("location", inplace=True)


# In[6]:


transition_matrix


# In[21]:


sns.heatmap(data=transition_matrix, annot=True, cmap='Blues');


# In[53]:


from markovchain import MarkovChain

mc = MarkovChain(np.array(transition_matrix), ['checkout', 'dairy','drinks','fruit','spices'])
mc.draw("C:/spiced_projects/student-code/thyme-machine-student-code/week8/code/markov-chain-five-states1.png")


# In[40]:





# In[ ]:




