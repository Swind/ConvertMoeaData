import argparse
import os

import converter
import query

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def convert_xlsx_to_json(year: str):
    sheet_name_list = []
    for i in range(1, 13):
        sheet_name_list.append(f"{year}{i:02d}")

    xlsx_file_name = f"{year}.xlsx"
    xlsx_file_path = os.path.join(SCRIPT_DIR, "xlsx", xlsx_file_name)

    json_file_name = f"{year}.json"
    json_file_path = os.path.join(SCRIPT_DIR, "json", json_file_name)

    parser = converter.Parser()
    xlsx = converter.open_xlsx(xlsx_file_path, sheet_name_list)
    parser.parse_all_sheets(xlsx)
    parser.save(json_file_path)


def main():
    parser = argparse.ArgumentParser(description="Convert Excel files to JSON format.")
    parser.add_argument(
        "sub_command",
        help="Subcommand to execute",
        choices=["convert", "query-factory-id"],
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        required=True,
        help="Specify the year in ROC (Republic of China) format to convert the corresponding Excel file.",
    )

    args = parser.parse_args()

    if args.sub_command == "convert":
        convert_xlsx_to_json(args.year)
    elif args.sub_command == "query-factory-id":
        json_file_name = f"{args.year}.json"
        json_file_path = os.path.join(SCRIPT_DIR, "json", json_file_name)
        query.query_factory_id(json_file_path)


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     parser = converter.Parser()
#     xlsx = converter.open_xlsx("112.xlsx", sheet_name_list)
#     parser.parse_all_sheets(xlsx)
#     parser.save("112.json")

# if __name__ == "__main__":
# converter = SectCodeConverter()
# address = "竹北市三崁店段三崁店小段120-6地號"
# address = "烏日區北里段277地號"
# converter.convert(address)
