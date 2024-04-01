from motor.motor_asyncio import AsyncIOMotorClient

from miko.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

from miko.core.database.expired import *
from miko.core.database.notes import *
from miko.core.database.premium import *
from miko.core.database.reseller import *
from miko.core.database.saved import *
from miko.core.database.userbot import *
from miko.core.database.pref import *
from miko.core.database.otp import *
from miko.core.database.gbans import *
from miko.core.database.variabel import *
