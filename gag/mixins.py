


class TranslateMixin:
   def getattr(self, item):
       if item in self.translate_fields:
           return getattr(self, '{}_{}'.format(item ,get_language()))
       return super().__getattr__(item)