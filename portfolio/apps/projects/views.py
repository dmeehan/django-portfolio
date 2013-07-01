# projects/views.py

from django.conf import settings
from django.db.models import get_model
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    queryset = Project._default_manager.filter(status=Project.STATUS_LIVE).order_by('-featured', '-date_end')
    paginate_by = settings.PROJECT_PAGINATE_BY

class ProjectSizeAscListView(ProjectListView):
    queryset = Project._default_manager.size_asc()

class ProjectSizeListView(ProjectListView):
    queryset = Project._default_manager.live().order_by('area_normalized')

class ProjectSizeDescListView(ProjectListView):
    queryset = Project._default_manager.size_desc()

class ProjectDateListView(ProjectListView):
    pass

class ProjectCurrentListView(ProjectListView):
    pass

class ProjectCompletedListView(ProjectListView):
    pass

