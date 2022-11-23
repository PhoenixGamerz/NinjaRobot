from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~ filters.edited & ~filters.via_bot & ~ filter.forwaded
