import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt








df = pd.read_csv("g:\Shared drives\CT_Data_Files\DataSets\SalaryInfo\salaries.csv")

selected_columns = ['Employer', 'Job Title', 'Years of Experience', 'Location']
selected_df = df[selected_columns]
st.write(selected_df)




st.write("Annual Base Pay")
chart_data = pd.DataFrame(np.random.randn(20, 1), columns=["h"])
st.bar_chart(chart_data)

value_counts = df['Years at Employer'].value_counts()
st.write("### Years at Employer Pie Chart")
fig, ax = plt.subplots()
ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)