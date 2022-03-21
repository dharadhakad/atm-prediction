import numpy as np
import joblib
import sklearn
import pandas
import streamlit as st
reg = joblib.load('KNN.joblib')

def welcome():
    return "Welcome"

def pred_yield(weekday, holiday, trans_date_set, trans_month, trans_year, osmia,prevweek_mean):

    prediction = reg.predict([[weekday, holiday, trans_date_set, trans_month, trans_year, osmia,prevweek_mean]])
    print('prediction')
    return prediction


def main():

    st.title('ATM Amount Prediction')

    Date = st.text_input('Date(DD/MM/YYYY)','Type Here')
    weekday = st.text_input('weekday(in number i.e. 1 for sunday)','Type Here')
    holiday = st.text_input('Holiday (H for holiday, W for working day)','Type Here')
    trans_date_set = st.text_input('DATE (DD)','Type Here')
    trans_month = st.text_input('MONTH','Type Here')
    trans_year = st.text_input('YEAR','Type Here')
    prevweek_mean = st.text_input('Previous Week Average','Type Here')
    pred=""
    result=0
    row=1
    if st.button("Predict"):
        result=pred_yield(weekday, holiday, trans_date_set, trans_month, trans_year, osmia,prevweek_mean)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built by Dhara Dhakad")


if __name__ == '__main__':

    main()
