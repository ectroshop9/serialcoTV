from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product


class CategoryListAPI(APIView):
    def get(self, request):
        categories = Category.objects.filter(is_active=True).values('id', 'name')
        return Response({'success': True, 'categories': list(categories)})


class ProductListAPI(APIView):
    def get(self, request):
        category_id = request.query_params.get('category')
        
        products = Product.objects.filter(is_active=True, product_type='digital')
        if category_id:
            products = products.filter(category_id=category_id)
        
        data = products.values('id', 'name', 'price', 'product_type', 'image', 'category__name')
        return Response({'success': True, 'products': list(data)})


class ProductDetailAPI(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, is_active=True)
            return Response({
                'success': True,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': str(product.price),
                    'product_type': product.product_type,
                    'image': product.image.url if product.image else None,
                    'category': product.category.name if product.category else None,
                }
            })
        except Product.DoesNotExist:
            return Response({'success': False, 'message': 'المنتج غير موجود'}, status=404)