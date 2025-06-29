"""
Test different Taipy configurations to find what works
"""

from taipy.gui import Gui, Markdown
import pandas as pd
import socket

# Simple test data
data = pd.DataFrame({'Test': [1, 2, 3], 'Value': ['A', 'B', 'C']})
text = "Working!"

page = """
# Taipy Test

Message: {text}

<|{data}|table|>
"""

def find_free_port():
    """Find an available port"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port

def test_config(host, port, name):
    """Test a specific configuration"""
    print(f"\n🧪 Testing {name}: http://{host}:{port}")
    try:
        gui = Gui(page)
        gui.run(
            title=f"Taipy Test - {name}",
            host=host,
            port=port,
            debug=False,
            use_reloader=False,
            run_browser=True  # Try to auto-open browser
        )
    except Exception as e:
        print(f"❌ {name} failed: {e}")
        return False
    return True

if __name__ == "__main__":
    port = find_free_port()
    print(f"🔍 Found free port: {port}")
    
    configs_to_try = [
        ("0.0.0.0", port, "All interfaces"),
        ("localhost", port, "Localhost"),
        ("127.0.0.1", port, "Loopback"),
    ]
    
    print("🚀 Testing different network configurations...")
    print("⚠️  Try each URL in your browser if auto-open doesn't work")
    
    for host, test_port, name in configs_to_try:
        print(f"\n{'='*50}")
        print(f"Testing {name}: http://{host}:{test_port}")
        print(f"{'='*50}")
        
        try:
            gui = Gui(page)
            print(f"✅ Starting server on {host}:{test_port}")
            print(f"🌐 Open: http://{host}:{test_port}")
            print("⏹️  Press Ctrl+C to try next configuration")
            
            gui.run(
                title=f"Taipy - {name}",
                host=host,
                port=test_port,
                debug=False,
                use_reloader=False
            )
        except KeyboardInterrupt:
            print(f"\n⏭️  Moving to next configuration...")
            continue
        except Exception as e:
            print(f"❌ {name} failed: {e}")
            continue