"""
Dear Kangers Stay Away
"""

from helpers.SQL import dbb

Rbun = dbb["RBAN"]


async def rlisa(user, reason="#MATHERCHOD"):
    await Rbun.insert_one({"user": user, "reason": reason})


async def runlisa(user):
    await Rbun.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in Rbun.find({})]


async def lisaub_info(user):
    kk = await Rbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
