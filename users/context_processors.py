from users.models import Customer


def navbar_context(request):
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user)
            image = customer.imageURL
        except Customer.DoesNotExist:
            image = None
    else:
        image = None
    return {"image": image}
