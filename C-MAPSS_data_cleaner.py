
import pandas as pd

columns=["id","cycle","op1","op2","op3","sensor1","sensor2","sensor3",      "sensor4","sensor5","sensor6","sensor7","sensor8",
         "sensor9","sensor10","sensor11","sensor12","sensor13","sensor14","sensor15","sensor16","sensor17","sensor18","sensor19"
         ,"sensor20","sensor21","sensor22","sensor23"]

cycle=125 #Assumed cycle after which the engine starts degrading

def train_data_cleaner(train):
    train['remaining_cycle'] = train.groupby(['id'])['cycle'].transform(max)-train['cycle']
    train_x=train.drop(["id","cycle","op1","op2","op3","sensor1","sensor5","sensor6",
    "sensor10","sensor16","sensor18","sensor19","sensor22","sensor23"],axis=1)
    return train_x


def train_data_cleaner_R_ectified(train):
    train['remaining_cycle'] = train.groupby(['id'])['cycle'].transform(max)-train['cycle']
    df_train['R_early'] = train['remaining_cycle'].apply(lambda x: cycle if x >= cycle else x)
    train_x=df_train.drop(["id","cycle","op1","op2","op3","sensor1","sensor5","sensor6",
    "sensor10","sensor16","sensor18","sensor19","sensor22","sensor23"],axis=1)
    return train_x


def test_data_cleaner(test_results,test):
    test_results.columns=["rul","null"]
    test_results.drop(["null"],axis=1,inplace=True)
    test_results['id']=test_results.index+1
    rul = pd.DataFrame(test.groupby('id')['cycle'].max()).reset_index()
    rul.columns = ['id', 'max']
    test_results['rul_failed']=test_results['rul']+rul['max']
    test_results.drop(["rul"],axis=1,inplace=True)
    test=test.merge(test_results,on=['id'],how='left')
    test["remaining_cycle"]=test["rul_failed"]-test["cycle"]
    test.drop(["rul_failed"],axis=1,inplace=True)
    test_x = test.drop(["id","cycle","op1","op2","op3","sensor1","sensor5","sensor6",
    "sensor10","sensor16","sensor18","sensor19","sensor22","sensor23","remaining_cycle"],axis=1)
    return test_x


def test_data_cleaner_R_ectified(test_results,test):
    test_results.columns=["rul","null"]
    test_results.drop(["null"],axis=1,inplace=True)
    test_results['id']=test_results.index+1
    rul = pd.DataFrame(test.groupby('id')['cycle'].max()).reset_index()
    rul.columns = ['id', 'max']
    test_results['rul_failed']=test_results['rul']+rul['max']
    test_results.drop(["rul"],axis=1,inplace=True)
    test=test.merge(test_results,on=['id'],how='left')
    test["remaining_cycle"]=test["rul_failed"]-test["cycle"]
    test.drop(["rul_failed"],axis=1,inplace=True)
    df_test['R_early'] = test['remaining_cycle'].apply(lambda x: cycle if x >= cycle else x)
    test_x = df_test.drop(["id","cycle","op1","op2","op3","sensor1","sensor5","sensor6","sensor10","sensor16",
    "sensor18","sensor19","sensor22","sensor23","remaining_cycle"],axis=1)
    return test_x
