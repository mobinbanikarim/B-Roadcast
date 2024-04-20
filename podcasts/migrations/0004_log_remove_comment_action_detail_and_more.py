# Generated by Django 4.2 on 2024-04-20 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_userdislike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('log', models.TextField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='action_detail',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='action_detail',
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislike_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='episode',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='episode_comments', to='podcasts.episode'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='podcasts.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='podcasts.user'),
        ),
    ]