
import pandas as pd

from src.general_utils.io_utils import write_excel

def get_df():
    data = [
        {'A': 5, 'C': 3, 'D': 3},
        {'A': 7, 'B': 9, 'F': 5},
        {'A': 4, 'C': 7, 'E': 6}
    ]

    df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E", "F"]).set_index('A')

    return df

if __name__ == '__main__':
    df = get_df()

    print(df)
    # index_header = df.index.name  # "A"
    write_excel(df, 'pandas_exp.xlsx', write_index=True)

    """
    A	B	C	D	E	F
    5		3	3		
    7	9				5
    4		7		6	
    """
    dft = df.T
    dft.index.name = "X"
    print(dft)
    write_excel(dft, 'pandas_expT.xlsx', write_index=True)

    """
    X	5	7	4
    B		9	
    C	3		7
    D	3		
    E			6
    F		5	
    """