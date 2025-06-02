# print-dataframe-with-headers.py

import pandas as pd

# Define the DFPlus class
class DFPlus(pd.DataFrame):
    # Make sure when DataFrame methods return new objects, they are DFPlus objects
    @property
    def _constructor(self):
        return DFPlus

    # Class method to create DFPlus from CSV
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    # Print with column headers every 10 rows
    def print_with_headers(self):
        total_rows = len(self)
        for start in range(0, total_rows, 10):
            end = start + 10
            print(f"\nRows {start + 1} to {min(end, total_rows)}:\n")
            print(self.iloc[start:end])  # Uses super().iloc implicitly
            print("-" * 40)

# Main block to test the class
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")  # create DFPlus instance
    dfp.print_with_headers()  # print with headers every 10 rows
