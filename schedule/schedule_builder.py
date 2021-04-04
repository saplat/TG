from openpyxl.worksheet.worksheet import Worksheet

from parsers.parser import ScheduleParser
from schedule.document_settings import StructParse
from schedule.group_schedule import GroupInfo


class ScheduleBuilder:

    def __init__(self, worksheet: Worksheet):
        self.parser: ScheduleParser = ScheduleParser(worksheet)

    def build(self):
        group_schedule_list: list[GroupInfo] = []
        data_prapare_list = self.__prepare_data()
        return []

    def __prepare_data(self):
        header_parse_list = self.parser.parse_header()
        data_prepare_list = []
        elem_split_list = []
        for it in header_parse_list:
            elem_split_list.append(it)
            if it[1] is StructParse.NumberClass:
                data_prepare_list.append(elem_split_list[:])
                elem_split_list = []


        temp = data_prepare_list[0]
        for it in data_prepare_list:
            if len(it) > 2:
                temp = it
            else:
                it.extend(temp[:2])
                it.sort(key=lambda x: x[1])
        return data_prepare_list