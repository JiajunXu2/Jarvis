from plugin import plugin, alias
from datetime import datetime


@alias("endofyear")
@plugin("endofyear timer")
class EndOfYearTimer:
    def __call__(self, jarvis, s):
        self.jarvis = jarvis
        self.main()

    def main(self):
        actual_datetime = datetime.now()
        end_of_year = datetime(actual_datetime.year, 12, 31, 23, 59, 59)

        time_till_end = end_of_year - actual_datetime

        self.jarvis.say(f"It\'s {self.format_time_delta(time_till_end)}" +
            " until the end of the year")

    def format_time_delta(self, t) -> str:
        remaining_secs = t.seconds % 3600
        time_dict = {
            'days' : t.days,
            'hours' : int(t.seconds / 3600),
            'minutes' : int(remaining_secs / 60),
            'seconds' : remaining_secs % 60
        }

        new_timedict = {}
        for element in time_dict:
            if time_dict[element] == 1:
                new_timedict[element[0:len(element)-1]] = time_dict[element]
            else:
                new_timedict[element] = time_dict[element]

        # store keys and values in a list
        # for easier access
        days = list(new_timedict.keys())
        values = list(new_timedict.values())
        
        timedelta = ''
        for i in range(len(values)):
            timedelta += f'{values[i]} {days[i]}, '

        # ignore the last 2 characters ', '
        return timedelta[:-2]