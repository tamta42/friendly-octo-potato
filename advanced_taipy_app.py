"""
Advanced Taipy Example: Data Processing Pipeline
This example demonstrates:
- File upload
- Data processing scenarios
- Multiple scenarios comparison
- Configuration management
"""

import taipy as tp
from taipy.gui import Gui, Markdown
from taipy import Config
from taipy.core import Task, DataNode
import pandas as pd
import numpy as np

# Sample datasets for demonstration
def generate_sample_data():
    """Generate sample sales data"""
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    return pd.DataFrame({
        'Date': dates,
        'Product': np.random.choice(['Widget A', 'Widget B', 'Widget C'], 100),
        'Sales': np.random.randint(100, 1000, 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
    })

# Data processing functions
def clean_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare the data"""
    # Remove any null values
    cleaned = raw_data.dropna()
    
    # Add calculated fields
    cleaned = cleaned.copy()
    cleaned['Month'] = pd.to_datetime(cleaned['Date']).dt.strftime('%Y-%m')
    cleaned['Revenue'] = cleaned['Sales'] * np.random.uniform(10, 50, len(cleaned))
    
    return cleaned

def analyze_data(cleaned_data: pd.DataFrame) -> pd.DataFrame:
    """Perform data analysis"""
    # Group by month and product
    analysis = cleaned_data.groupby(['Month', 'Product']).agg({
        'Sales': ['sum', 'mean'],
        'Revenue': ['sum', 'mean']
    }).round(2)
    
    # Flatten column names
    analysis.columns = ['_'.join(col).strip() for col in analysis.columns]
    analysis = analysis.reset_index()
    
    return analysis

def create_summary(analysis: pd.DataFrame) -> pd.DataFrame:
    """Create executive summary"""
    total_sales = analysis['Sales_sum'].sum()
    total_revenue = analysis['Revenue_sum'].sum()
    avg_sales = analysis['Sales_mean'].mean()
    
    summary = pd.DataFrame({
        'Metric': ['Total Sales', 'Total Revenue', 'Average Daily Sales', 'Number of Products'],
        'Value': [f"{total_sales:,.0f}", f"${total_revenue:,.2f}", f"{avg_sales:.1f}", len(analysis['Product'].unique())]
    })
    
    return summary

# Configure Taipy Core data processing pipeline
Config.configure_data_node(id="raw_data", default_data=generate_sample_data())
Config.configure_data_node(id="cleaned_data")
Config.configure_data_node(id="analysis_data")
Config.configure_data_node(id="summary_data")

Config.configure_task(id="clean_task", function=clean_data, input="raw_data", output="cleaned_data")
Config.configure_task(id="analyze_task", function=analyze_data, input="cleaned_data", output="analysis_data")
Config.configure_task(id="summary_task", function=create_summary, input="analysis_data", output="summary_data")

Config.configure_scenario(id="analysis_scenario", 
                         task_configs=["clean_task", "analyze_task", "summary_task"])

# GUI variables
scenario = None
raw_data = generate_sample_data()
cleaned_data = pd.DataFrame()
analysis_data = pd.DataFrame()
summary_data = pd.DataFrame()

# GUI callback functions
def run_analysis(state):
    """Run the complete data analysis pipeline"""
    print("🔄 Running analysis pipeline...")
    
    # Create a new scenario
    state.scenario = tp.create_scenario(Config.scenarios["analysis_scenario"])
    
    # Set the input data
    state.scenario.raw_data.write(state.raw_data)
    
    # Execute the pipeline
    state.scenario.submit()
    
    # Get the results
    state.cleaned_data = state.scenario.cleaned_data.read()
    state.analysis_data = state.scenario.analysis_data.read()
    state.summary_data = state.scenario.summary_data.read()
    
    print("✅ Analysis complete!")

def generate_new_data(state):
    """Generate new sample data"""
    print("🎲 Generating new sample data...")
    state.raw_data = generate_sample_data()
    print("✅ New data generated!")

# Define the page layout
page = Markdown("""
# 📈 Advanced Taipy Data Processing

## 🎯 Data Pipeline Demo
This example shows how Taipy can create automated data processing pipelines.

---

## 📊 Raw Data

**Current dataset:** {len(raw_data)} records

<|Generate New Data|button|on_action=generate_new_data|>

<|{raw_data}|table|page_size=10|>

---

## 🚀 Run Analysis Pipeline

<|Run Complete Analysis|button|on_action=run_analysis|active={len(raw_data) > 0}|>

---

## 📋 Executive Summary
<|{summary_data}|table|show_all|>

---

## 📈 Monthly Analysis
<|{analysis_data}|table|page_size=10|>

---

## 📊 Visualizations

### Sales by Product (Monthly Totals)
<|{analysis_data}|chart|x=Month|y=Sales_sum|color=Product|type=bar|title=Monthly Sales by Product|>

### Revenue Trend
<|{analysis_data}|chart|x=Month|y=Revenue_sum|color=Product|type=line|title=Revenue Trend by Product|>

---

## ℹ️ How It Works:

1. **Data Input**: Raw sales data with dates, products, and sales figures
2. **Cleaning**: Remove nulls, add calculated fields
3. **Analysis**: Group by month/product, calculate totals and averages
4. **Summary**: Create executive summary metrics
5. **Visualization**: Interactive charts showing trends

**Try this:**
1. Click "Generate New Data" to create a new dataset
2. Click "Run Complete Analysis" to process the data through the pipeline
3. Explore the results in the tables and charts below

*This demonstrates Taipy's ability to create reusable, configurable data processing workflows!*
""")

if __name__ == "__main__":
    # Create the Gui instance
    gui = Gui(page)
    
    # Run the application
    print("🚀 Starting Advanced Taipy application...")
    print("💡 Open your browser to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    
    gui.run(
        title="Advanced Taipy Data Processing",
        host="127.0.0.1",
        port=5001,
        debug=True,
        use_reloader=True
    )