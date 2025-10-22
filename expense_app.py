import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#Page Config
st.set_page_config(page_title="Monthly Expense Tracker", page_icon="💰")
st.title("💰 Monthly Expense Tracker")

#Upload CSV
uploaded_file = st.file_uploader("Upload your expenses.csv file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded CSV")
    st.dataframe(df)

    #Function to show pie chart and totals
    def show_chart(dataframe):
        category_totals = dataframe.drop(columns=["Date"]).sum()
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=140)
        st.pyplot(fig)
        st.write("### Total per category")
        st.dataframe(category_totals.to_frame("Amount (₹)"))
        st.write(f"💵 Grand Total: ₹ {category_totals.sum():,.2f}")

    #Show chart for uploaded CSV
    show_chart(df)

    st.write("### Add Today's Expense")
    today = datetime.now().strftime("%Y-%m-%d")
    new_expense = {}
    
    # Input fields for each category
    for col in df.columns[1:]:
        new_expense[col] = st.number_input(f"{col} (₹)", min_value=0.0, value=0.0)

    # Add expense button
    if st.button("Add Expense"):
        new_row = {"Date": today, **new_expense}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv("updated_expenses.csv", index=False)
        st.success("Expense added! CSV updated.")
        
        # Show updated chart
        show_chart(df)

    # Download updated CSV
    st.download_button(
        label="📥 Download Updated CSV",
        data=df.to_csv(index=False),
        file_name="updated_expenses.csv",
        mime="text/csv"
    )


