from django.shortcuts import render
from .forms import ImageForm
from .utils.template_search import rotate_func
from django.http import HttpResponse

def rotate_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        stat_code, an_image = rotate_func(request.FILES['image'])
        response = HttpResponse(status=stat_code, content_type="image/png")
        if stat_code != 400 and stat_code != 204:
            an_image.save(response, format='PNG')
        return response

    else:
        form = ImageForm()
    return render(request, 'rotate.html', {'form': form})