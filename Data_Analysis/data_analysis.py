from sys import displayhook
import pandas as pd
import matplotlib.pyplot as plt


def analyze_dataset(file_path):
    # Read the dataset
    df = pd.read_csv(file_path)

    # Set display options for pandas
    pd.set_option("display.max_columns", None)  # Show all columns
    pd.set_option("display.width", 1000)  # Set display width

    # Display the number of rows and columns
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # Display the first few rows with borders
    displayhook(
        df.head().style.set_table_styles(
            [
                {"selector": "th", "props": [("border", "2px solid white")]},
                {"selector": "td", "props": [("border", "2px solid white")]},
            ]
        )
    )

    # Analyze and plot the 'label' column if it exists
    if "label" in df.columns:
        label_counts = df["label"].value_counts()
        # Get the number of good and bad URLs
        num_good = label_counts.get("good", 0)  # Default to 0 if 'good' is not a key
        num_bad = label_counts.get("bad", 0)  # Default to 0 if 'bad' is not a key
        print(f"Number of good URLs: {num_good}")
        print(f"Number of bad URLs: {num_bad}")

        # Plotting the histogram with specific counts
        plt.bar(["good", "bad"], [num_good, num_bad])
        plt.xlabel("Label")
        plt.ylabel("Count")
        plt.title("Distribution of Good and Bad URLs")
        plt.show()
    else:
        print("Column 'label' not found in the dataset.")


# Example usage
# analyze_dataset('path_to_your_dataset.csv')
