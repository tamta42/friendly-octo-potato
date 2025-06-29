"""
Fixed Taipy Demo - Ensuring variables display correctly
"""

from taipy.gui import Gui, Markdown
import pandas as pd

# Simple data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

# Variables for the GUI - these should display their values
text = "Hello Taipy!"
number = 42

# Test different variable binding approaches
page = """
# 🎉 Taipy is Working!

## Text Display
**Message:** {text}

## Number Display  
**Number:** {number}

## Interactive Text Input
**Try editing this:** <|{text}|text|>

## Simple Table
<|{data}|table|>

## Debug Info
- Text variable contains: "{text}"
- Number variable contains: {number}
- Data has {len(data)} rows

## Success! 
If you can see the actual values above (not {text} or {number}), then Taipy is working correctly!
"""

if __name__ == "__main__":
    # Create Gui instance and pass variables explicitly
    gui = Gui(page)
    
    print("🚀 Starting fixed Taipy demo...")
    print("💡 Open your browser to: http://127.0.0.1:5002")
    print(f"📊 Debug - text='{text}', number={number}")
    
    try:
        gui.run(
            title="Fixed Taipy Demo",
            host="127.0.0.1",
            port=5002,
            debug=True,
            use_reloader=False
        )
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try a different port or check for conflicts")