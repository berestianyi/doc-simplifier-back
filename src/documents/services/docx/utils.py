from datetime import date
from dateutil.relativedelta import relativedelta

class DocxUtils:

    def __init__(self):
        self.month_names = {"01": "січня", "02": "лютого", "03": "березня", "04": "квітня", "05": "травня",
                            "06": "червня", "07": "липня", "08": "серпня", "09": "вересня", "10": "жовтня",
                            "11": "листопада", "12": "грудня"}

    def today_date(self) -> str:
        today = date.today()
        d = today.strftime("%d.%m.%Y")
        return d

    def year_from_today(self) -> str:
        y_from_today = date.today() + relativedelta(years=1)
        d = y_from_today.strftime("%d.%m.%Y")
        return d

    def end_of_year(self) -> str:
        today = date.today()
        d = "31.12." + str(today.year)
        return d

    def date_to_dict(self, doc_date: str) -> dict:
        today_date_list = doc_date.split('.')

        today_date_dict = {"dd": today_date_list[0],
                           "mm": today_date_list[1],
                           "yyyy": today_date_list[2]}

        return today_date_dict

    def date_to_dict_for_replace(self, doc_date: str) -> dict:
        today_date_dict = self.date_to_dict(doc_date)

        dictionary = {"dd": today_date_dict["dd"],
                      "mm": self.month_names[today_date_dict["mm"]],
                      "yyyy": today_date_dict["yyyy"]}

        return dictionary

    def name_split(self, full_name) -> dict:
        full_name = full_name.split()
        slitted_full_name = {
            "first_name": full_name[1],
            "last_name": full_name[0],
            "surname": full_name[2],
            "half_name": full_name[1] + " " + full_name[0],
            "small_name": " " + full_name[0] + " " + full_name[1][0].upper() + "." + full_name[2][0].upper() + "."
        }
        return slitted_full_name

    def document_number(self):
        today = date.today()
        doc_num = today["dd"] + "/" + today["mm"]
