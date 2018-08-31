# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-31 10:11:35
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-31 10:11:54

from functools import wraps


# decorator (no impact on help() function)
def valida(func):
    @wraps(func)
    def handle_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            descr = 'ERROR in "%s": %s' % (func.__name__, str(e))
            print(descr)
    return handle_error
