from core.models import Setting


def global_website_context(request):
    context = {
        'setting': Setting.objects.last(),
    }

    return context
