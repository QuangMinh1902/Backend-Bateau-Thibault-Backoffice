from django.urls import path
from monTiGMagasin import views

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('putonsale/<int:tig_id>/<str:new_price>/', views.PutOnSale.as_view()),
    path('removesale/<int:tig_id>/', views.RemoveSale.as_view()),
    path('incrementStock/<int:tig_id>/<int:number>/', views.IncrementStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:number>/', views.DecrementStock.as_view()),
    path('transaction/', views.Transaction.as_view()),
    path('transactions/month/<int:month_id>/', views.TransactionsByMonth.as_view()),
]
