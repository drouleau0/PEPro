# Generated by Django 3.0.3 on 2020-04-01 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=70)),
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company2company_id', to='homepage.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(default=None, max_length=10000)),
                ('review_created_at', models.DateTimeField(blank=True, default=None)),
                ('status', models.CharField(choices=[('E', 'editing'), ('S', 'sent')], default='E', max_length=10)),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewee2id', to='homepage.Employee')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer2id', to='homepage.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_created_at', models.DateTimeField(auto_now_add=True)),
                ('request_reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_reviewee2id', to='homepage.Employee')),
                ('request_reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_reviewer2id', to='homepage.Employee')),
            ],
        ),
    ]
