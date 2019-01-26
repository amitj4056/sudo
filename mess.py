
# coding: utf-8

# In[1]:


import zulip


# In[3]:


# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="./zuliprc")


# In[10]:


# Send a stream message
request = {
    "type": "stream",
    "to": "sunilkv20164012@gmail.com",
    "subject": "Castle",
    "content": "I come not, friends, to steal away your hearts."
}


# In[11]:


result = client.send_message(request)
print(result)


# In[8]:


# Send a private message
request = {
    "type": "private",
    "to": "sunilkv20164012@gmail.com",
    "content": "With mirth and laughter let old wrinkles come."
}


# In[9]:


result = client.send_message(request)
print(result)


# In[13]:


# Upload a file
fp = open('speech2Text.py', 'rb')
result = client.call_endpoint(
    'user_uploads',
    method='POST',
    files=[fp]
)


# In[14]:


print(result)

