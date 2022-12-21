"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "436757497")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "15832480"))
    CHAT = int(os.environ.get("CHAT", "-1001792395780"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001792395780")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://sayajifm.radioca.st/stream?listening-from-radio-garden=1639494716")
    API_HASH = os.environ.get("API_HASH", "892a7eac73500e41c4f3fd092dfead65")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5827214852:AAGXNgNOwJDthuYB8MowHZyD1R3C7wZa94g") 
    SESSION = os.environ.get("SESSION_STRING", "BQCV90OS-QyZW2RPCteU1AbxMBgvUmDIBhch-CTC1ni-7cr0rZbs2Xw4ZgEP1XgzUEbG9PlHLpdgmqdluMhZM1dZ2JTx0DVj_F74PCWvaC5Uk6H6skv9aTXBAInfyY39uUt1dkjBzyoN0Q4PGb3zuf1fNmYq3wYryIuxmmZVA3s0smWULFSlfizw0ANCNHNXs4rYpp-5A3VDpUNyZNoNAK2UGqGskvJkJxBTWUkcH6BFmYoHAHQpLIQhg3Ernl-UFeZ9LKTDQumwUKbyvwGQxqToUcfHMbl8kPWu8caePlhDtx6lzToxTwyH8R-K9TvSkLLBoSqWo7UjOENwIcydBkPUAAAAAH6SkvAA")

