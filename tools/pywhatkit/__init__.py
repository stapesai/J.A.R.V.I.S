from platform import system

from pywhatkit.ascii_art import image_to_ascii_art
from pywhatkit.handwriting import text_to_handwriting
from pywhatkit.mail import send_hmail, send_mail
from pywhatkit.misc import info, playonyt, search, show_history, web_screenshot
from pywhatkit.sc import cancel_shutdown, shutdown
from pywhatkit.whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendwhats_image,
)

if system().lower() in ("darwin", "windows"):
    from pywhatkit.misc import take_screenshot

if system().lower() == "windows":
    from pywhatkit.remotekit import start_server
