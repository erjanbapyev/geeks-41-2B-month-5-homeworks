from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 1)
        return None

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description is required.")
        return value

    def validate_price(self, value):
        if value is None:
            raise serializers.ValidationError("Price is required.")
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_category(self, value):
        if value is None:
            raise serializers.ValidationError("Category is required.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Text is required.")
        if len(value) < 10:
            raise serializers.ValidationError("Text must be at least 10 characters long.")
        return value

    def validate_stars(self, value):
        if value is None:
            raise serializers.ValidationError("Stars rating is required.")
        if value < 1 or value > 5:
            raise serializers.ValidationError("Stars rating must be between 1 and 5.")
        return value

    def validate_product(self, value):
        if value is None:
            raise serializers.ValidationError("Product is required.")
        return value
