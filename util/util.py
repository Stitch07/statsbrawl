from collections import OrderedDict


def sort_dict(obj):
    sorted_dict = sorted(obj.items(), key=lambda kv: kv[1])
    sorted_dict.reverse()
    return OrderedDict(sorted_dict)
