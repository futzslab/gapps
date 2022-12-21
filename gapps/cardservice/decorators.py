import types


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def appscript(*args, **kwargs):

    def wrapper(cls, **kwargs1):

        if not hasattr(cls, '__annotations__'):
            return cls

        # if cls.__name__ == 'SelectionInput':
        #     import ipdb; ipdb.set_trace()

        for key, t_value in cls.__annotations__.items():

            def create_function(cls_key):
                def _run(self, val):
                    setattr(self, cls_key, val)
                    return self
                return _run

            def create_add_function(cls_key):
                def _run_add(self, *val):
                    attr = getattr(self, cls_key)
                    attr = attr or []
                    attr.append(*val) if len(val) == 1 else attr.append(val)
                    setattr(self, cls_key, attr)
                    return self
                return _run_add

            if t_value is list:
                setattr(cls, to_camel_case(f"add_{key}"),
                        create_add_function(key))
            elif isinstance(t_value,
                            types.GenericAlias) and t_value.__origin__ is list:
                setattr(cls, to_camel_case(f"add_{key}"),
                        create_add_function(key))
            else:
                setattr(cls, to_camel_case(f"set_{key}"), create_function(key))
        return cls

    return wrapper(args[0])
