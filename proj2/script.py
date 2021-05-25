def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import sklearn.tree as tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


data_2018 = pd.read_csv("archive/Example_DATASET.csv", na_values=['NA'])
data_2019 = pd.read_csv("archive/Example_2019_price_var.csv", na_values=['NA'])

data_2018.columns.values[0] = "Name"
data_2019.columns.values[0] = "Name"



#full data with the actual  price variation
full_data = pd.merge(data_2018, data_2019, on='Name', how='inner')
full_data['Name'].unique()
# full_data.columns.values[109] = "price_var_2019"


# Create correlation matrix
corr_matrix = full_data.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

# Find features with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

print("to_drop", len(to_drop))

# Drop features 
full_data.drop(to_drop, axis=1, inplace=True)

    
### REMOVING OUTLIERS ###
# full_data.loc[full_data['Revenue Growth'] > 25,'Revenue Growth'] = full_data['Revenue Growth'].mean()

# full_data.loc[full_data['Gross Margin'] < -7,'Gross Margin'] = full_data['Gross Margin'].mean()

# full_data.loc[full_data['Cash and cash equivalents'] > 1.2e11,'Cash and cash equivalents'] = full_data['Cash and cash equivalents'].mean()

# full_data.loc[full_data['Free Cash Flow growth'] > 140,'Free Cash Flow growth'] = full_data['Free Cash Flow growth'].mean()

# full_data.loc[full_data['Weighted Average Shares Growth'] > 100,'Weighted Average Shares Growth'] = full_data['Weighted Average Shares Growth'].mean()

# full_data.loc[full_data['daysOfPayablesOutstanding'] > 60000,'daysOfPayablesOutstanding'] = full_data['daysOfPayablesOutstanding'].mean()

# full_data.loc[full_data['EBIT Growth'] > 2000,'EBIT Growth'] = full_data['EBIT Growth'].mean()

# full_data.loc[full_data['Capex to Depreciation'] > 40,'Capex to Depreciation'] = full_data['Capex to Depreciation'].mean()

# full_data.loc[full_data['Weighted Average Shares Diluted Growth'] > 100,'Weighted Average Shares Diluted Growth'] = full_data['Weighted Average Shares Diluted Growth'].mean()


# full_data.loc[(full_data['Gross Profit Growth'] < -60) | (full_data['Gross Profit Growth'] > 20) ,'Gross Profit Growth'] = full_data['Gross Profit Growth'].mean()

# full_data.loc[full_data['Capex per Share'] < -2,'Capex per Share'] = full_data['Capex per Share'].mean()



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
  testing_classes) = train_test_split(all_inputs, all_labels, test_size=0.2, stratify=full_data.drop(columns=["Name", "2019 PRICE VAR [%]"], inplace=True), random_state=1)


# Apply scaler to normalize data
scaler = StandardScaler()

scaler.fit(training_inputs)

inputs_train = scaler.transform(training_inputs)
inputs_test = scaler.transform(testing_inputs)


cross_validation = StratifiedKFold(n_splits=10)

###     DECISION TREES

# weights =  {0: len(full_data) / (2*len(full_data.loc[full_data['class'] == 0,'class'])), 1: len(full_data) / (2*len(full_data.loc[full_data['class'] == 1,'class']))}

# decision_tree_classifier = DecisionTreeClassifier()

# # print("weights: ", weights)


# DTParameters = {'criterion': ['gini', 'entropy'],
#                   'splitter': ['best', 'random'],
#                   'max_depth': [2, 3, 4, 5],
#                   'max_features': ['auto', 'sqrt', 'log2'],
#                   }



# dtgs = GridSearchCV(decision_tree_classifier,
#                             param_grid=DTParameters,
#                             cv=cross_validation,
#                             scoring = "precision_weighted")


# dtgs.fit(inputs_train, training_classes)

# predictions_train = dtgs.predict(inputs_train)
# predictions_test = dtgs.predict(inputs_test)

# print('Best score, and parameters, found on development set:')
# print()
# print('%0.3f for %r' % (dtgs.best_score_, dtgs.best_params_))
# print()



# print("Training set Confusion Matrix ")
# print(confusion_matrix(training_classes, predictions_train))

# print("Testing set Confusion Matrix ")
# print(confusion_matrix(testing_classes, predictions_test))

# print(accuracy_score(training_classes, predictions_train))
# print(accuracy_score(testing_classes, predictions_test))
# print(classification_report(training_classes, predictions_train, target_names=['IGNORE', 'BUY']))
# print(classification_report(testing_classes, predictions_test, target_names=['IGNORE', 'BUY']))

# print(classification_report(testing_classes, dtgs.predict(testing_inputs), target_names=['IGNORE', 'BUY']))





###     NEURAL NETWORKS

# neural_network_classifier = MLPClassifier(random_state=1, early_stopping=False, verbose=True)

# MLPParameters = {
#     "learning_rate": ["adaptive", "constant"],
#     "alpha": [0.0001, 0.05],
#     "power_t": [0.25, 0.5, 0.75],
#     'activation': ['tanh', 'relu', "logistic"],
#     'hidden_layer_sizes': [(32,), (64,), (32, 64, 32)],
#     'solver': ['adam', 'sgd']
#   }

# cross_validation = StratifiedKFold(n_splits=10)

# mlpgs = GridSearchCV(neural_network_classifier, MLPParameters, n_jobs=-1, scoring = "precision_weighted", cv = cross_validation)

# mlpgs.fit(inputs_train, training_classes)

# print('Best score, and parameters, found on development set:')
# print()
# print('%0.3f for %r' % (mlpgs.best_score_, mlpgs.best_params_))
# print()

# print("Predictions train")
# print()


# predictions_train = mlpgs.predict(inputs_train)
# predictions_test = mlpgs.predict(inputs_test)


# print("Training set Confusion Matrix ")
# print(confusion_matrix(training_classes, predictions_train))

# print("Testing set Confusion Matrix ")
# print(confusion_matrix(testing_classes, predictions_test))

# print(accuracy_score(training_classes, predictions_train))
# print(accuracy_score(testing_classes, predictions_test))
# print(classification_report(training_classes, predictions_train, target_names=['IGNORE', 'BUY']))
# print(classification_report(testing_classes, predictions_test, target_names=['IGNORE', 'BUY']))


###     SVM

# SVMParameters = {
#     "kernel": ["rbf", "linear", "poly", "sigmoid"],
#     'gamma': ['scale', 'auto'],
#     'shrinking': [True, False],
#     'C': [0.01, 0.1, 1, 10, 100],
#     "class_weight": [None, 'balanced']
#     }


# svmgs = GridSearchCV(SVC(), SVMParameters, n_jobs = -1, scoring="precision_weighted", cv=cross_validation)



# svmgs.fit(inputs_train, training_classes)

# print('Best score and parameters found on development set:')
# print()
# print('%0.3f for %r' % (svmgs.best_score_, svmgs.best_params_))
# print()

# predictions_train = svmgs.predict(inputs_train)
# predictions_test = svmgs.predict(inputs_test)


# print("Training set Confusion Matrix ")
# print(confusion_matrix(training_classes, predictions_train))

# print("Testing set Confusion Matrix ")
# print(confusion_matrix(testing_classes, predictions_test))


# print(accuracy_score(training_classes, predictions_train))
# print(accuracy_score(testing_classes, predictions_test))
# print(classification_report(training_classes, predictions_train, target_names=['IGNORE', 'BUY']))
# print(classification_report(testing_classes, predictions_test, target_names=['IGNORE', 'BUY']))


### KNN

KNNParameters = {'n_neighbors': list(range(1,10)),
                  'weights': ['uniform', 'distance'],
                  'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
                  'p':[1,2]
                  }


knngs = GridSearchCV(KNeighborsClassifier(), KNNParameters, n_jobs=-1, scoring="precision_weighted", cv=cross_validation, return_train_score=False)

knngs.fit(inputs_train, training_classes)


print('Best score and parameters found on development set:')
print()
print('%0.3f for %r' % (knngs.best_score_, knngs.best_params_))
print()

scores = cross_val_score(knngs.best_estimator_, inputs_train, training_classes, cv=10, scoring="precision_weighted")
print("Scores: ", scores)

predictions_train = knngs.predict(inputs_train)
predictions_test = knngs.predict(inputs_test)

print("Training set Confusion Matrix ")
print(confusion_matrix(training_classes, predictions_train))

print("Testing set Confusion Matrix ")
print(confusion_matrix(testing_classes, predictions_test))


print(accuracy_score(training_classes, predictions_train))
print(accuracy_score(testing_classes, predictions_test))
print(classification_report(training_classes, predictions_train, target_names=['IGNORE', 'BUY']))
print(classification_report(testing_classes, predictions_test, target_names=['IGNORE', 'BUY']))


score_df = pd.DataFrame()
best_scores = {}
best_scores['Decision Trees'] = dtgs.best_score_
best_scores['Neural Networks'] = mlpgs.best_score_
best_scores['Support Vector Machine'] = svmgs.best_score_
best_scores['K Nearest Neighbours'] = knngs.best_score_
for name, score in best_scores.items():
    score_df = score_df.append(pd.DataFrame({'Score': [score], 'Classifier': [name]}))

ax = sb.barplot(x='Classifier', y='Score', data=score_df)
ax.set_title('Classifiers Best Accuracy Score')
ax.set_xticklabels(ax.get_xticklabels(), rotation=20, horizontalalignment='right')


classifiers = {}
classifiers['Decision Trees'] = dtgs.best_estimator_
classifiers['Neural Networks'] = mlpgs.best_estimator_
classifiers['Support Vector Machine'] = svmgs.best_estimator_
classifiers['K Nearest Neighbours'] = knngs.best_estimator_
clf_df = pd.DataFrame()
for name, clf in classifiers.items():
    clf_df = clf_df.append(pd.DataFrame({'precision_weighted': cross_val_score(clf, inputs_train, training_classes, cv=StratifiedKFold(n_splits=10)),
                       'classifier': [name] * 10}))

ax = sb.boxplot(x='classifier', y='precision_weighted', data=clf_df)
ax.set_title('Classifiers Accuracy')
ax.set_xticklabels(ax.get_xticklabels(), rotation=20, horizontalalignment='right')

fittime_df = pd.DataFrame()
fit_times = {}
fit_times['Decision Trees'] = np.mean(dtgs.cv_results_['mean_fit_time'])
fit_times['Neural Networks'] = np.mean(mlpgs.cv_results_['mean_fit_time'])
fit_times['Support Vector Machine'] = np.mean(svmgs.cv_results_['mean_fit_time'])
fit_times['K Nearest Neighbours'] = np.mean(knngs.cv_results_['mean_fit_time'])
for name, fittime in fit_times.items():
    fittime_df = fittime_df.append(pd.DataFrame({'Avg Fit Time': [fittime], 'Classifier': [name]}))
    
ax = sb.barplot(x='Classifier', y='Avg Fit Time', data=fittime_df)
ax.set_title('Classifiers Average Fit Time')
ax.set_xticklabels(ax.get_xticklabels(), rotation=20, horizontalalignment='right')

grid_visualization = mlpgs.cv_results_['mean_test_score']
grid_visualization.shape = (4, 12)
sb.heatmap(grid_visualization, cmap='Blues', annot=True)
plt.xticks(np.arange(3) + 0.5, mlpgs.param_grid['max_features'])
plt.yticks(np.arange(4) + 0.5, mlpgs.param_grid['max_depth'])
plt.xlabel('max_features')
plt.ylabel('max_depth')