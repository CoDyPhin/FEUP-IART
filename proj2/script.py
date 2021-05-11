import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import sklearn.tree as tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


data_2018 = pd.read_csv("archive/Example_DATASET.csv", na_values=['NA'])
data_2019 = pd.read_csv("archive/Example_2019_price_var.csv", na_values=['NA'])

data_2018.columns.values[0] = "Name"
data_2019.columns.values[0] = "Name"



#full data with the actual  price variation
full_data = pd.merge(data_2018, data_2019, on='Name', how='inner')
full_data['Name'].unique()
# full_data.columns.values[109] = "price_var_2019"


    
### REMOVING OUTLIERS ###
full_data.loc[full_data['Revenue Growth'] > 25,'Revenue Growth'] = full_data['Revenue Growth'].mean()

# full_data.loc[full_data['Weighted Average Shares Growth'] > 100,'Weighted Average Shares Growth'] = full_data['Weighted Average Shares Growth'].mean()

full_data.loc[full_data['Weighted Average Shares Diluted Growth'] > 100,'Weighted Average Shares Diluted Growth'] = full_data['Weighted Average Shares Diluted Growth'].mean()

# full_data.loc[full_data['EBIT Growth'] > 2000,'EBIT Growth'] = full_data['EBIT Growth'].mean()

# full_data.loc[(full_data['Gross Profit Growth'] < -60) | (full_data['Gross Profit Growth'] > 20) ,'Gross Profit Growth'] = full_data['Gross Profit Growth'].mean()

# full_data.loc[full_data['Capex per Share'] < -2,'Capex per Share'] = full_data['Capex per Share'].mean()

# full_data.loc[full_data['Free Cash Flow growth'] > 140,'Free Cash Flow growth'] = full_data['Free Cash Flow growth'].mean()

full_data.loc[full_data['Days Payables Outstanding'] > 60000,'Days Payables Outstanding'] = full_data['Days Payables Outstanding'].mean()

# full_data.loc[(full_data['ROE'] < -20),'ROE'] = full_data['ROE'].mean()

# Plot attributes relatively to 2019 price variation
# for col1 in full_data.columns[2:]:
#     print(col1)
#     plt.suptitle(col1)
#     plt.scatter(full_data[col1], full_data[full_data.columns[-1]])
#     plt.show()
    
    
all_inputs = full_data.drop(columns=["class", "Name", "2019 PRICE VAR [%]"])
all_labels = full_data['class'].values


(training_inputs,
 testing_inputs,
 training_classes,
 testing_classes) = train_test_split(all_inputs, all_labels, test_size=0.25)


# Create the classifier
decision_tree_classifier = DecisionTreeClassifier()


#Find the best paramters

parameters = {'criterion': ['gini', 'entropy'],
              'max_depth': [ 2, 3, 4, 5, 10, 20, 30, 40, 50],
              }


cross_validation = StratifiedKFold(n_splits=10)

grid_search = GridSearchCV(decision_tree_classifier,
                           param_grid=parameters,
                           cv=cross_validation)


grid_search.fit(all_inputs, all_labels)
print('Best score: {}'.format(grid_search.best_score_)) #Score means accuracy
print('Best parameters: {}'.format(grid_search.best_params_))

with open('decision_tree.dot', 'w+') as out_file:
    out_file = tree.export_graphviz(grid_search.best_estimator_, out_file=out_file)


decision_tree_classifier = grid_search.best_estimator_
cv_scores = cross_val_score(decision_tree_classifier, all_inputs, all_labels, cv=cross_validation, scoring="accuracy")
print(cv_scores)
plt.hist(cv_scores)
plt.title('Average score: {}'.format(np.mean(cv_scores)))


# Validate the classifier on the testing set using classification accuracy
# print(decision_tree_classifier.score(testing_inputs, testing_classes))


