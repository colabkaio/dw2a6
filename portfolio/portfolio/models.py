from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(verbose_name="Imagem", upload_to="projects")
    link = models.URLField(verbose_name="Endereço da Internet", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    class Meta:
        verbose_name = "projeto ou experiência"
        verbose_name_plural = "projetos ou experiências"
        ordering = ["-created"]

    def __str__(self):
        return self.title