import datetime

import common_words


class PasswordCrafter:
    def __init__(self, file_location="/tmp/minirock.txt"):
        self.file_location = file_location
        self.passwords = []

    def years(self):
        current_year = datetime.datetime.now().year
        years = []
        for year in range(current_year - 10, current_year + 1):
            year = str(year)
            years.append(year)
            years.append(year[-2:])
        return years

    def numbers(self):
        numbers = [str(i) for i in range(10)]
        numbers += ["12", "123", "1234", "12345"]
        return numbers

    def special(self):
        return ["!"]

    def conjunctions(self):
        return ["", "_"]

    def craft_passwords(self, prefixes):
        conjunctions = self.conjunctions()
        suffixes = self.years() + self.numbers() + self.special() + [""]
        passwords = []
        for prefix in prefixes:
            for conjunction in conjunctions:
                for suffix in suffixes:
                    passwords.append(prefix + conjunction + suffix)
        self.passwords += passwords

    def seasonal_passwords(self):
        prefixes = common_words.months + common_words.months_short + common_words.seasons
        self.craft_passwords(prefixes)

    def standard_passwords(self):
        prefixes = common_words.common_standard
        self.craft_passwords(prefixes)

    def weak_passwords(self):
        prefixes = common_words.password_permutations + common_words.random_stuff
        self.craft_passwords(prefixes)

    def write_to_file(self):
        with open(self.file_location, "w") as file:
            file.write("\n".join(self.passwords))
