from django.urls import path,include
from .views import okayamaagrifoods,okayamaagrifoodscontact,okayamaagrifoodscontactresult

urlpatterns = [
  
  path("okayama-agrifoods/"   ,okayamaagrifoods, name="okayama-agrifoods"),
  path("okayama-agrifoodscontact/"  ,okayamaagrifoodscontact.as_view(), name="okayama-agrifoodscontact"),
  path("okayama-agrifoodscontactresult/"  ,okayamaagrifoodscontactresult, name="okayama-agrifoodscontactresult"),
]