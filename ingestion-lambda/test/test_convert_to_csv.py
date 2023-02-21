from src.convert_to_csv import convert_to_csv
from test_data.mock_ingested_data_function_output import mock_data, mock_data2
import os
import shutil
import csv

# file_path = "/tmp"

def reset_folder():
    if os.path.exists("src/csv_files"):
        shutil.rmtree("src/csv_files")
    os.mkdir('src/csv_files')

def test_writes_a_csv_file():
    reset_folder()
        
    convert_to_csv(mock_data)

    assert os.path.exists("./src/csv_files/payment.csv") == True


def test_writes_csv_files_():
    reset_folder()

    convert_to_csv(mock_data)

    assert os.path.exists("./src/csv_files/payment.csv") == True
    assert os.path.exists("./src/csv_files/transaction.csv") == True
    assert os.path.exists("./src/csv_files/sales_order.csv") == True


def test_doesnt_save_empty_files():
    reset_folder()

    convert_to_csv(mock_data)

    assert os.path.exists("./src/csv_files/design.csv") == False
    assert os.path.exists("./src/csv_files/staff.csv") == False


def test_column_names_exist():
    reset_folder()

    convert_to_csv(mock_data2)

    with open("src/csv_files/payment.csv", "r") as file:
        reader = csv.reader(file)
        row1 = next(reader)
        assert "payment_id" in row1
        assert "last_updated" in row1
