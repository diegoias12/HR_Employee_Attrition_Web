import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

[
    'Age', # 29.25, 39.5, 49.75, 60
    'EnvironmentSatisfaction', 
    'JobInvolvement', 
    'JobLevel', 
    'MonthlyIncome',  # 4795.80, 8582.60, 12369.40, 16156.20, 19943.00  
    'StockOptionLevel', 
    'TotalWorkingYears', # 9.25, 17.50, 25.75, 34.00
    'YearsAtCompany', # 7.00, 13.00, 19.00, 25.00
    'YearsInCurrentRole', # 3.75, 7.50, 11.25, 15.00
    'YearsWithCurrManager', # 3.50, 7.00, 10.50, 14.00
    'PercentCurrentRoleAtCompany', # 20.00, 40.00, 60.00, 80.00, 100.00

    'BusinessTravel_Travel_Frequently',
    'BusinessTravel_Travel_Rarely', 

    'JobRole_Laboratory Technician',
    'JobRole_Manufacturing Director', 
    'JobRole_Other',
    'JobRole_Research Scientist', 
    'JobRole_Sales Executive',
    'JobRole_Sales Representative', 

    'MaritalStatus_Married',
    'MaritalStatus_Single', 

    'OverTime_Yes'
]

def make_prediction(form_dict):
    loaded_model = pickle.load(open('static/models/model_attrition.sav', 'rb'))

    data_for_model = []

    # 'Age', # 29.25, 39.5, 49.75, 60
    value = float(form_dict.get('Age'))
    new_value = np.array([29.25, 39.5, 49.75, 60.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    data_for_model.append(int(form_dict.get('EnvironmentSatisfaction')))
    data_for_model.append(int(form_dict.get('JobInvolvement')))
    data_for_model.append(int(form_dict.get('JobLevel')))

    # 'MonthlyIncome',  # 4795.80, 8582.60, 12369.40, 16156.20, 19943.00  
    value = float(form_dict.get('MonthlyIncome'))
    new_value = np.array([4795.80, 8582.60, 12369.40, 16156.20, 19943.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    data_for_model.append(int(form_dict.get('StockOptionLevel')))

    # 'TotalWorkingYears', # 9.25, 17.50, 25.75, 34.00
    value = float(form_dict.get('TotalWorkingYears'))
    new_value = np.array([9.25, 17.50, 25.75, 34.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    # 'YearsAtCompany', # 7.00, 13.00, 19.00, 25.00
    value = float(form_dict.get('YearsAtCompany'))
    new_value = np.array([7.00, 13.00, 19.00, 25.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    # 'YearsInCurrentRole', # 3.75, 7.50, 11.25, 15.00
    value = float(form_dict.get('YearsInCurrentRole'))
    new_value = np.array([3.75, 7.50, 11.25, 15.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    # 'YearsWithCurrManager', # 3.50, 7.00, 10.50, 14.00
    value = float(form_dict.get('YearsWithCurrManager'))
    new_value = np.array([3.50, 7.00, 10.50, 14.00, 1000000.00])
    data_for_model.append(np.where(new_value > value)[0][0])

    # 'PercentCurrentRoleAtCompany', # 20.00, 40.00, 60.00, 80.00, 100.00
    value = float(form_dict.get('YearsInCurrentRole')) / float(form_dict.get('YearsAtCompany')) * 100
    new_value = np.array([20.00, 40.00, 60.00, 80.00, 100.00, 1000000.00])
    data_for_model.append(np.where(new_value >= value)[0][0])

    # 'BusinessTravel_Travel_Frequently',
    # 'BusinessTravel_Travel_Rarely', 
    value = int(form_dict.get('BusinessTravel'))
    bit_index = [-1, 1, 0]
    one_hot = [0] * 2
    if bit_index[value] >= 0:
        one_hot[bit_index[value]] = 1
    data_for_model += one_hot

    # 'JobRole_Laboratory Technician',
    # 'JobRole_Manufacturing Director', 
    # 'JobRole_Other',
    # 'JobRole_Research Scientist', 
    # 'JobRole_Sales Executive',
    # 'JobRole_Sales Representative', 
    value = int(form_dict.get('BusinessTravel'))
    bit_index = [4, 3, 0, 1, 2, 2, 5, 2, 2]
    one_hot = [0] * 6
    if bit_index[value] >= 0:
        one_hot[bit_index[value]] = 1
    data_for_model += one_hot

    # 'MaritalStatus_Married',
    # 'MaritalStatus_Single', 
    value = int(form_dict.get('MaritalStatus'))
    bit_index = [1, 0, -1]
    one_hot = [0] * 2
    if bit_index[value] >= 0:
        one_hot[bit_index[value]] = 1
    data_for_model += one_hot

    # 'OverTime_Yes'
    data_for_model.append(int('OverTime' in form_dict))

    data_for_model = [float(x) for x in data_for_model]
    # example = [1., 2., 3., 1., 0., 1., 0., 0., 0., 0., 4., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.]

    # [0.89307303, 0.10692697]
    proba = loaded_model.predict_proba([data_for_model])[:, 1][0]
    str_2dec = str(round(proba, 4) * 100)[:5]
    return str_2dec
