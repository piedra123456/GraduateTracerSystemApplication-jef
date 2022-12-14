# Generated by Django 4.0.5 on 2022-09-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0034_rename_campus_schoolgraduated_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='argao_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='barili_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bsit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='carmen_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cebu_city_mountain_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='daanbantayan_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='danao_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dumanjug_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='employed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ginatilan_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='main_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='moalboal_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='naga_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='oslob_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pinamungajan_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='san_fernando_extension_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='san_francisco_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tuburan_campus',
        ),
        migrations.RemoveField(
            model_name='user',
            name='unemployed',
        ),
        migrations.AlterField(
            model_name='user',
            name='course_type',
            field=models.CharField(blank=True, choices=[('Bachelor of Science in Information Technology', 'Bachelor of Science in Information Technology'), ('Bachelor in Industrial Technology Major in Computer Technology', 'Bachelor in Industrial Technology Major in Computer Technology'), ('Bachelor in Elementary Education', 'Bachelor in Elementary Education'), ('Bachelor in Industrial Technology - Drafting Technology', 'Bachelor in Industrial Technology - Drafting Technology'), ('Bachelor in Industrial Technology - Electrical Technology', 'Bachelor in Industrial Technology - Electrical Technology'), ('Bachelor in Industrial Technology -  Electronics Technology', 'Bachelor in Industrial Technology -  Electronics Technology'), ('Bachelor in Industrial Technology - Automotive Technology', 'Bachelor in Industrial Technology - Automotive Technology'), ('Bachelor in Industrial Technology - Food Technology', 'Bachelor in Industrial Technology - Food Technology'), ('Bachelor in Industrial Technology - Garments Technology', 'Bachelor in Industrial Technology - Garments Technology'), ('Bachelor in Industrial Technology - Machine Shop Technology', 'Bachelor in Industrial Technology - Machine Shop Technology'), ('Bachelor in Industrial Technology - Welding and Fabrication Technology', 'Bachelor in Industrial Technology - Welding and Fabrication Technology'), ('Bachelor in Secondary Education Major in Math', 'Bachelor in Secondary Education Major in Math'), ('Bachelor in Secondary Education Major in Science', 'Bachelor in Secondary Education Major in Science'), ('Bachelor in Secondary Education Major in English', 'Bachelor in Secondary Education Major in English'), ('Bachelor in Secondary Education Major in Social Studies', 'Bachelor in Secondary Education Major in Social Studies'), ('Bachelor of Technology and Livelihood Education', 'Bachelor of Technology and Livelihood Education'), ('Bachelor of Technology and Livelihood Education Major in Home Economics', 'Bachelor of Technology and Livelihood Education Major in Home Economics'), ('Bachelor of Technology and Livelihood Education Major in Information and Communications Technology', 'Bachelor of Technology and Livelihood Education Major in Information and Communications Technology'), ('Bachelor of Arts in English', 'Bachelor of Arts in English'), ('Bachelor of Arts in English Major in Language Studies', 'Bachelor of Arts in English Major in Language Studies'), ('Bachelor of Arts in Literature', 'Bachelor of Arts in Literature'), ('Bachelor of Arts in Literature Major in Literature and Cultural Studies', 'Bachelor of Arts in Literature Major in Literature and Cultural Studies'), ('Bachelor of Early Childhood Education', 'Bachelor of Early Childhood Education'), ('Bachelor in Elementary Education Major in Content Education', 'Bachelor in Elementary Education Major in Content Education'), ('Bachelor of Industrial Technology Major in Civil Technology', 'Bachelor of Industrial Technology Major in Civil Technology'), ('Bachelor of Industrial Technology Major in Cosmetology', 'Bachelor of Industrial Technology Major in Cosmetology'), ('Bachelor of Industrial Technology Major in Furniture and Cabinetmaking Technology', 'Bachelor of Industrial Technology Major in Furniture and Cabinetmaking Technology'), ('Bachelor of Industrial Technology Major in Interior Design Technology', 'Bachelor of Industrial Technology Major in Interior Design Technology'), ('Bachelor of Industrial Technology Major in Power Plant Technology', 'Bachelor of Industrial Technology Major in Power Plant Technology'), ('Bachelor of Industrial Technology Major in Refrigeration and and Air-Conditioning Technology', 'Bachelor of Industrial Technology Major in Refrigeration and and Air-Conditioning Technology'), ('Bachelor of Public Administration', 'Bachelor of Public Administration'), ('Bachelor of Science in AgriBusiness', 'Bachelor of Science in AgriBusiness'), ('Bachelor of Science in Agricultural and Biosystems Engineering', 'Bachelor of Science in Agricultural and Biosystems Engineering'), ('Bachelor of Science in Agriculture', 'Bachelor of Science in Agriculture'), ('Bachelor of Science in Agriculture Major in Horticulture', 'Bachelor of Science in Agriculture Major in Horticulture'), ('Bachelor of Science in Agriculture-Animal Production', 'Bachelor of Science in Agriculture-Animal Production'), ('Bachelor of Science in Business Administration - MM', 'Bachelor of Science in Business Administration - MM'), ('Bachelor of Science in Civil Engineering', 'Bachelor of Science in Civil Engineering'), ('Bachelor of Science in Computer Engineering', 'Bachelor of Science in Computer Engineering'), ('Bachelor of Science in Development Communication', 'Bachelor of Science in Development Communication'), ('Bachelor of Science in Electrical Engineering', 'Bachelor of Science in Electrical Engineering'), ('Bachelor of Science in Electronic Engineering', 'Bachelor of Science in Electronic Engineering'), ('Bachelor of Science in Fisheries', 'Bachelor of Science in Fisheries'), ('Bachelor of Science in Food Technology', 'Bachelor of Science in Food Technology'), ('Bachelor of Science in Forestry', 'Bachelor of Science in Forestry'), ('Bachelor of Science in Graphics and Designs', 'Bachelor of Science in Graphics and Designs'), ('Bachelor of Science in Hospitality Management', 'Bachelor of Science in Hospitality Management'), ('Bachelor of Science in Industrial Engineering', 'Bachelor of Science in Industrial Engineering'), ('Bachelor of Science in Marine Engineering', 'Bachelor of Science in Marine Engineering'), ('Bachelor of Science in Mathematics', 'Bachelor of Science in Mathematics'), ('Bachelor of Science in Mechanical Engineering', 'Bachelor of Science in Mechanical Engineering'), ('Bachelor of Science in Mechatronics Technology', 'Bachelor of Science in Mechatronics Technology'), ('Bachelor of Science in Nursing', 'Bachelor of Science in Nursing'), ('Bachelor of Science in Psychology', 'Bachelor of Science in Psychology'), ('Bachelor of Science in Statistics', 'Bachelor of Science in Statistics'), ('Bachelor of Science in Technology Management', 'Bachelor of Science in Technology Management'), ('Bachelor of Science in Tourism Management', 'Bachelor of Science in Tourism Management'), ('Bachelor of Special Needs Education Major in Generalist', 'Bachelor of Special Needs Education Major in Generalist'), ('Bachelor of Special Needs Education Major in Teaching and Hard of Hearing Learners', 'Bachelor of Special Needs Education Major in Teaching and Hard of Hearing Learners'), ('Bachelor of Technical and Vocational Teachers Education', 'Bachelor of Technical and Vocational Teachers Education'), ('Bachelor of Technical Vocational Teacher Education Major in Automotive Technology', 'Bachelor of Technical Vocational Teacher Education Major in Automotive Technology'), ('Bachelor of Technical Vocational Teacher Education Major in Drafting Technology', 'Bachelor of Technical Vocational Teacher Education Major in Drafting Technology'), ('Bachelor of Technical Vocational Teacher Education Major in Electrical Technology', 'Bachelor of Technical Vocational Teacher Education Major in Electrical Technology'), ('Bachelor of Technical Vocational Teacher Education Major in Electronics Technology', 'Bachelor of Technical Vocational Teacher Education Major in Electronics Technology'), ('Bachelor of Technical Vocational Teacher Education Major in Food Service Management', 'Bachelor of Technical Vocational Teacher Education Major in Food Service Management'), ('Bachelor of Technical Vocational Teacher Education Major in Garments Fashion and Design', 'Bachelor of Technical Vocational Teacher Education Major in Garments Fashion and Design'), ('Bachelor of Technical Vocational Teacher Education Major in Welding and Fabrication Technology', 'Bachelor of Technical Vocational Teacher Education Major in Welding and Fabrication Technology'), ('Bachelor of Technology and Livelihood Education Major in Industrial Arts', 'Bachelor of Technology and Livelihood Education Major in Industrial Arts'), ('Batsilyer ng Sining sa Filipino', 'Batsilyer ng Sining sa Filipino'), ('Certificate in Professional Education', 'Certificate in Professional Education'), ('Certificate of Technology Major in Computer Technology - Deaf Students', 'Certificate of Technology Major in Computer Technology - Deaf Students'), ('Certificate of Technology Major in Food Technology - Deaf Students', 'Certificate of Technology Major in Food Technology - Deaf Students'), ('DECE Practice Teaching', 'DECE Practice Teaching'), ('Diploma in Early Childhood Education', 'Diploma in Early Childhood Education'), ('Diploma in Early Childhood Education - Blended Learning', 'Diploma in Early Childhood Education - Blended Learning'), ('Diploma in Professional Education', 'Diploma in Professional Education'), ('Diploma in Professional Education - Blended Learning', 'Diploma in Professional Education - Blended Learning'), ('Diploma in Special Education', 'Diploma in Special Education'), ('Diploma in Special Education - Blended Learning', 'Diploma in Special Education - Blended Learning'), ('Doctor in Development Education', 'Doctor in Development Education'), ('Doctor in Development Education Major in Early Childhood Education', 'Doctor in Development Education Major in Early Childhood Education'), ('Doctor in Public Administration', 'Doctor in Public Administration'), ('Doctor in Development Education Major in Early Childhood Education - Blended Learning', 'Doctor in Development Education Major in Early Childhood Education - Blended Learning'), ('Doctor in Development Education Major in Guidance and Counseling', 'Doctor in Development Education Major in Guidance and Counseling'), ('Doctor in Development Education Major in Guidance and Counseling - Blended Learning', 'Doctor in Development Education Major in Guidance and Counseling - Blended Learning'), ('Doctor in Development Education Major in Special Education', 'Doctor in Development Education Major in Special Education'), ('Doctor in Development Education Major in Sped-Blended Learning', 'Doctor in Development Education Major in Sped-Blended Learning'), ('Doctor of Philosophy in Animal Science', 'Doctor of Philosophy in Animal Science'), ('Doctor of Philosophy in Horticulture', 'Doctor of Philosophy in Horticulture'), ('Doctor of Philosophy in Technology Management', 'Doctor of Philosophy in Technology Management'), ('Doctor of Veterinary Medicine', 'Doctor of Veterinary Medicine'), ('DPE Practice Teaching - Blended Learning', 'DPE Practice Teaching - Blended Learning'), ('DSPED Practice Teaching', ' DSPED Practice Teaching'), ('Foundation of Education-MAED ECE-Blended Learning', 'Foundation of Education-MAED ECE-Blended Learning'), ('Foundation of Education-MAED GC-Blended Learning', 'Foundation of Education-MAED GC-Blended Learning'), ('Foundation of Education-MAED Math-Blended Learning', 'Foundation of Education-MAED Math-Blended Learning'), ('Foundation of Education-MAED Sped-Blended Learning', 'Foundation of Education-MAED Sped-Blended Learning'), ('Master in Engineering Technology', 'Master in Engineering Technology'), ('Master in Fisheries and Aquatic Sciences', 'Master in Fisheries and Aquatic Sciences'), ('Master in Public Administration', 'Master in Public Administration'), ('Master in Technician Education Major in Automotive Technology', 'Master in Technician Education Major in Automotive Technology'), ('Master in Technician Education Major in Civil Technology', 'Master in Technician Education Major in Civil Technology'), ('Master in Technician Education Major in Drafting Technology', 'Master in Technician Education Major in Drafting Technology'), ('Master in Technician Education Major in Electrical Technology', 'Master in Technician Education Major in Electrical Technology'), ('Master in Technician Education Major in Electronics Technology', 'Master in Technician Education Major in Electronics Technology'), ('Master in Technician Education Major in Machine Shop Technology', 'Master in Technician Education Major in Machine Shop Technology'), ('Master in Vocational Education', 'Master in Vocational Education'), ('Master of Arts in Education Major in Administration and Supervision', 'Master of Arts in Education Major in Administration and Supervision'), ('Master of Arts in Education Major in Early Childhood Education', 'Master of Arts in Education Major in Early Childhood Education'), ('Master of Arts in Education Major in English Teaching', 'Master of Arts in Education Major in English Teaching'), ('Master of Arts in Education Major in Filipino Teaching', 'Master of Arts in Education Major in Filipino Teaching'), ('Master of Arts in Education Major in Guidance and Counseling', 'Master of Arts in Education Major in Guidance and Counseling'), ('Master of Arts in Education Major in Mathematics', 'Master of Arts in Education Major in Mathematics'), ('Master of Arts in Education Major in Teaching Biology', 'Master of Arts in Education Major in Teaching Biology'), ('Master of Arts in Education Major in Teaching Chemistry', 'Master of Arts in Education Major in Teaching Chemistry'), ('Master of Arts in Education Major in Teaching Science', 'Master of Arts in Education Major in Teaching Science'), ('Master of Arts in Education Major in Teaching Social Studies', 'Master of Arts in Education Major in Teaching Social Studies'), ('Master of Arts in Education Major in Teaching Mathematics', 'Master of Arts in Education Major in Teaching Mathematics'), ('Master of Arts in Education Major in Teaching Physical Education', 'Master of Arts in Education Major in Teaching Physical Education'), ('Master of Arts in Education Major in Teaching Physical Education and Sports', 'Master of Arts in Education Major in Teaching Physical Education and Sports'), ('Master of Arts in Education Major in Teaching Physics', 'Master of Arts in Education Major in Teaching Physics'), ('Master of Arts in Vocational Education', 'Master of Arts in Vocational Education'), ('Master of Science in AgriBusiness', 'Master of Science in AgriBusiness')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, choices=[('Argao Campus', 'Argao Campus'), ('Barili Campus', 'Barili Campus'), ('Carmen Campus', 'Carmen Campus'), ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'), ('Daanbantayan Campus', 'Daanbantayan Campus'), ('Danao Campus', 'Danao Campus'), ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'), ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'), ('Main Campus', 'Main Campus'), ('Moalboal Campus', 'Moalboal Campus'), ('Naga Extension Campus', 'Naga Extension Campus'), ('Oslob Extension Campus', 'Oslob Extension Campus'), ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'), ('San Fernando Extension Campus', 'San Fernando Extension Campus'), ('San Francisco Campus', 'San Francisco Campus'), ('Tuburan Campus', 'Tuburan Campus')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='CourseGraduated',
        ),
        migrations.DeleteModel(
            name='GraduateStatus',
        ),
        migrations.DeleteModel(
            name='SchoolGraduated',
        ),
    ]
