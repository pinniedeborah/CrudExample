from django.urls import path
import employee.views as view

urlpatterns=[
    path("show",view.show),
    path('emp', view.emp),  
    path('edit/<int:id>', view.edit),  
    path('update/<int:id>', view.update),  
    path('delete/<int:id>', view.destroy), 
    
]