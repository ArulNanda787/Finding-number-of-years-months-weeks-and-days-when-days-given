#!/usr/bin/env python
# coding: utf-8

# In[ ]:


days = int(input("Please enter number of days:"))
years = days // 365
rem = days%365
months = rem // 30
rem2 = rem % 30
weeks = rem2 // 7
days = rem2 % 7
print(years, "years")
print(months, "months")
print(weeks, "weeks")
print(days, "days")

