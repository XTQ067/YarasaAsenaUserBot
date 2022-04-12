from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.events import register

from userbot.language import get_value
LANG = get_value("__yarasa")

@register(outgoing=True, pattern="^.yarasa(?: |$)(.*)")
@register(outgoing=True, pattern="^.bat(?: |$)(.*)")
async def yarasa(event):
    """ Dilvuran Vüqar. """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]
        
        for i in sayfa:
            string += f'`✨ `'
            for sira, a in enumerate(i):
                string += "__" + str(a)
                if sira == i.index(i[-1]):
                    string += "__"
                else:
                    string += "__, "
            string += "\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)
