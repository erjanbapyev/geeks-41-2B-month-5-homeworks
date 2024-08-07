from django.urls import path
from .views import (
    CategoryList, CategoryDetail, ProductList, ProductDetail,
    ReviewList, ReviewDetail, ProductWithReviewsList
)

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/reviews/', ProductWithReviewsList.as_view(), name='product-with-reviews-list'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
