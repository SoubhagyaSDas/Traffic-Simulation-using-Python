class Conversions:
    @staticmethod
    def wc_point_to_cc_point(val):
        from Constants import Constants  # Assuming Constants is defined in the constants.py file
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def wc_length_to_cc_length(val):
        from Constants import Constants  # Assuming Constants is defined in the constants.py file
        return int(val * (Constants.CharMapSize / Constants.WorldSize))