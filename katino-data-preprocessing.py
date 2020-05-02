#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
import re
from itertools import compress
from tqdm import tqdm
import sys


# In[2]:


def delete_bracket_back(str_):
    try:
        m = re.match(r'(.*)(\(.*\)$)', str_)
        return(m.group(1))
    except:
        return(str_)


# In[3]:


def delete_bracket_front(str_):
    try:
        m = re.match(r'^(\[.*\])(.*)', str_)
        return(m.group(2))
    except:
        return(str_)


# In[4]:


def delete_bracket_front2(str_):
    try:
        m = re.match(r'^(\(.*\))(.*)', str_)
        return(m.group(2))
    except:
        return(str_)


# In[5]:


def delete_bracket_front_bold(str_):
    try:
        m = re.match(r'^(\【.*\】)(.*)', str_)
        return(m.group(2))
    except:
        return(str_)


# In[6]:


if __name__ == '__main__':
    #MIN_LENGTH = 10
    #FIALNAME = "katino_data.csv"
    FIALNAME = sys.argv[1]
    MIN_LENGTH = int(sys.argv[2])

    print("read %s in..." % FIALNAME)
    df = pd.read_csv(FIALNAME)

    print("move 時事 政治...")# 去除時事 政治 (index 在 legal_index_kuru.csv )
    df = df[df["board"] != 3590]
    df = df[df["board"] != 190]
    title = df.title.to_numpy()

    print("start to move bracket...")
    title = [delete_bracket_back(i) for i in tqdm(title)]
    title = [delete_bracket_front(i) for i in tqdm(title)]
    title = [delete_bracket_front2(i) for i in tqdm(title)]
    title_B = [delete_bracket_front_bold(i) for i in tqdm(title)]

    print("replace word \u3000")#　replace word \u3000
    title_C = [str(i).replace("\u3000", " ") for i in tqdm(title_B)]

    print("delete title that len(title) < %d" % MIN_LENGTH)
    title_length = [len(str(i)) for i in title_C]
    bool_want = np.array(title_length) > MIN_LENGTH
    title_D = list(compress(title_C, bool_want))

    # save
    name = "%s_adjust.npy" % FIALNAME[:-4]

    try:
        np.save(name, title_D)
        print("preprocessing successfully")
        print("save as %s" % name)
    except:
        print("preprocessing failed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




