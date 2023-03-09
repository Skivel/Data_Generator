from django.db import models


# class CreateSchema(models.Model):
#     COMMA = ','
#     SEMICOLON = ';'
#     DOUBLE_QUOTE = '"'
#     QUOTE = "'"
#
#     SEPARATORS = [
#         (COMMA, 'Comma (,)'),
#         (SEMICOLON, 'Semicolon (;)'),
#     ]
#
#     STRING_CHARACTER = [
#         (DOUBLE_QUOTE, 'Double-quote (")'),
#         (QUOTE, "Quote (')")
#     ]
#
#     author = models.CharField(max_length=255, verbose_name='Schema author', blank=True)
#     name = models.CharField(max_length=255, verbose_name='Schema name', blank=True)
#     separator = models.CharField(max_length=1, choices=SEPARATORS, default=COMMA, verbose_name='Separators', blank=True)
#     string_character = models.CharField(max_length=1, choices=STRING_CHARACTER, default=DOUBLE_QUOTE, verbose_name='String character', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
#
# class ConcreteModel(CreateSchema):
#     COMMA = ','
#     SEMICOLON = ';'
#     DOUBLE_QUOTE = '"'
#     QUOTE = "'"
#
#     SEPARATORS = [
#         (COMMA, 'Comma (,)'),
#         (SEMICOLON, 'Semicolon (;)'),
#     ]
#
#     STRING_CHARACTER = [
#         (DOUBLE_QUOTE, 'Double-quote (")'),
#         (QUOTE, "Quote (')")
#     ]
#
#     author = models.CharField(max_length=255, verbose_name='Schema author', blank=True)
#     name = models.CharField(max_length=255, verbose_name='Schema name', blank=True)
#     separator = models.CharField(max_length=1, choices=SEPARATORS, default=COMMA, verbose_name='Separators', blank=True)
#     string_character = models.CharField(max_length=1, choices=STRING_CHARACTER, default=DOUBLE_QUOTE, verbose_name='String character', blank=True)
#
#     class Meta:
#         verbose_name = 'Concrete Model'
#         verbose_name_plural = 'Concrete Models'
#
#
# MyModel = ConcreteModel()
