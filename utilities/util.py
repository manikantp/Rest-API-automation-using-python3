import utilities.custom_logger as cl

class Util(object):
    log = cl.customLogger()

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text from API response --> :: {}".format(actualText))
        self.log.info("Expected text from API response --> :: {}".format(expectedText))
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHES !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyNumbersMatch(self, actualNumber, expectedNumber):
        self.log.info("Actual number from API response --> :: {}".format(actualNumber))
        self.log.info("Expected number from API response --> :: {}".format(expectedNumber))
        if actualNumber == expectedNumber:
            self.log.info("### VERIFICATION MATCHES !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False
