# Generated by Django 2.2 on 2019-05-31 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=500)),
                ('cover', models.ImageField(null=True, upload_to='uploads/images/2019/05/31/')),
                ('submission_type', models.CharField(choices=[(0, 'standard'), (1, '20k mmr sous les mers'), (2, 'Taymapute')], default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('portrait', models.CharField(max_length=100)),
                ('portrait_lg', models.CharField(max_length=100)),
                ('portrait_full', models.CharField(max_length=100)),
                ('portrait_vert', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('cost', models.IntegerField()),
                ('secret_shop', models.BooleanField()),
                ('recipe', models.BooleanField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PatchVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', martor.models.MartorField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('cover', models.ImageField(null=True, upload_to='uploads/images/2019/05/31/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmissionSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('done', models.BooleanField(default='FALSE')),
                ('patch_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.PatchVersion')),
            ],
        ),
        migrations.CreateModel(
            name='VingtkmmrSubmission',
            fields=[
                ('emissionsubmission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.EmissionSubmission')),
                ('hero_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hero_1', to='www.Hero')),
                ('hero_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hero_2', to='www.Hero')),
            ],
            bases=('www.emissionsubmission',),
        ),
        migrations.CreateModel(
            name='TaymaputeSubmission',
            fields=[
                ('emissionsubmission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.EmissionSubmission')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Hero')),
                ('item_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_1', to='www.Hero')),
                ('item_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_2', to='www.Hero')),
                ('item_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_3', to='www.Hero')),
                ('item_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_4', to='www.Hero')),
                ('item_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_5', to='www.Hero')),
                ('item_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_6', to='www.Hero')),
            ],
            bases=('www.emissionsubmission',),
        ),
    ]
