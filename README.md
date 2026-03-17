💰 Monthly Expense Tracker

A Streamlit-based web application to track, analyze, and manage monthly expenses efficiently.

Users can upload their expense dataset, visualize spending patterns, add new expenses, and download the updated data—all within a simple interface.

🚀 Features

Upload expense data using CSV

View uploaded dataset in table format

Visualize expenses using a pie chart

Category-wise expense breakdown

Display total spending per category

Calculate overall monthly expenditure

Add new daily expenses dynamically

Automatically update dataset

Download updated CSV file

🛠️ Tech Stack

Python

Streamlit

Pandas

Matplotlib

▶️ Getting Started
1. Clone the Repository
git clone https://github.com/your-username/monthly-expense-tracker.git
cd monthly-expense-tracker
2. Install Dependencies
pip install -r requirements.txt
3. Run the Application
streamlit run app.py
📊 Dataset Format

Ensure your CSV file follows this structure:

Date,Food,Transport,Shopping,Entertainment,Others
2026-03-01,200,100,500,150,50
2026-03-02,300,50,200,100,80

The first column must be Date

Remaining columns represent expense categories

📌 Functional Overview
🔹 Data Visualization

Pie chart showing category-wise expense distribution

🔹 Expense Analysis

Total spending per category

Grand total calculation

🔹 Expense Management

Add new daily expenses

Automatically updates dataset

📥 Output

Updated dataset is saved as:

updated_expenses.csv
💡 Future Enhancements

Monthly and date filters

Custom category support

Additional visualizations (bar chart, line chart)

Budget tracking and alerts

🤝 Contributor

Pranesh Raj S
