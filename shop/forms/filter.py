from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from shop.models import Animal, Brand

MIN_PRICE = 0
MAX_PRICE = 10000

MIN_WEIGHT = 1
MAX_WEIGHT = 15


class RangeField(forms.Field):
    def __init__(self, *, min_value, max_value, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(**kwargs)

    def to_python(self, value):
        if not value:
            return

        from_value, to_value = tuple(map(float, value.split(';')))
        self.widget.attrs.update({'data-from': from_value, 'data-to': to_value})
        return from_value, to_value

    def validate(self, value):
        if not value:
            return

        super().validate(value)
        from_value, to_value = value
        if from_value > to_value:
            raise ValidationError('FROM value bigger than TO value')

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        if isinstance(widget, TextInput):
            attrs['data-type'] = 'double'
            if self.min_value is not None:
                attrs["data-min"] = self.min_value
            if self.max_value is not None:
                attrs["data-max"] = self.max_value
                attrs["data-from"] = 0
                attrs["data-to"] = self.max_value
        return attrs


class FilterForm(forms.Form):
    __category_choices = ((animal.id, animal.title) for animal in Animal.objects.all())
    __brand_choices = ((brand.id, brand.title) for brand in Brand.objects.all())

    price_range = RangeField(min_value=MIN_PRICE,
                             max_value=MAX_PRICE,
                             required=False,
                             widget=forms.TextInput(attrs={
                                 'class': 'js-range-slider',
                                 'id': 'priceSlider',
                             }))

    weight_range = RangeField(min_value=MIN_WEIGHT,
                              max_value=MAX_WEIGHT,
                              required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'js-range-slider',
                                  'id': 'weightSlider',
                              }))

    category = forms.TypedMultipleChoiceField(required=False,
                                              choices=__category_choices,
                                              coerce=int,
                                              widget=forms.CheckboxSelectMultiple())

    has_discount = forms.BooleanField(required=False)

    brand = forms.TypedMultipleChoiceField(required=False,
                                           choices=__brand_choices,
                                           coerce=int,
                                           widget=forms.CheckboxSelectMultiple())
