
# coding: utf-8

# Part 1 - Explaining your plan to solve the final (your algorithm) - 20 pts
# 
# Part 2 - Reading from a JSON file for instructions - 20 pts
# 
# Part 3 - Reading from an XML file for supplemental data - 20 pts
# 
# Part 4 - Creating a function to calculate total cost - 20 pts
# 
# Part 5 - Reading from a SQL database and merging it with other data - 30 pts
# 
# Part 6 - Summarize along brand/generic and mail/retail indicators - 30 pts
# 
# Background
# JSON files are often used not just to store data, but also to store configuration information for how a program should run. This way, your program doesn't have to be changed when minor configuration changes are all that need to change. Examples might include database configuration information, source database table names, date ranges for data processing, etc. The final includes a JSON file that provides important configuration information that will be used to direct the rest of your program on how to combine and process the data from an XML file and a SQL database. First, however, you'll need to read all the instructions and describe your approach / algorithm for solving the final exam.
# 
# JSON Configuration --------------------------------------\
#                                                           >---> Total Cost per Claim --> Summary
# SQL Database: Prescription Claims ---------------\       /
#                                                   >-----/
# XML File: Mapping of Member Group to Admin Fee --/

# Part 1 - Algorithm (20 pts)
# Before you start writing any code, spend some time to think through what you're planning to do. Explain your approach to the problem, possibly breaking down separate algorithms for each of the 4 segments below, if that seems natural to you.
# 
# Only write 8-10 sentences. Anything longer will be too much detail.

# Part 2 - JSON for configuration (20 pts)
# You've been provided a JSON file that contains the following pieces of information:
# 
# Database Connection Information:
# Database User Name
# Database Password
# Database Host
# Database Name
# Start Date - The start date for data to process, in the format YYYY-MM-DD
# End Date - The end date for data to process, in the format YYYY-MM-DD
# Cost Field Mapping - This is a dictionary that contains entries that describe which fields should be summed to compute an output field, total cost
# Fill in the function definition below to read in the configuration information from the specified JSON file. You'll know it works using the test code that provided in the function description.
# 
# You can cat /data/config.json to see the contents of the entire file. Below is a sample file.
# 
# In [2]:
# %%bash
# cat /data/config_sample.json
# {
# 	"Database User": "slucor",
# 	"Database Password": "S1UC0R",
# 	"Database Host": "localhost",
# 	"Database Name": "hds5210",
# 
# 	"Start Date": "2016-11-01",
# 	"End Date": "2016-11-30",
# 
# 	"Cost Field Mapping": {
# 		"MG001": ["ingredient_cost", "admin_fee", "rebate_amount"],
# 		"MG002": ["ingredient_cost"],
# 		"AZ001": ["incredient_cost", "admin_fee"]
# 	}
# }

#  Put your code to read configuration information from whatever file is specified by "filename"
# # Your function has to return an dictionary that has the same key/value pairs as in the file.
# import json
# def setup(filename):
#     """(str) -> dict
#     The function reads from the specified configuration file, in JSON format, and stores the contents
#     in a Python dictionary.  That dictionary is returned to the caller, as shown in #4.
#     
#     >>> setup('/data/config_sample.json').get("Database User")
#     'slucor'
#     
#     >>> setup('/data/config_sample.json').get("Cost Field Mapping")["MG001"][0]
#     'ingredient_cost'
#     
#     >>> setup('/data/config_sample.json').get("Cost Field Mapping").get("AZ001")[1]
#     'admin_fee'
#     """
#     
#     #...
#     # Put your code here
#     #...

# In[3]:


importimport  doctestdoctest
doctest.testmod()


# Part 3 - Read data from XML (20 pts)
# The XML file in /data/fees.xml provides information about extra fees that are applied to prescription claims based on the member's group and whether or not the claim is for a mail order (90 day) or retail (30 day) prescription. The "admin_fee" is in this file and will be an important component in determining the final cost of the claims. You can see the contents of the XML file with the cat command below.
# 
# Write a function that will read in the fee configuration information from the XML file specified, and return a Python dictionary that contains that information in the following format. Your format should match the structure below exactly, and you should not hard-code any field values like member group or mail/retail code. That is, your code should automatically work with any new groups or mail/retail codes that may be created in the future.
# 
# { 
#   'MG001': {
#     'MAIL': {'admin_fee': 0.5, 'processing_fee': 0.05},
#     'RETAIL': {'admin_fee': 0.5, 'processing_fee': 0.1}
#   }
# }
# You can cat the entire XML file if you like, below is a sample.
# 
# In [1]:
# %%bash
# cat /data/fees_sample.xml
# <?xml version="1.0" encoding="UTF-8"?>
# 
# <fee_config>
#   <fees member_group="MG001" mail_retail="MAIL">
#     <admin_fee>0.50</admin_fee>
#     <processing_fee>0.05</processing_fee>
#   </fees>
#   <fees member_group="MG001" mail_retail="RETAIL">
#     <admin_fee>0.50</admin_fee>
#     <processing_fee>0.10</processing_fee>
#   </fees>
# </fee_config>

# # Put your code into the function definition below.  You can test it using doc test.
# import xml.etree.ElementTree as xml
# def read_fees(filename):
#     """(str)->dict
#     
#     >>> read_fees('/data/fees_sample.xml').get("MG001").get("RETAIL").get("admin_fee")
#     0.5
#     
#     >>> read_fees('/data/fees_sample.xml').get("MG001").get("MAIL").get("processing_fee")
#     0.05
#     """
# 
#     #...
#     # Put your code here
#     #...

# Part 4 - Computing Total Cost based on Configuration Logic (20 pts)
# The logic for computing the total cost varies based on the member group, as specified in the configuration file, and requires a combination of data that will come from a database table (ingredient cost) and data from the fees.xml file.
# 
# Write a function called calc_total_cost that will take the following parameters and return the resulting total cost.
# 
# config - The Python dictionary loaded from your setup() function and the /data/config.json file
# fees - The Python dictionary loaded from your read_fees() function and the /data/fees.xml file
# member_group - The member group to use in computing total cost
# mail_retail - Either MAIL or RETAIL to specify
# ingredient_cost - The base ingredient cost amount.
# Your function will need to calculate a total cost based on the components defined for that member group in the config dictionary, and the fees specified for that member group in the fees dictionary.
# 
# For example, if we provide inputs of:
# 
# mail_retail="MAIL" and ingredient_cost=2.45
# 
# and if the configuration file says the following within in:
# 
# "00HH02": ["ingredient_cost", "processing_fee"]
# and fees file says the following within it:
# 
#   <fees member_group="00HH02" mail_retail="MAIL">
#     <admin_fee>0.93</admin_fee>
#     <processing_fee>1.84</processing_fee>
#   </fees>
#   <fees member_group="00HH02" mail_retail="RETAIL">
#     <admin_fee>0.22</admin_fee>
#     <processing_fee>1.01</processing_fee>
#   </fees>
# Then the total cost function should return:
# 
# ingredient_cost + processing_fee for MAIL 
# 2.45 + 1.84
# 4.29
# Note that the formula will not always be the same. Some member groups use just ingredient_cost to calculate the total cost, others use ingredient_cost, admin_fee, and still others use ingredient_cost, admin_fee, processing_fee.
# 
# Round the answer to 2 decimal places

# def calc_total_cost(config, fees, member_group, mail_retail, ingredient_cost):
#     """(dict, dict, str, str, float) -> float
#     This function uses a combination of information from the configuration dictionary,
#     fees dictionary, member group name, mail retail identifier, and ingredient cost
#     to compute a total cost.
#     
#     >>> c = setup('/data/config.json')
#     >>> f = read_fees('/data/fees.xml')
#     >>> calc_total_cost(c, f, "00400F", "MAIL", 2.11)
#     2.11
#     
#     >>> calc_total_cost(c, f, "00460H", "RETAIL", 1.09)
#     1.46
#     """
# 
#     #...
#     # Put your code here...
#     #...

# Part 5 - Putting it together with data from a SQL database (30 pts)
# In this final step, you will read the raw data from a database into a dictionary and compute the total cost of each claim using the configuration you got from the JSON file and additional fees from the XML file. Simply store the computed TOTAL COST as another attribute of the dictionary you retrieved from the database.
# 
# You don't need to write a separate function to do this, but you will need to include calls to your functions defined above earlier.
# 
# The claims database table contains the following fields that you can use in your computations. You won't need all of them.
# 
# rx_number
# member_group
# drug_ndc
# rx_count
# process_date
# new_refill_indicator
# brand_generic_ind
# mail_order_ind
# lob_code
# lob_desc
# pa_indicator
# benefit_plan_code
# business_unit_id
# paid_amount
# ingredient_cost
# sales_tax
# copay_amount
# You should expect to see results that look like the example below, but a list of 1000 items.
# 
# [{'TOTAL COST': Decimal('88.98'),
#   'benefit_plan_code': 'PZU',
#   'brand_generic_ind': 'GENERIC',
#   'business_unit_id': 'HNCA',
#   'copay_amount': Decimal('5.00000'),
#   'drug_ndc': '60505036302',
#   'ingredient_cost': Decimal('88.98000'),
#   'lob_code': '',
#   'lob_desc': '',
#   'mail_order_ind': 'RETAIL',
#   'member_group': '00400F',
#   'new_refill_indicator': 'NEW',
#   'pa_indicator': 'N',
#   'paid_amount': Decimal('88.23000'),
#   'process_date': '2015-01-05',
#   'rx_count': '',
#   'rx_number': '1460346',
#   'sales_tax': Decimal('0.00000')},
#   ...

# import pymysql.cursors
# 
# c = setup('/data/config.json')
# f = read_fees('/data/fees.xml')
# 
# connection = pymysql.connect(
#     host=c.get("Database Host"),
#     user=c.get("Database User"),
#     password=c.get("Database Password"),
#     db=c.get("Database Name"),
#     cursorclass=pymysql.cursors.DictCursor)
# 
# # ...
# # Put your code to query the database and produce the results here
# # ...
Part 6 - Summarize along retail/mail and generic/brand dimensions (30 pts)
Your output in result is a list of dictionaries that all have the same attributes. Now, we need to summarize this information to understand how the paid_amount differs based on the values in the mail_order_ind and brand_generic_ind fields. We intuitively know that the possible values for these are MAIL/RETAIL and BRAND/GENERIC, but that may not always be the case. In your code, do not assume these are the only possible values. Instead, build the summary results dynamically based on the actual values in the data.

Take the result output from above and create the following matrix (list of lists), where the value at the intersection of the labels is the average of the paid_amount for those criteria, rounded to 2 decimal places.

[[None,    'GENERIC', 'BRAND'], 
 ['MAIL',   33.0,      325.79], 
 ['RETAIL', 13.05,     297.65]]