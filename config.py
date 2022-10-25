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
    ADMIN = os.environ.get("ADMINS", "1316963576")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 14218096))
    CHAT = int(os.environ.get("CHAT", "-1001792395780"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001792395780")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://sayajifm.radioca.st/stream?listening-from-radio-garden=1639494716")
    API_HASH = os.environ.get("API_HASH", "5b1a66b2baa1521d7cb880e4d33fd483")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5491007768:AAFoe4TUfVDgvYegEAEK6mMKoDtyvMzCN9g") 
    SESSION = os.environ.get("SESSION_STRING", "BQCDQRUkj4dkDuiTQSjI0Jdifk2wxO_7IKwHXZWvYoC2OnwtBhKXsKjXnkehO-qk-Qw4kwemIseH3ZVzjkHgqBl70iS4VyxCrdjL9e1VVq13nVqCAk30-6CsFy33O8OvTGgQTO1c8hBxX_V7WIkgSuEipaN-xIAIUuLYP7HAB77Az39M7C1bWwAloYTEaLFkcChstc0DsGPWsoNEPEtRjTg26_1wZsj2jrkWy7A7MseuLLzrjhfuUJujDLq0L4n2tneWVKF6D3PPWicOFGuteje0_UD-MN-6YsO4Hr60qx3UKnA-gJEy1LYydCuGSBqUqz90OY_s4ttMN5go5YZyQSjGAAAAAU1PCJ8A")

