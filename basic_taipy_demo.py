"""
Basic Taipy Demo - Minimal example to test installation
"""

from taipy.gui import Gui, Markdown
import pandas as pd

# Simple data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

# Variables for the GUI
text = "Hello Taipy!"
number = 42

# Simple page
page = Markdown("""
# 🎉 Taipy is Working!

## Text Display
**Message:** {text}

## Number Display  
**Number:** {number}

## Simple Table
<|{data}|table|>

## Success! 
If you can see this page, Taipy is working correctly on your system.
""")

if __name__ == "__main__":
    gui = Gui(page)
    print("🚀 Starting basic Taipy demo...")
    print("💡 Open your browser to: http://127.0.0.1:5000")
    
    try:
        gui.run(
            title="Basic Taipy Demo",
            host="127.0.0.1",
            port=5000,
            debug=False,
            use_reloader=False
        )
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try running with different settings...")