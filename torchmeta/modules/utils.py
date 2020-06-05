import re
from collections import OrderedDict

def get_subdict(dictionary, key=None):
    if dictionary is None or not dictionary:
        return None

    if (key is None) or (key == ''):
        return dictionary

    key_re = re.compile(r'^{0}\.(.+)'.format(re.escape(key)))
    # Compatibility with DataParallel
    if not any(filter(key_re.match, dictionary.keys())):
        key_re = re.compile(r'^module\.{0}\.(.+)'.format(re.escape(key)))

    return_dict = OrderedDict((key_re.sub(r'\1', k), value) for (k, value)
        in dictionary.items() if key_re.match(k) is not None)
    # TODO: I am not sure this is proper behavior - it is likely that the meta learning isn't working because of this
    return return_dict if return_dict else None
