import pandas as pd


def check_pandas_installation():
    try:
        # Create a simple DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Tokyo']
        }
        df = pd.DataFrame(data)

        # Print DataFrame
        print("Pandas is installed correctly! 🎉")
        print("\nSample DataFrame:")
        print(df)

        # Basic operations
        print("\nBasic DataFrame Info:")
        print(df.info())

        return True
    except ImportError:
        print("❌ Pandas is not installed. Install it using: `pip install pandas`")
        return False


# Run the check
if __name__ == "__main__":
    check_pandas_installation()