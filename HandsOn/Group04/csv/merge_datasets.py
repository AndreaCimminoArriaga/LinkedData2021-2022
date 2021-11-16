import pandas as pd


def merge_csv_datasets(folder: str = "",
                       prefixes: list = None,
                       root: str = "",
                       suffixes: list = None,
                       **kwargs) -> pd.DataFrame:
    """
    Merge multiple CSV files into a single dataframe.
    :param folder: The folder containing the CSV files.
    :param prefixes: A list with the prefixes of the CSV files.
    :param root: The root of the CSV files.
    :param suffixes: A list with the suffixes of the CSV files.
    :param kwargs: Additional arguments to pass to pd.read_csv.
    :return: The merged dataframe.
    """

    if prefixes is not None and suffixes is not None:
        if len(prefixes) != len(suffixes):
            raise TypeError("prefixes and suffixes must have the same length")
    if prefixes is None and suffixes:
        prefixes = [""] * len(suffixes)
    if suffixes is None and prefixes:
        suffixes = [""] * len(prefixes)

    df = pd.DataFrame()

    for p, s in zip(prefixes, suffixes):
        temp_df = pd.read_csv(folder + "/" + p + root + s + ".csv", **kwargs)
        df = pd.concat([df, temp_df])

    return df


if __name__ == "__main__":

    suffixes1 = [month for month in ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep"] for _ in range(3)]
    prefixes1 = [year for _ in range(9) for year in ["19", "20", "21"]]

    suffixes2 = [month for month in ["oct", "sep", "dic"] for _ in range(2)]
    prefixes2 = [year for _ in range(3) for year in ["19", "20"]]

    suf = suffixes1 + suffixes2
    prefs = prefixes1 + prefixes2

    air_quality_df = merge_csv_datasets("air quality", suf, "_meteo", prefs, delimiter=";")
    air_quality_df.to_csv("air_quality_merged.csv", index=False)
    meteorological_data = merge_csv_datasets("meteorological data", suf, "_meteo", prefs, delimiter=";")
    meteorological_data.to_csv("meteorological_data_merged.csv", index=False)
