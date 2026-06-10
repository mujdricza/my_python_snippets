import pandas as pd

def merge_column1(df_left, df_right, key: str, col: str) -> None:
    print("df_left")
    print(df_left)
    print("df_right")
    print(df_right)
    merged_df = pd.merge(df_left, df_right, on=key, how="outer", suffixes=('_left', '_right'))
    print("merged 1")
    print(merged_df)
    col_left = f"{col}_left"
    col_right = f"{col}_right"

    dummy_value = "DUMMY"
    merged_df[col_left] = merged_df[col_left].fillna(value=dummy_value)
    merged_df[col_right] = merged_df[col_right].fillna(value=dummy_value)
    print("merged_df dummy")
    print(merged_df)
    merged_df[col] = merged_df.apply(
        lambda row: list(
            (
                (set(row[col_left]) if row[col_left] != dummy_value else set())
                | (set(row[col_right]) if row[col_right] != dummy_value else set())
            )
            - set([dummy_value])
        ),
        axis=1,
    )
    print("merged 2")
    print(merged_df)


def _filling_up(l1, l2, dummy) -> list[str]:
    final_list = []
    print(f"l1: {l1}")
    print(f"l2: {l2}")
    l = [x for x in l1 if not (x in final_list or final_list.append(x))]
    print(f"-> l ith l1: {l}")
    l = [x for x in l2 if not (x in final_list or final_list.append(x))]
    print(f"-> l ith l2: {l}")
    if dummy in final_list:
        final_list.remove(dummy)
    print(f"final_list: {final_list}")
    return final_list


def merge_column2(df_left, df_right, key: str, col: str) -> None:
    print("df_left")
    print(df_left)
    print("df_right")
    print(df_right)
    merged_df = pd.merge(df_left, df_right, on=key, how="outer", suffixes=('_left', '_right'))
    print("merged 1")
    print(merged_df)
    col_left = f"{col}_left"
    col_right = f"{col}_right"

    dummy_value = "DUMMY"
    merged_df[col_left] = merged_df[col_left].fillna(value=dummy_value)
    merged_df[col_right] = merged_df[col_right].fillna(value=dummy_value)
    print("merged_df dummy")
    print(merged_df)

    merged_df[col] = (
        merged_df.apply(
            lambda x: _filling_up(
                x[col_left] if x[col_left] != dummy_value else [],
                x[col_right] if x[col_right] != dummy_value else [],
                dummy_value,
            ),
            axis=1,
        )

    )
    # print(f"merged_tp 2: {type(merged_tp)}, {len(merged_tp)}")
    # merged_df[col] = pd.Series(merged_tp)
    # print(merged_tp)
    # m_df = pd.DataFrame(merged_tp)
    # print(m_df)
    print(f"merged 2: {type(merged_df)}")
    print(merged_df)


def main():

    df_left = pd.DataFrame.from_records([
        {"i": 1, "a": [1, 2, None]},
        {"i": 2, "a": [1, None, 2]},
        {"i": 3, "a": [1, 2, 3]},
        {"i": 5, "a": [1, 2, 3]},

    ])
    df_right = pd.DataFrame.from_records(
        [
            {"i": 1, "a": [1, 2, 33]},
            {"i": 2, "a": [11, None, 2]},
            {"i": 3, "a": [1, 2, 33]},
            {"i": 4, "a": [1, 2, 33]},
        ]
    )
    # df_merged1 = merge_column1(df_left, df_right, key="i", col="a")
    df_merged2 = merge_column2(df_left, df_right, key="i", col="a")

    """
    with merge_colum1()
    
df_left
   i             a
0  1  [1, 2, None]
1  2  [1, None, 2]
2  3     [1, 2, 3]
3  5     [1, 2, 3]
df_right
   i              a
0  1     [1, 2, 33]
1  2  [11, None, 2]
2  3     [1, 2, 33]
3  4     [1, 2, 33]
merged 1
   i        a_left        a_right
0  1  [1, 2, None]     [1, 2, 33]
1  2  [1, None, 2]  [11, None, 2]
2  3     [1, 2, 3]     [1, 2, 33]
3  5     [1, 2, 3]            NaN
4  4           NaN     [1, 2, 33]
merged_df dummy
   i        a_left        a_right
0  1  [1, 2, None]     [1, 2, 33]
1  2  [1, None, 2]  [11, None, 2]
2  3     [1, 2, 3]     [1, 2, 33]
3  5     [1, 2, 3]          DUMMY
4  4         DUMMY     [1, 2, 33]
merged 2
   i        a_left        a_right                 a
0  1  [1, 2, None]     [1, 2, 33]  [1, 2, None, 33]
1  2  [1, None, 2]  [11, None, 2]  [1, 2, 11, None]
2  3     [1, 2, 3]     [1, 2, 33]     [1, 2, 3, 33]
3  5     [1, 2, 3]          DUMMY         [1, 2, 3]
4  4         DUMMY     [1, 2, 33]        [1, 2, 33]
    """


if __name__ == "__main__":
    main()
