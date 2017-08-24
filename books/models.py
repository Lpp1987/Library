from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_('First name'), max_length=255)
    last_name = models.CharField(_('Last name'), max_length=255)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


def isbn_validator(isbn):
    control = int(isbn[-1])
    i = 1
    isbn_list = []

    if isbn.isdigit():
        if len(isbn) == 13:
            for char in isbn[:-1]:
                if i % 2 == 0:
                    isbn_list.append(int(char))
                else:
                    isbn_list.append((int(char)*3))
                i += 1
            if control != (((10 - sum(isbn_list)) % 10) % 10):
                raise ValidationError(_('ISBN is not valid'), code='not_valid')
        elif len(isbn) == 10:
            for char in isbn[:-1]:
                isbn_list.append((int(char) * i))
                i += 1
            if control != (sum(isbn_list) % 11):
                raise ValidationError(_('ISBN is not valid'), code='not_valid')
        elif len(isbn) < 10:
            raise ValidationError(_('ISBN is too short'), code='too_short')
        elif len(isbn) > 13:
            raise ValidationError(_('ISBN is too long'), code='too_long')
        elif 10 < len(isbn) < 13:
            raise ValidationError(_('ISBN must contain 10 or 13 digits'), code='10_or_13')
    else:
        raise ValidationError(_('ISBN contains only digits'), code='illegal_characters')


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    author = models.ManyToManyField(
        Author,
        related_name='author',
        verbose_name=_('Author'),
    )
    isbn = models.CharField(
        _('ISBN'),
        unique=True,
        max_length=13,
        validators=[isbn_validator],
        null=True,
        blank=True,
        help_text=_('10 or 13 digits')
    )
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    cover = models.ImageField(_('Cover'), upload_to='books/covers', null=True, blank=True)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        authors = Author.objects.filter(author=self.pk)
        authors_clean = ''

        for author in authors:
            authors_clean += str(author.last_name) + ', ' + str(author.first_name) + ', '
        authors_clean = authors_clean[:-2]

        if self.cover:
            cover = _('cover available')
        else:
            cover = _('cover unavailable')

        return '{} - {} - {}'.format(self.title, authors_clean, cover)


