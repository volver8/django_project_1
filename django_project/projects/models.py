from django.contrib.auth import get_user_model
from django.db import models


MAX_LEN = 256

User = get_user_model()


class CreatedAt(models.Model):
    """Абстрактный класс"""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        abstract = True


class TaskSubTask(CreatedAt):
    """Абстрактный класс"""

    description = models.TextField("Описание")
    time_estimation = models.TimeField("Оценка времени")
    spent_time = models.TimeField("Затраченное время")

    class Meta:
        abstract = True


class ReadyStatus(models.Model):
    """Модель для статуса готовности задач и подзадач"""

    name = models.CharField("Статус готовности", max_length=MAX_LEN)

    class Meta:
        verbose_name = "статус готовности"
        verbose_name_plural = "Статусы готовности"

    def __str__(self):
        return self.name


class Priority(models.Model):
    """Модель для приоритета задач и подзадач"""

    name = models.CharField("Приоритет", max_length=MAX_LEN)

    class Meta:
        verbose_name = "приоритет"
        verbose_name_plural = "Приоритеты"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Модель для тегов"""

    name = models.CharField("Название тэга", max_length=MAX_LEN)

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Project(CreatedAt):
    """Модель для проектов"""

    name = models.CharField("Название проекта", max_length=MAX_LEN)

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


class KanbanBoard(CreatedAt):
    """Модель для досок в проекте"""

    name = models.CharField("Название доски", max_length=MAX_LEN)
    projects = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="kanbanboards",
    )

    def __str__(self):
        return self.name


class Task(TaskSubTask):
    """Модель для задач"""

    name = models.CharField("Название задачи", max_length=MAX_LEN)
    ready_status = models.ForeignKey(
        ReadyStatus,
        on_delete=models.PROTECT,
        verbose_name="Статус готовности",
        null=False,
        blank=False,
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Теги",
        blank=True,
    )
    developers = models.ManyToManyField(
        User,
        verbose_name="Исполнители",
        blank=True,
    )
    kanboard = models.ForeignKey(
        KanbanBoard,
        on_delete=models.CASCADE,
        verbose_name="Доска",
        null=True,
        blank=True,
        related_name="tasks",
    )

    def __str__(self):
        return self.name


class SubTask(TaskSubTask):
    """Модель для подзадач"""

    name = models.CharField("Название подзадачи", max_length=MAX_LEN)
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Теги",
        blank=True,
    )
    developers = models.ManyToManyField(
        User,
        verbose_name="Исполнители",
        blank=True,
    )
    tasks = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name="Задание",
        null=False,
        blank=False,
        related_name="subtasks",
    )

    def __str__(self):
        return self.name
