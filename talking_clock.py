from time import strftime
import time
from gtts import gTTS
import vlc
import os

# Get Time from time module and convert h, m and s to integers using map function
hour, min, sec = map(int, strftime('%H / %M / %S').split(' / '))


ZERO_TO_NINE = ["Oh", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
ELEVEN_TO_NINETEEN = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] # Should never use sixty and over
TIME_OF_DAY = ["AM", "PM"]


def to_words(number, is_hour=False, is_minute=False, is_second=False):
    words = ''
    tens = number // 10
    singles = number % 10

    if number == 0:
        return words

    if number % 10 == 0:
        words += TENS[tens - 1]
        return words
    if tens == 1:
        words += ELEVEN_TO_NINETEEN[singles - 1]
        return words

    if tens == 0 and is_minute:
        # Add "Oh"
        words += ZERO_TO_NINE[tens] + ' '

    if tens >= 2:
        # Add tens to word
        words += TENS[tens-1] + ' '
    # Add singles to word
    words += ZERO_TO_NINE[singles]

    return words

time_of_day = TIME_OF_DAY[0]
if hour >= 12:
    if hour != 12:
        hour = hour % 12
    time_of_day = TIME_OF_DAY[1]

hStr = to_words(hour, is_hour=True)
mStr = to_words(min, is_minute=True)
sStr = to_words(sec, is_second=True)

# print(hour, " == ", hStr)
# print(min, " == ", mStr)
# print(sec, " == ", sStr)

# The final text
text = "It Is Now: " + hStr + ' ' + mStr + ' ' + time_of_day + ' and ' + sStr + ' Seconds.'

# Manual text
# text = "sea"

# Printing it
print(text)

# Saving it as a .mp3 file
file_path = "C:\\test.mp3"
# First make sure there are no files with that name already
try:
    os.remove(file_path)
except OSError:
    pass
tts = gTTS(text=text, lang='en')
tts.save(file_path)

# Playing the file
vlc_instance = vlc.Instance()
vlc_player = vlc_instance.media_player_new()
media = vlc_instance.media_new(file_path)
vlc_player.set_media(media)
vlc_player.play()

while True:
    pass

# time.sleep(5)

