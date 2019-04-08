def dict_merge(a, b):
    """merges b into a and return merged result

    NOTE: tuples and arbitrary objects are not handled as it is totally ambiguous what should happen"""
    key = None
    # ## debug output
    # sys.stderr.write("DEBUG: %s to %s\n" %(b,a))
    try:
        if a is None or isinstance(a, str) or isinstance(a, unicode) or isinstance(a, int) or isinstance(a, long) or isinstance(a, float):
            # border case for first run or if a is a primitive
            a = b
        elif isinstance(a, list):
            # lists can be only appended
            if isinstance(b, list):
                # merge lists
                a.extend(b)
            else:
                # append to list
                a.append(b)
        elif isinstance(a, dict):
            # dicts must be merged
            if isinstance(b, dict):
                for key in b:
                    if key in a:
                        a[key] = dict_merge(a[key], b[key])
                    else:
                        a[key] = b[key]
            elif isinstance(b, list):
                for item in b:
                    for key in a:
                        if key in item:
                            item[key] = dict_merge(item[key], a[key])
                        else:
                            item[key] = a[key]
                a = b
            else:
                raise Exception('Cannot merge non-dict "%s" into dict "%s"' % (b, a))
        else:
            raise Exception('NOT IMPLEMENTED "%s" into "%s"' % (b, a))
    except TypeError, e:
        raise Exception('TypeError "%s" in key "%s" when merging "%s" into "%s"' % (e, key, b, a))
    return a


context = {'delete': True, 'provider': 'amazon', 'glue_cli': {'capacity' :2, 'timeout': 100, 'connection':''}}
exec_prof = {'delete': False, 'glue_cli':{ 'capacity':10}}
new_a = dict_merge(context,exec_prof)
print new_a