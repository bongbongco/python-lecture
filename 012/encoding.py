
# coding: utf-8

# In[27]:

import os
path = "/Users/seungyonglee/dev/git/adidas/"


# In[29]:

for filename in os.listdir(path):
    print filename[-3:]
    if filename[-3:] == "txt":     # txt 파일이면
        print path+filename
        open(path+filename)
        os.rename(path+filename, "[Edit]"+path+filename)


# In[ ]:




# In[ ]:



