import datetime
import os

# class Logger():
#     # define the file name and structure
#     file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
#
#     # create a non-static method to open and write data
#     @classmethod
#     def write_log_to_file(cls, data: str):
#         with open(cls.file_name, 'a', encoding='utf=8', ) as logger_file:
#             logger_file.write(data)

# @classmethod
# def add_response(cls, url: str, method: str):
#     test_name = os.environ.get('PYTEST_CURRENT_TEST')
#     data_to_add = f"\n-----\n"
#     data_to_add += f"Test: {test_name}\n"
#     data_to_add += f"Time: {str(datetime.datetime.now())}\n"
#     data_to_add += f"Request method: {method}\n"
#     data_to_add += f"Request cURL: {url}\n"
#     data_to_add += "\n"
#
#     cls.write_log_to_file(data_to_add)
file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"


def write_log_to_file(cls, data):
    with open(cls.file_name, 'a', encoding='utf=8', ) as logger_file:
        logger_file.write(data)


def add_response(cls, url):
    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    data_to_add = f"\n-----\n"
    data_to_add += f"Test: {test_name}\n"
    # data_to_add += f"Time: {str(datetime.datetime.now())}\n"
    # data_to_add += f"Request method: {method}\n"
    data_to_add += f"Request cURL: {url}\n"
    data_to_add += "\n"

    cls.write_log_to_file(data_to_add)
