from rest_framework import generics

from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers



class showproduct(generics.ListCreateAPIView):
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializers 
    
    
  def get(self, request, *args, **kwargs):
    
      products = self.get_queryset()
      serializer = self.get_serializer(products, many=True)
      # if serializer.is_valid():
        
      return Response(serializer.data)
      
      
      
       
     
    
    
    
    
    
    
