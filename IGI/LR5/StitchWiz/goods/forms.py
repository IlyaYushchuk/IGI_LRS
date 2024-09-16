import logging
from django import forms 

from goods.models import Order
from users.models import Master
from main_page.models import Coupon
from datetime import timezone
from django.utils import timezone
import datetime
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['master', 'date_release', 'coupon_code', 'comments']    
    
    def valid_pickup_date(date):
        if date < timezone.now().date():
            raise forms.ValidationError("The pickup date cannot be in the past.")
        return date
    
    def valid_coupon(code):
        logger = logging.getLogger('django')
        logger.info('Inside valid_coupon')
        try:
            coupon = Coupon.objects.get(code=code)
            if coupon.date < timezone.now().date():
                raise forms.ValidationError("This coupon already expired")
        except Coupon.DoesNotExist:
            raise forms.ValidationError("There are no coupon with such code")
          
    def save(self, commit=True):
        order = super().save(commit=False)
        code = self.cleaned_data.get('coupon_code')
        if code:
            order.coupon = Coupon.objects.get(code=code)
        if commit:
            order.save()
        return order       
        

    comments = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'placeholder': 'Leave a comment...'}),
        label='Comment'
    )
    master = forms.ModelChoiceField(
        queryset=Master.objects.all(),
        widget=forms.Select(),
        label='Choose a master'
    )
    coupon_code = forms.CharField(
        required=False, 
        max_length=50, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your coupon code'}),
        validators=[valid_coupon],
        label='Coupon',
    )
    date_release = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[valid_pickup_date],
        label='Pickup Date',
    )

    def __init__(self, *args, **kwargs):
        masters = kwargs.pop('masters', None)
        super().__init__(*args, **kwargs)
        if masters is not None:
            self.fields['master'].queryset = masters

 
    

    