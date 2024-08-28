import zipfile
import os
import constants



class ZipFiles:

    download_folder = f'C:\\Users\\{os.getlogin()}\\Downloads'
    result_directory = f'{os.getcwd()}\\technical_challenge_solution\\ExcelFiles'
    zip_file_directory = f'{os.getcwd()}\\technical_challenge_solution\\ZipFiles'

    def __creating_result_folder__():
        try:
            os.makedirs(ZipFiles.result_directory)
        except:
            pass

    def __creating_zip_folder__():
        try:
            os.makedirs(ZipFiles.zip_file_directory)
        except Exception as e:
            pass

    def __moving_downloaded_files__(BRAZILIAN_STATES):
        for state in BRAZILIAN_STATES:
            try:
                os.rename(f'C:\\Users\\{os.getlogin()}\\Downloads\\{state}',
                        f'{os.getcwd()}\\technical_challenge_solution\\ZipFiles\\{state}')
            except:
                pass

    @staticmethod
    def unzip_files(BRAZILIAN_STATES):
        ZipFiles.__creating_result_folder__()
        ZipFiles.__creating_zip_folder__()
        ZipFiles.__moving_downloaded_files__(BRAZILIAN_STATES)
        for state in BRAZILIAN_STATES:
            zip_file_path = f'{ZipFiles.zip_file_directory}\\{state}'
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all the contents of the zip file
                try:
                    zip_ref.extractall(ZipFiles.result_directory)
                except:
                    pass
    