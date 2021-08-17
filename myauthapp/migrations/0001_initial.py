# Generated by Django 3.2.6 on 2021-08-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('work_class', models.CharField(choices=[('Private', 'Private'), ('Unincorporated self employment', 'Unincorporated self employment'), ('Incorporated self employment', 'Incorporated self employment'), ('Federal Government', 'Federal Government'), ('Local Government', 'Local Government'), ('State Government', 'State Government'), ('Without Pay', 'Without Pay'), ('Never Worked', 'Never Worked')], max_length=50)),
                ('education', models.CharField(choices=[('PreSchool to 12th Grade', 'PreSchool to 12th Grade'), ('High School Graduate', 'High School Graduate'), ('Some College', 'Some College'), ('Associate', 'Associate'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Professional School', 'Professional School'), ('Doctorate', 'Doctorate')], max_length=50)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Divorced', 'Divorced'), ('Never Married', 'Never Married'), ('Separated', 'Separated'), ('Widowed', 'Widowed')], max_length=50)),
                ('occupation', models.CharField(choices=[('Technical Support', 'Technical Support'), ('Craft Repair', 'Craft Repair'), ('Sales', 'Sales'), ('Executive Manager', 'Executive Manager'), ('Professional Specialty', 'Professional Specialty'), ('Handlers or Cleaners', 'Handlers or Cleaners'), ('Machine Operator Inspector', 'Machine Operator Inspector'), ('Administrative Clerks', 'Administrative Clerks'), ('Farming or Fishing', 'Farming or Fishing'), ('Transport and Moving Services', 'Transport and Moving Services'), ('Private House Services', 'Private House Services'), ('Protective Services', 'Protective Services'), ('Armed Forces', 'Armed Forces'), ('Other Services', 'Other Services')], max_length=50)),
                ('relationship', models.CharField(choices=[('Wife', 'Wife'), ('Own Child', 'Own Child'), ('Husband', 'Husband'), ('Other Relative', 'Other Relative'), ('Unmarried', 'Unmarried'), ('Not In Family', 'Not In Family')], max_length=20)),
                ('race', models.CharField(choices=[('White', 'White'), ('Asian/Pacific Islander', 'Asian/Pacific Islander'), ('American Indian/Eskimo', 'American Indian/Eskimo'), ('Black', 'Black'), ('Other', 'Other')], max_length=30)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('capital_gain', models.IntegerField()),
                ('capital_loss', models.IntegerField()),
                ('hours_per_week', models.IntegerField()),
                ('native_country', models.CharField(choices=[('United States', 'United States'), ('Other Country', 'Other Country')], max_length=30)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
    ]
