"""
Simple Taipy GUI Example
A basic web application showing Taipy's GUI capabilities with:
- Text input
- Slider control
- Chart visualization
- Data table
"""

import taipy as tp
from taipy.gui import Gui, Markdown
import pandas as pd
import numpy as np

# Sample data for demonstration
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [1200, 1500, 1800, 1300, 1700, 2000],
    'Expenses': [800, 900, 1100, 850, 1000, 1200]
})

# Variables that will be used in the GUI
text_input = "Hello, Taipy!"
slider_value = 50
name = "World"

# Function that gets called when slider changes
def on_slider_change(state):
    """Update the chart based on slider value"""
    # Generate new random data based on slider value
    np.random.seed(int(state.slider_value))
    state.data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': np.random.randint(1000, 2500, 6),
        'Expenses': np.random.randint(500, 1500, 6)
    })

# Function for text input changes
def on_text_change(state):
    """React to text input changes"""
    print(f"Text changed to: {state.text_input}")

# Define the page layout using Markdown
page = Markdown("""
# 🎉 Welcome to Taipy!

## Personal Greeting
Hello **{name}**! 

**Enter your name:** <|{name}|text|>

---

## Interactive Controls

**Your message:** <|{text_input}|text|on_change=on_text_change|>

**Slider value:** <|{slider_value}|slider|min=0|max=100|step=1|on_change=on_slider_change|>

Current value: **{slider_value}**

---

## 📊 Sample Data Visualization

<|{data}|chart|x=Month|y[1]=Sales|y[2]=Expenses|type=bar|title=Monthly Sales vs Expenses|>

---

## 📋 Data Table

<|{data}|table|>

---

## 🎮 Try This:
1. **Change your name** in the text field above
2. **Move the slider** to see the chart update with new random data
3. **Type in the message box** to see console output

*This is a simple example showing Taipy's reactive GUI capabilities!*
""")

if __name__ == "__main__":
    # Create the Gui instance
    gui = Gui(page)
    
    # Run the application
    print("🚀 Starting Taipy application...")
    print("💡 Open your browser to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    
    gui.run(
        title="Simple Taipy Example",
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=True
    )