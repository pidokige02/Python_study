class Casting:
    def to_int(ns):
        if type(ns) == str:
            return int(ns.strip())
        else:
            return ns
