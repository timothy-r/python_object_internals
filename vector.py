class Vector:
    
    """
        accept arbitrary coordinate names (keys)
    """
    def __init__(self, **coords) -> None:
        # add a leading underscore to each key name
        private_coords = {'_'+k: v for k, v in coords.items()}
         
        self.__dict__.update(private_coords)
    
    def __getattr__(self, name):
        private_name = '_' + name
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                self.__class__.__name__,
                name
            ))
    
    def __setattr__(self, name: str, value) -> None:
        raise AttributeError("Cannot set attribute {!r}".format(name))
    
    def __repr__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                    # strip out the added underscores
                    k=k[1:],
                    v=self.__dict__[k])
                    for k in sorted(self.__dict__.keys())
            )
        )