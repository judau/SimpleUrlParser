import urllib.parse
import json


def proc_parse(input_value) -> dict:
    res = {}
    if "?" not in input_value:
        # really need `unquote` ? 🤔
        return {input_value: {"No Query Params": {"unquote": urllib.parse.unquote(input_value)}}}
    (url, appendix) = input_value.split("?")
    apd = {}
    apd_list = appendix.split("&")
    for item in apd_list:
        (a_key, a_val) = item.split("=")
        a_val = urllib.parse.unquote(a_val)
        if "?" in a_val:
            apd[a_key] = proc_parse(a_val)
        else:
            apd[a_key] = a_val
    res[url] = apd
    return res


def main_task():
    res = proc_parse(input())
    res_json = json.dumps(res, indent=4)
    print(res_json)


main_task()
