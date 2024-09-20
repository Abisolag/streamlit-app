pip install matplotlib
pip install pandas
pip install seaborn
pip install plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df=pd.read_csv('new_data.csv')

# Set the background image and style
st.markdown("""
    <style>
    .reportview-container {
        background: url('https://drive.google.com/file/d/1M9veuEBmAHeLrqDba8urdGvIUP_WdBoe/view?usp=sharing') no-repeat center center fixed;
        background-size: cover;
    }
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# Function for landing page
def landing_page():
    st.title("Welcome to My Streamlit App")
    st.write("This is the landing page with a background image.")
    st.write("Click on the sidebar to navigate to different sections.")

# Function for univariate analysis
def univariate_analysis():
    st.header("Univariate Analysis")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    cat_columns = df.select_dtypes(include=['object']).columns

    column = st.sidebar.selectbox("Select a column for Univariate Analysis", numeric_columns.tolist() + cat_columns.tolist())

    if column in numeric_columns:
        st.write("Histogram:")
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=20, color='orange')
        ax.grid(False)
        st.pyplot(fig)

        st.write("Box plot:")
        fig, ax = plt.subplots()
        sns.boxplot(df[column], ax=ax, color='green')  # Example color
        st.pyplot(fig)

    elif column in cat_columns:
        st.write(f"Value counts for {column}:")
        st.write(df[column].value_counts())

        st.write("Bar chart:")
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='bar', ax=ax, color='red') 
        st.pyplot(fig)

# Function for bivariate analysis
def bivariate_analysis():
    st.header("Bivariate Analysis")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    cat_columns = df.select_dtypes(include=['object']).columns

    col1 = st.sidebar.selectbox("Select first variable", numeric_columns.tolist() + cat_columns.tolist())
    col2 = st.sidebar.selectbox("Select second variable", numeric_columns.tolist() + cat_columns.tolist())

    if col1 in numeric_columns and col2 in numeric_columns:
        st.write(f"Scatter plot of {col1} vs {col2}:")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col1], y=df[col2], ax=ax, color='blue')  
        st.pyplot(fig)

    elif col1 in cat_columns and col2 in numeric_columns:
        st.write(f"Box plot of {col1} vs {col2}:")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col1], y=df[col2], ax=ax, palette='coolwarm')  
        st.pyplot(fig)

    elif col1 in numeric_columns and col2 in cat_columns:
        st.write(f"Box plot of {col1} vs {col2}:")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col2], y=df[col1], ax=ax, palette='coolwarm')  
        st.pyplot(fig)

    elif col1 in cat_columns and col2 in cat_columns:
        st.write(f"Bar plot of {col1} vs {col2}:")
        ct = pd.crosstab(df[col1], df[col2])
        st.write(ct)

        fig, ax = plt.subplots()
        ct.plot(kind='bar', ax=ax, color='purple')  
        st.pyplot(fig)

# Function for advanced visualizations
def advanced_visualizations():
    st.header("Advanced Visualizations")

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    col1 = st.sidebar.selectbox("Select first numerical variable for advanced plot", numeric_columns)
    col2 = st.sidebar.selectbox("Select second numerical variable for advanced plot", numeric_columns)

    st.write(f"Interactive Plotly scatter plot of {col1} vs {col2}:")
    fig = px.scatter(df, x=col1, y=col2, color_discrete_sequence=['cyan'])
    st.plotly_chart(fig)

    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    selected_cat_col = st.sidebar.selectbox("Select categorical variable for box plot", categorical_columns)
    selected_num_col = st.sidebar.selectbox("Select numerical variable for box plot", numeric_columns)

    if selected_cat_col in df.columns and selected_num_col in df.columns:
        st.write(f"Box plot of {selected_num_col} grouped by {selected_cat_col}:")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[selected_cat_col], y=df[selected_num_col], ax=ax, palette='coolwarm')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Landing Page", "Analysis"])

# Display the selected page
if page == "Landing Page":
    landing_page()
elif page == "Analysis":
    # Sidebar for analysis sections
    st.sidebar.title("Analysis Sections")
    section = st.sidebar.selectbox("Choose Analysis Type", ['Univariate Analysis', 'Bivariate Analysis', 'Advanced Visualizations'])

    if section == 'Univariate Analysis':
        univariate_analysis()
    elif section == 'Bivariate Analysis':
        bivariate_analysis()
    elif section == 'Advanced Visualizations':
        advanced_visualizations()
