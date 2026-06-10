import importlib
import json
import os
import sys
from enum import Enum
from typing import Any, Callable, Dict, List, Set, Tuple

import pandas as pd
import yaml


class IO(Enum):
    json_extension = ".json"
    txt_extension = ".txt"
    xlsx_extension = ".xlsx"
    yml_extension = ".yml"
    yaml_extension = ".yaml"


def read_json(json_path: str) -> Dict | List:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def read_dict_jsons(input_paths: List[str]) -> Dict:
    """Reading multiple json files with same structure.
    If it is a dictionary, the key content in the individual files should be distinct!
    """
    if not input_paths:
        raise ValueError("No input paths provided")
    all_data: List = []
    for input_path in input_paths:
        data = read_json(input_path)
        all_data.append(data)

    if isinstance(all_data[0], Dict):
        merged_data: Dict = {}
        for data in all_data:
            merged_data.update(data)
        return merged_data
    # elif isinstance(all_data[0], List):
    #     merged_data = []
    #     for data in all_data:
    #         merged_data.extend(data)
    else:
        raise NotImplementedError(f"Not handling type {type(all_data[0])}")
    #return merged_data


def write_json(data: Dict | List, json_path: str, indentation: int = 2) -> None:
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indentation)


def read_yaml(config_path: str) -> Dict:
    with open(config_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def read_text(input_path: str) -> str:
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read()


def read_text_lines(input_path: str,
                    reformatting_function: Callable | None = str.strip,
                    encoding: str = "utf-8") -> List[str]:
    with open(input_path, "r", encoding=encoding) as f:
        lines = f.readlines()
        if reformatting_function:
            lines = [reformatting_function(l) for l in lines]
        return lines


def read_csv(
    input_path: str,
    delimiter: str = ",",
    header_rows: int = 0,

) -> pd.DataFrame:
    return pd.read_csv(input_path, sep=delimiter, header=header_rows)


class YamlDumperWithIndentation(yaml.Dumper):
    """Solution for indentation in YAML dumper.
    See
    - https://github.com/yaml/pyyaml/issues/234
    - https://stackoverflow.com/questions/25108581/python-yaml-dump-bad-indentation
    """

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


def write_yaml(
    data: List | Dict,
    output_path: str,
    explicit_start: bool = False,
    indent: int = 2,
    sort_keys: bool = False,
) -> None:
    with open(output_path, encoding="utf-8", mode="w") as f:
        yaml.dump(
            data,
            stream=f,
            Dumper=YamlDumperWithIndentation,
            explicit_start=explicit_start,
            sort_keys=sort_keys,
            indent=indent,
            default_flow_style=False,
            allow_unicode=True,
            line_break=os.linesep,
        )


def print_yaml(
    data: List | Dict,
    explicit_start: bool = False,
    indent: int = 2,
    sort_keys: bool = False,
) -> None:
    yaml.dump(
        data,
        stream=sys.stdout,
        Dumper=YamlDumperWithIndentation,
        explicit_start=explicit_start,
        sort_keys=sort_keys,
        indent=indent,
        default_flow_style=False,
        allow_unicode=True,
        line_break=os.linesep,
    )


def read_excel(
    excel_path: str,
    sheet_name: str | None = None
) -> pd.DataFrame | Dict[str, pd.DataFrame]:
    # if there are multiple sheets in the excel file, and the given sheet_name
    # is None, all sheets will be read in a dictionary with sheet name as key
    # and the sheet content as dataframe.
    return pd.read_excel(excel_path, sheet_name=sheet_name)


def read_excel_all_sheets(input_path: str) -> Dict[str, pd.DataFrame]:
    all_sheets_data_df = pd.read_excel(
        input_path, sheet_name=None
    )  # Note sheet_name=None for getting all sheets
    return all_sheets_data_df


def read_excel_sheet(input_path: str, sheet_name) -> pd.DataFrame:
    all_sheets_df = read_excel_all_sheets(input_path)
    sheet_names = all_sheets_df.keys()
    if sheet_name in sheet_names:
        data_df = all_sheets_df[sheet_name]
        return data_df
    raise ValueError(f"Sheet '{sheet_name}' not found in '{input_path}'.")


def write_excel(
    df: pd.DataFrame,
    output_path: str,
    write_index: bool = False,
    strings_to_formulas: bool = False,  # see https://github.com/pandas-dev/pandas/issues/29095
) -> None:
    df.to_excel(output_path, index=write_index,
                # NOTE that engine_kwargs could not be working here (but would work if added to a writer or workbook, see write_excel_with_sheets()
                engine_kwargs={"options": {"strings_to_formulas": strings_to_formulas}}
                )


def _filter_for_file_extensions(
    file_names: List[str], file_extensions: Tuple[str, ...]
) -> List[str]:
    files_with_extension = [
        file
        for file in file_names
        for file_extension in file_extensions
        if file.endswith(file_extension)
    ]
    return files_with_extension


def _join_with_root(root_dir: str, file_names: List[str]) -> List[str]:
    return [os.path.join(root_dir, file) for file in file_names]


def _get_files_in_dir_recursively(
    input_dir: str, file_extensions: Tuple[str, ...]
) -> List[str]:
    paths = []
    for root, dirs, files in os.walk(input_dir):
        files_with_extension = _filter_for_file_extensions(files, file_extensions)
        paths.extend(_join_with_root(root, files_with_extension))
    return paths


def _get_files_in_dir_shallow(
    input_dir: str, file_extensions: Tuple[str, ...]
) -> List[str]:
    files = os.listdir(input_dir)
    files_with_extension = _filter_for_file_extensions(files, file_extensions)
    paths = _join_with_root(input_dir, files_with_extension)
    return paths


def get_files(
    input_path: str,
    file_extensions: Tuple[str, ...],
    recursive_search: bool = False
) -> List[str]:

    input_path = os.path.realpath(input_path)
    if os.path.isfile(input_path):
        return [input_path]
    elif os.path.isdir(input_path):
        return get_files_in_dir(input_path, file_extensions, recursive_search)
    else:
        raise ValueError(f"Please provide a path to a file or directory.")


def get_files_in_dir(
    input_dir: str,
    allowed_file_extensions: str | Tuple[str, ...],
    recursive_search: bool = False,
) -> List[str]:
    """Get all files in a directory with given file extension(s).

    :param input_dir: Input directory path.
    :param allowed_file_extensions: Considered file extension(s).
    :param recursive_search: set to True, if search for files should be done recursively.
    :return: List of file paths with given file extension(s).
    """
    allowed_file_extensions = (
        tuple([allowed_file_extensions])
        if isinstance(allowed_file_extensions, str)
        else allowed_file_extensions
    )
    return (
        _get_files_in_dir_recursively(input_dir, allowed_file_extensions)
        if recursive_search
        else _get_files_in_dir_shallow(input_dir, allowed_file_extensions)
    )


def get_shared_path_part(input_paths: List[str]) -> str:
    """NOTE that absolute paths/directories are expected as input."""
    shared = input_paths[0]
    for i in range(1, len(input_paths)):
        for idx, e1_e2 in enumerate(zip(shared, input_paths[i])):
            e1, e2 = e1_e2
            if e1 != e2:
                shared = shared[:idx]
                break
    return shared


def sort_dict_on_key(
    dictionary: Dict[str|int|float|None|tuple|bool, Any]
) -> Dict[str|int|float|None|tuple|bool, Any]:
    k0 = list(dictionary.keys())[0]
    if isinstance(k0, str):
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[0].lower()))
    elif isinstance(k0, (int, float, type(None), tuple, bool)):
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    else:
        raise TypeError(f"Not handled type for sorting: {type(k0)}")
    return dictionary


def sort_on_key_and_value(
    data: Dict|List|Set,
    sort_on_key: bool,
    deduplicate: bool,
) -> Dict|List|Set:
    if isinstance(data, list):
        if deduplicate:
            if len(data) > 0:
                if isinstance(data[0], dict):
                    pass
                else:
                    data = list(set(data))
        if len(data) > 0:
            if isinstance(data[0], (dict, list, tuple)):
                data = [sort_on_key_and_value(el, sort_on_key, deduplicate) for el in data]
            elif isinstance(data[0], str):
                data = sorted(data, key=lambda item: item.lower())
            elif isinstance(data[0], (int, float, type(None), bool)):
                data = sorted(data)
            else:
                raise TypeError(f"Not handled type for sorting: {type(data[0])}")
    elif isinstance(data, dict):
        if sort_on_key:
            data = sort_dict_on_key(data)
        for key, value in data.items():
            sorted_value = sort_on_key_and_value(value, sort_on_key, deduplicate)
            data[key] = sorted_value
    elif isinstance(data, (str, int, float, type(None), bool, tuple, set)):
        pass
    else:
        raise TypeError(f"Not handled type for sorting: {type(data)}")
    return data


def sort_dict_or_list(
    data: Dict | List, sort_on_key: bool = True, deduplicate: bool = True
) -> Dict | List:
    data = sort_on_key_and_value(data, sort_on_key, deduplicate)
    return data


class ExcelFormat(Enum):
    """Some constants for the output excel file."""
    HEADER_FORMAT = tuple({"text_wrap": True, "bold": True}.items())
    CELL_FORMAT = tuple({}.items())
    FREEZED_ROWS = 1
    FREEZED_COLUMNS = 0

    DEFAULT_CELL_WIDTH: int = 20
    CELL_WIDTHS: Dict[str, int] = {
        # key is the name of the column, value is the width of the column
        "path": 50,
        "utterance": 50,
        "utterances": 50,
        "intent": 25,
        "column": 80,
        "description": 80,
        "information": 80,
        "result": 10,
        # for index column
        "index": 7,
        "None": 5,
    }

    @classmethod
    def get_excel_cell_width(cls, column_name: str) -> int:
        for name, width in cls.CELL_WIDTHS.value.items():
            if column_name.endswith(name):
                return width
        return cls.DEFAULT_CELL_WIDTH.value


def write_excel_with_sheets(
    collected_data_for_sheets: Dict[str, pd.DataFrame],
    output_path: str,
    format_handling_enum: Any = ExcelFormat,
    write_index: bool = False,
    strings_to_formulas: bool = False,  # see https://github.com/pandas-dev/pandas/issues/29095,
                                        # https://xlsxwriter.readthedocs.io/working_with_pandas.html#passing-xlsxwriter-constructor-options-to-pandas

) -> None:
    """Write out collected data in dataframes grouped per sheet name to
    excel file.

    :param collected_data_for_sheets: the collected dataframes grouped per sheet name.
    :param output_path: output path
    :param format_handling_enum: enum with formatting information, see default value for details
    :param write_index: whether to include the index in the output table; default is False
    :param strings_to_formulas: whether to include formulas as such in the table;
    default is False
    :return: None
    """

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(output_path, engine="xlsxwriter", engine_kwargs={"options": {"strings_to_formulas": strings_to_formulas}})

    for sheet_name, dataframe in collected_data_for_sheets.items():
        # Convert the dataframe to an XlsxWriter Excel object.
        dataframe.to_excel(writer, sheet_name=sheet_name, index=write_index)
        format_excel_sheet_content(dataframe,
                                   writer,
                                   sheet_name,
                                   format_handling_enum,
                                   write_index)

    writer.close()


def format_excel_sheet_content(
    dataframe: pd.DataFrame,
    writer,
    sheet_name: str,
    format_handling_enum: Any,
    write_index: bool):

    # Get the xlsxwriter workbook and worksheet objects.
    worksheet = writer.sheets[sheet_name]
    workbook = writer.book

    # Add a header content.
    header_content_format = workbook.add_format(format_handling_enum.HEADER_FORMAT.value)
    cell_content_format = workbook.add_format(format_handling_enum.CELL_FORMAT.value)

    col_num_shift = 0
    if write_index:
        worksheet.set_column(
            0,
            0,
            format_handling_enum.get_excel_cell_width(str(dataframe.index.name)),
            cell_content_format,
        )
        col_num_shift += 1

    # Write the column headers with the defined content.
    for col_num, name_value in enumerate(zip(dataframe.columns, dataframe.columns.values)):
        col_name, value = name_value
        worksheet.write(0, col_num + col_num_shift, value, header_content_format)
        worksheet.set_column(
            col_num + col_num_shift,
            col_num + col_num_shift,
            format_handling_enum.get_excel_cell_width(str(col_name)),
            cell_content_format,
            )

    # Get the dimensions of the dataframe, and set the autofilter.
    max_row, max_col = dataframe.shape
    if max_row > 0 and max_col > 0:
        worksheet.autofilter(0, 0, max_row, max_col + col_num_shift - 1)

        # Freeze pane on the first x rows and the first y columns
        worksheet.freeze_panes(format_handling_enum.FREEZED_ROWS.value,
                               format_handling_enum.FREEZED_COLUMNS.value+col_num_shift)


def write_text(data: str | List[str], output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        if isinstance(data, str):
            f.write(data)
        elif isinstance(data, List):
            for line in data:
                f.write(line)
                f.write(os.linesep)


def get_file_name_stem(input_path: str) -> str:
    "Get the file name without the file extension."
    return os.path.splitext(os.path.basename(input_path))[0]


def load_python_content(lib_path: str, object_name: str) -> Any:
    # NOTE not always working
    if lib_path.endswith(".py"):
        lib_path = lib_path[:-3]
    if os.path.sep in lib_path:  # os.path.sep on linux: "/"
        lib_path = lib_path.replace(os.path.sep, ".")

    imported_module = importlib.import_module(lib_path)
    object = vars(imported_module)[object_name]
    # print(f"Loading python content '{object_name}' from '{lib_path}'.")
    return object


def is_empty(input_string: str) -> bool:
    input_string = input_string.strip()
    if not input_string:
        return True
    return False


def is_comment(input_string: str, comment_prefix: str) -> bool:
    if input_string.startswith(comment_prefix):
        return True
    return False
