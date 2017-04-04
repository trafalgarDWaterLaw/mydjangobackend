
from rest_framework import serializers
from models  import users,products,product,component

image = serializers.ImageField(max_length=None,use_url=True)
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('user_id', 'created', 'username', 'email_id')

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('product_id', 'created', 'productname', 'category', 'premium', 'user_id', 'user_upload', 'layout', 'image')


class product_id_Serializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('product_id','width','height')

class component_id_Serializers(serializers.ModelSerializer):
    class Meta:
        model = component
        fields = ('product_id','width','height','component_id','position')