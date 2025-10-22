import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Monthly Expense Tracker", page_icon="💰")

st.title("💰 Monthly Expense Tracker")
st.write("Track your monthly spending and visualize it with a pie chart.")

# --- Load or upload CSV ---
st.sidebar.header("📂 Load Monthly CSV File")
uploaded_file = st.sidebar.file_uploader("Upload your expenses.csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Please upload your expenses.csv file to continue.")
    st.stop()

# --- Show current pie chart ---
st.header("📊 Monthly Expense Overview")
category_totals = df.drop(columns=["Date"]).sum()

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
st.pyplot(fig)

st.write("### Total Spent Per Category")
st.dataframe(category_totals.to_frame("Amount (₹)"))

st.write(f"### 💵 Grand Total: ₹ {category_totals.sum():,.2f}")

# --- Add today's expense ---
st.header("🧾 Add Today's Expense")
with st.form("expense_form"):
    today = datetime.now().strftime("%Y-%m-%d")
    st.write(f"Date: {today}")
    new_row = {"Date": today}

    for col in df.columns[1:]:
        new_row[col] = st.number_input(f"{col} (₹)", min_value=0.0, step=100.0, format="%.2f")

    submitted = st.form_submit_button("Add Expense")

if submitted:
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("updated_expenses.csv", index=False)
    st.success("✅ Expense added successfully and saved to updated_expenses.csv!")
    st.write("Here’s your updated pie chart:")

    # Show updated pie chart
    category_totals = df.drop(columns=["Date"]).sum()
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig)
