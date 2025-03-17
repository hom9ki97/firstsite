from .models import Language


def language_context_processor(request):
    context = {'languages': Language.objects.all()}
    return context
