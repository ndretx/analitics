# Excel Data Reader

This project is designed to read and process data from Excel files containing forms filled out by third parties. It provides a simple interface to extract relevant information from these forms for further analysis.

## Project Structure

```
excel-data-reader
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── excel_reader.py  # Contains the ExcelReader class for reading Excel files
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

This will initialize the program and start processing the Excel files.

## Dependencies

The project requires the following Python packages:

- pandas
- openpyxl

Make sure these are included in your `requirements.txt` file.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.