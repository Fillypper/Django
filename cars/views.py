from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    print(request)
    
    cars = Car.objects.all() #passing only argument brand= it will be able to search only for id numbers or if u put brand__name= u will be able to search by brand name like 'Chevrolet'
                                            #We can search only for strings when our db have this collun with a string name like model='ram'
                                            #we can use __contains also to search certains things in a collunm, like model__contains='Ram'
    return render(                          
        request,
        'cars.html',
        {'cars': cars}
    )

