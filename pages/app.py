import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use('seaborn-v0_8')
st.title('World Cities')

# 读取根目录下的worldcities.csv
csv_path = os.path.join(os.path.dirname(__file__), "..", "worldcities.csv")
df = pd.read_csv(csv_path)

# 人口滑块（单位百万）
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)

# 首都多选框
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),
     df.capital.unique())

# 国家输入表单
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

# 筛选数据
df = df[df.population >= population_filter]
df = df[df.capital.isin(capital_filter)]
if country_filter!='ALL':
    df = df[df.country == country_filter]

# 处理空数据
if df.empty:
    st.warning("No cities match your filter!")
else:
    # 地图
    st.map(df)
    # 表格
    st.subheader('City Details:')
    st.write(df[['city', 'country', 'population']])
    # 绘图
    st.subheader('Total Population By Country')
    fig, ax = plt.subplots(figsize=(12, 5))
    pop_sum = df.groupby('country')['population'].sum()
    pop_sum.plot.bar(ax=ax)
    st.pyplot(fig)

