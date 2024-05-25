import pm4py # type: ignore
import pandas as pd



log = pm4py.read_xes('./data/RequestForPayment.xes')
dataframe = pm4py.convert_to_dataframe(log)

dataframe.to_csv('RequestForPayment.csv', sep=';', decimal=",")