import os ,urllib



files_names=os.listdir('/Users/mac/Desktop/SE- Python/Backend')
print(files_names)


def check_profanity(text_2_check):
    connection = urllib.urlopen('htttp://www.wdly.com/profanity?q='+text_2_check)


for file_name in files_names:
    file_name.translate(None,'0123456789')




#Send messages using Twilio 