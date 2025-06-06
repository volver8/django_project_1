from django.contrib import admin

from .models import KanbanBoard, Project, SubTask, Tag, Task


admin.site.empty_value_display = "Не задано"


class SubTaskAdmin(admin.ModelAdmin):
    """Класс для отображения раздела подзадач в админке"""

    list_display = (
        "name",
        "description",
        "priority",
        "tasks",
        "time_estimation",
        "spent_time",
        "created_at",
    )
    search_fields = ("name",)
    list_filter = ("name", "priority", "created_at")
    list_display_links = ("name",)
    filter_horizontal = (
        "tags",
        "developers",
    )


class SubTaskInline(admin.TabularInline):
    """Класс для совместного отображения задач с подзадачами"""

    model = SubTask
    fk_name = "tasks"
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    """Класс для отображения раздела задач в админке"""

    inlines = (SubTaskInline,)

    list_display = (
        "name",
        "description",
        "ready_status",
        "priority",
        "kanboard",
        "time_estimation",
        "spent_time",
        "created_at",
    )
    search_fields = ("name",)
    list_filter = ("name", "kanboard", "priority", "created_at")
    list_display_links = ("name",)
    filter_horizontal = (
        "tags",
        "developers",
    )


class TaskInline(admin.TabularInline):
    """Класс для совместного отображения досок с задачами"""

    model = Task
    fk_name = "kanboard"
    extra = 0


class KanbanBoardAdmin(admin.ModelAdmin):
    """Класс для отображения раздела исполнители в админке"""

    inlines = (TaskInline,)

    list_display = ("name", "projects", "created_at")
    search_fields = ("name",)
    list_filter = ("projects", "created_at")
    list_display_links = ("name",)


class KanbanBoardInline(admin.TabularInline):
    """Класс для совместного отображения проектов с досками"""

    model = KanbanBoard
    fk_name = "projects"
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    """Класс для отображения раздела проектов в админке"""

    inlines = (KanbanBoardInline,)

    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("name", "created_at")
    list_display_links = ("name",)


admin.site.register(SubTask, SubTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(KanbanBoard, KanbanBoardAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
