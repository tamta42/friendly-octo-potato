"""
Absolute minimal Taipy example to test basic functionality
"""

from taipy.gui import Gui
import pandas as pd

# Minimal data
data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Minimal page - no Markdown wrapper
page = "<|{data}|table|>"

if __name__ == "__main__":
    print("🧪 Running minimal Taipy test...")
    
    gui = Gui(page)
    
    # Try the most permissive settings
    try:
        gui.run(
            host="0.0.0.0",  # Listen on all interfaces
            port=8888,       # Different port
            debug=False,
            use_reloader=False
        )
    except Exception as e:
        print(f"Error: {e}")
        print("Taipy might have installation issues.")