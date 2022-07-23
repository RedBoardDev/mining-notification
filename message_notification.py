import bitly_api
from get_data import set_var_dotenv

def shorten_link(long_link:str) -> str:
    bitly = bitly_api.Connection(access_token = set_var_dotenv("API_KEY_BITLY"))
    link:str = bitly.shorten(long_link)['url']
    return (link)

def set_status_block(status_block:str):
    if (status_block == 'uncle'):
        return "Status: Uncle"
    elif (status_block == 'orphaned'):
        return "Status: Orphan"
    else:
        return "Status: Good"

def get_effort(last_block) -> str:
    try:
        return ((str)(round(last_block['effort'], 2)))
    except:
        return ("-")

def get_infoLink(last_block) -> str:
    try:
        link = last_block['infoLink']
    except:
        return ("-")
    return(shorten_link(link))

def set_global_message(last_block) -> str:
    status_stats:str = set_status_block(last_block['status'])
    luck_stats:str = "Luck: " + get_effort(last_block) + "%"
    global_stats:str = status_stats + '\n' + luck_stats + '\n' + get_infoLink(last_block)
    return (global_stats)
