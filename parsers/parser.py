from openpyxl.worksheet.worksheet import Worksheet

from schedule.document_settings import START_PARSE_COL, HEADER_ROW, TIME_SPLIT_DATA, CLASS_SPLIT_DATA,DAY_SPLIT_DATA, StructParse


class ScheduleParser:

    def __init__(self, worksheet: Worksheet):
        self.worksheet = worksheet


    def parse_header(self):
        data = 0
        it_col = START_PARSE_COL
        header_parse_list = []
        while data is not None:
            data = self.worksheet.cell(row=HEADER_ROW, column=it.col).value
            if data is not None:
                data = data.replace(' ','')
                if data == DAY_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.Day))
                elif data == TIME_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.Time))
                elif data == CLASS_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.NumberClass))
                else:
                    header_parse_list.append((it_col, StructParse.GroupName))
                it_col += 1
        return header_parse_list