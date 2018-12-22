class PySingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PySingleton, cls).__new__(cls)
        return cls.instance


s1 = PySingleton()
s2 = PySingleton()
print('%s == %s' % (s1, s2))

sa1 = PySingleton()
sa2 = PySingleton()
print('%s == %s' % (sa1, sa2))
