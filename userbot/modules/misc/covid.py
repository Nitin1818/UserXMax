from datetime import datetime
from covid import Covid
from ..help import add_help_item
from userbot.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"**Confirmed**   : `{country_data['confirmed']}`\n"
        output_text += f"**Active**      : `{country_data['active']}`\n"
        output_text += f"**Deaths**      : `{country_data['deaths']}`\n"
        output_text += f"**Recovered**   : `{country_data['recovered']}`\n"
        output_text += (
            "**Last update** : "
            f"`{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%Y-%m-%d %H:%M:%S')}`\n"
        )
        output_text += f"__Data provided by__ [Johns Hopkins University](https://j.mp/2xf6oxF)"
    else:
        output_text = "No information yet about this country!"
    await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")


add_help_item(
    "covid",
    "Misc",
    "Get an information about data covid-19 in your country.",
    """
.covid [Country Name]
    """
)
