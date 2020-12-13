from rest_framework import serializers
from .models import PaymentDetails
import re
import _datetime

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

    def validate_CreditCardNumber(self, value):
        value1, value2 = False, False
        pattern1 = r"(\d{4})(-?)(\d{4})(\2\d{4}){2}"
        pattern2 = r"((\d)(?!\2{3})){16}"
        if re.match( pattern1, value):
          print("value1 is true")
          value1 = True
        value = value.replace("-", "")
        if re.match(pattern2, value):
          print("value2 is true")
          value2 = True
       
        if value1 == True and value2 == True:
          return value
        else:
          raise serializers.ValidationError("Invalid card Number")

    def validate_ExpirationDate(self, value):
      if value < _datetime.date.today():
        raise serializers.ValidationError("ExpirationDate cannnot be past date")
      else:
        return value