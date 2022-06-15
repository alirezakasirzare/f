from services.models import Services


def best():
    services = Services.objects.all()
    scores = {service.id:service.score for service in services}
    max_value = 0
    values = []
    for value in scores:
        if scores.get(value) > max_value:
            max_value = scores.get(value)
            values.append(value)

    return values[::-1][:5]




