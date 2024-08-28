from browser_functions import WebBrowser
import constants
from ETL import DataETL
from zipfile_functions import ZipFiles



def main():
    browser = WebBrowser()
    browser.download_zip_files(constants.BRAZILIAN_STATES)
    ZipFiles.unzip_files(constants.BRAZILIAN_STATES)
    agregated_table = DataETL.aggregate_reports()
    DataETL.save_report(agregated_table)


if __name__ == "__main__":
   main()
