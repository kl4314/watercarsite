# Generated by Django 2.0.3 on 2018-05-22 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waterapp', '0002_auto_20180522_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('title', models.CharField(max_length=200)),
                ('content', django_summernote.fields.SummernoteTextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('django_summernote.attachment',),
        ),
        migrations.AddField(
            model_name='comment2',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='waterapp.Post2'),
        ),
    ]
