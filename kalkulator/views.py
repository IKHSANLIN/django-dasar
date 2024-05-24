from django.shortcuts import render, HttpResponse

# Create your views here.
def tambah(request, num1, num2):
    # context = {
    #     'title': 'kalkulator',
    #     'num1': num1,
    #     'num2': num2,
    #     'result': num1 + num2,
    #     'end-results': f"{num1} + {num2} = {num1+num2}"
    # }
    context = dict(
        title = 'kalkulator',
        result = f"{num1} + {num2} = {num1+num2}"
    )
    return render(request,'kalkulator/index.html',context)

def kurang(request, num1, num2):
    context = dict(
        title = 'kalkulator',
        result = f"{num1} - {num2} = {num1-num2}"
    )
    return render(request,'kalkulator/index.html',context)
def kali(request, num1, num2):
    context = dict(
        title = 'kalkulator',
        result = f"{num1} * {num2} = {num1*num2}"
    )
    return render(request,'kalkulator/index.html',context)
def bagi(request, num1, num2):
    context = dict(
        title = 'kalkulator',
        result = f"{num1} / {num2} = {num1/num2}"
    )
    return render(request,'kalkulator/index.html',context)