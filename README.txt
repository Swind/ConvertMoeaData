MOEA Data Conversion and Query Tool
===================================

Description:
-------------
This tool is designed to convert Excel files containing information about illegal factories from the website:
https://www.cto.moea.gov.tw/FactoryMCLA/web/information/list.php?cid=1
to a JSON format which is easier to parse and use for further analysis. It also converts Chinese section names to section numbers for easier querying.

Usage:
------
python moea_data.py <sub_command> -y <year>

Subcommands:
------------
1. convert:
   Convert an Excel file corresponding to the specified ROC year to JSON format.
   Example:
   python moea_data.py convert -y 112

2. query-factory-id:
   Query factory IDs from the JSON file corresponding to the specified ROC year.
   Example:
   python moea_data.py query-factory-id -y 112

Options:
--------
-y, --year:
   Specify the year in ROC (Republic of China) format. This option is required.

Directory Structure:
--------------------
Place your Excel files in the `xlsx` directory.
Converted JSON files will be saved in the `json` directory.

Example:
--------
1. To convert the Excel file for the year 112 to JSON format:
   python moea_data.py convert -y 112

2. To query factory IDs from the JSON file for the year 112:
   python moea_data.py query-factory-id -y 112

Functionality:
--------------
1. Convert Excel to JSON:
   This tool reads Excel files downloaded from the specified MOEA website and converts them into JSON format for easier parsing and usage.
   Example Excel file name: 112.xlsx
   Example JSON file name: 112.json

2. Convert Chinese Section Names to Section Numbers:
   During the conversion process, Chinese section names are converted to section numbers to facilitate easier querying in the JSON format.

Excel File Content Example:
---------------------------
Here is an example of the content in the Excel file:

ID          編號    市縣    地號                   使用分區        使用地      市縣政府查處情形
112010001   1       新北市  樹林區東園段1130地號   一般農業區      農牧用地    裁處罰鍰    已停止供水供電
112010002   2       新北市  樹林區西園段681地號    一般農業區      農牧用地    裁處罰鍰    已停止供水供電

JSON File Content Example:
--------------------------
Here is an example of the converted JSON format:

```json
{
    "id": "112010240",
    "year": "112",
    "month": "01",
    "number": "255",
    "city": "彰化縣",
    "Sectname": "和美鎮大榮段869地號",
    "sectcode": "0248",
    "land_numbers": [
        "08690000"
    ],
    "usage_zone": "特定農業區",
    "Use": "農牧用地",
    "status": [
        "依工廠管理輔導法規定核准納管"
    ],
    "factory_id": "a2a8f133-9c17-4e7f-a148-0d8756f412c3"
}
```

Note:

Make sure to place the Excel files named as ‘.xlsx’ in the xlsx directory.
The converted JSON files will be saved in the json directory with the name ‘.json’.

Dependencies:

This tool requires Python and the following Python packages:

	•	argparse
	•	os
	•	converter (custom module)
	•	query (custom module)
	•	pandas (external package for reading Excel files)

Ensure that the converter and query modules are in the same directory as the moea_data.py script.
