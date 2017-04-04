
from rest_framework import serializers
from models  import users,products

image = serializers.ImageField(max_length=None,use_url=True)
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('user_id', 'created', 'username', 'email_id')

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('product_id', 'created', 'productname', 'category', 'premium', 'user_id', 'user_upload', 'layout', 'image')