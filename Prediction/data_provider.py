import os
import joblib

config = {
    'heart': {
        'NaiveBayes': 'production/NaiveBayes_model.sav',
        'DecisionTree':'production/decision_tree_model.sav',
        'scalar_file': 'production/standard_scalar.pkl',
    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    else:
        print("file does not exit")



def GetNaiveBayesClassifierForHeart():
    return GetJobLibFile(config['heart']['NaiveBayes'])

def GetDecisionTreeClassifierForHeart():
    return GetJobLibFile(config['heart']['DecisionTree'])


def GetStandardScalarForHeart():
    return GetJobLibFile(config['heart']['scalar_file'])

def GetAllClassifiersForHeart():
    return (GetNaiveBayesClassifierForHeart(),GetDecisionTreeClassifierForHeart())

