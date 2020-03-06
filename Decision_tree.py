from __future__ import absolute_import, division, print_function, unicode_literals

try:
  # %tensorflow_version only exists in Colab.
  %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import figure

from google.colab import drive
drive.mount('/content/drive',force_remount=True)

import os
os.chdir('/content/drive/My Drive/daisy')
product_dictionary = './files/product_dictionary.csv'
units_dictionary = './files/units_dictionary.csv'

products = pd.read_csv(product_dictionary)
product_list = list(products['product_name'].values)
products = pd.get_dummies(products,prefix=['product_name'])
units = pd.read_csv(units_dictionary)
unit_list = list(units['units'].values)
units= pd.get_dummies(units,prefix=['units'])# units,products 


# Random Forest



# for i in a 
# l = a[i]

# Test Examples
l1 = ['2/$5',
     'SAVE $6.98 on 2',
     'Blueberries',
     'cat ion',
     '1 pint',
     "10% off",
     "RECEIVE AN EXTRA 5% OFF",
    #  "BRAND WIDE SALE",
    #  "SAVE $4/lb.",
    #  "Gouda with Mediterranean Herbs",
    #  "$3.99",
    #  "SAVE $1.50",
    #  "$7.99/lb",
    #  "SAVE $1/lb",
    #  "Ice Cream",
    #  "Cereals",
    #  "SAVE 50¢",
    #  "SAVE 98¢ on 2",
    #  "NY Strips",
    #  "2/$6",
    #  "$9.49",
    #  "BUY ONE, GET ONE FREE",
    #  "Kombucha",
    #  "$2.99",
    #  "$3.99/lb",
    #  "3 lb. Bag Organic Gala Apples",
    #  "7oz."
     ]


    


d = dict()


namelist = []
namecandidatelist = []
for i in range(len(l)):
    a = l[i]
    if "SAVE" in a:
        for ii in range(i+1,len(l)):
            i = l[ii]
            if "SAVE" not in i and "OFF" not in i and "$" not in i and "¢" not in i and "BUY ONE, GET ONE FREE" in i:
                i = l[ii] 
                b = i.split()
                namelist.append(b)
bestcandidate = product_list[0]
for j in range(len(product_list)):
    count = 0
    currentcount = 0
    leachproductname = product_list[j].split()
    for k in leachproductname:
        if k in namelist:
            count += 1

    if count > currentcount:
        bestcandidate = product_list[j]
        currentcount = count

d["name"] = bestcandidate
# to find product_name
# product_name – Name from the product dictionary that matches closest with the product name in the ad-block

            
for i in range(len(l)):
    a = l[i]
    b = a.split()
    for j in b:
        if j in unit_list:
            d["unit"] = a
# to find unit
# uom – Unit of measurement of the product (e.g. lb, 1 Pint, 10 Pack, etc.)




for i in range(len(l)):
    a = l[i]
    


    if "SAVE" in a and "on" in a:
        d["least_unit_for_promo"] = a
# to find least_unit_for_promo
# least_unit_for_promo – Least amount of the product the customer has to buy in order to use the promo (e.g. Save $3.5 on 2, output value – 2). Default value is 1.

    if "$" in a or "¢" in a:
        if "/" in a:
            d["price"] = a
# to find unit_promo_price
# unit_promo_price – Promotion price for each unit (e.g. ad-block - 2/$5, output value $2.5)

    if "SAVE" in a:
        if "$" in a or "¢":
            d["save"] = a
# to find the money saved per unit
# amount of money saved per unit rounded off at 2 decimal places (e.g. - Save $3.5 on 2, output value – $1.75)

    if "OFF" in a and "RECEIVE AN EXTRA" not in a:
        if "HALF" in a:
            d["discount"] = 0.5
        elif "%" in a:
            d["discount"] = a
        elif "$" in a:
            d["save"] = a

    if "RECEIVE AN EXTRA" in a:
        d["extra_discount"] = a
# to find/count if there is an extra disconut


    if "BUY ONE, GET ONE FREE" in a:
        d["discount"] = 0.5
 # to find the percent discount
 # discount – Discount on the original price rounded off to 2 decimal places (e.g. 2/$5, Save $6.98 on 2, output value = $6.98/$11.98 = 0.58)
