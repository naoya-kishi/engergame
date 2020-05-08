from django.db import models

class BusinessMonthlyGoals(models.Model):
    company = models.ForeignKey('Company', models.DO_NOTHING)
    user_company = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    target_month = models.PositiveIntegerField()
    sales = models.PositiveIntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)
    matching = models.PositiveIntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_monthly_goals'
        unique_together = (('target_month', 'user_company'),)


class BusinessTalkStatus(models.Model):
    business_talk_status_id = models.AutoField(primary_key=True)
    company_id = models.PositiveIntegerField()
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    phase = models.PositiveIntegerField(blank=True, null=True)
    accuracy = models.PositiveIntegerField(blank=True, null=True)
    money = models.PositiveIntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)
    proposal_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    lost_flag = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'business_talk_status'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_manager = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True, related_name = "company_manager")
    business_type = models.CharField(max_length=11, blank=True, null=True)
    industry = models.CharField(max_length=11, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    company_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    media_id = models.CharField(max_length=50, blank=True, null=True)
    media_company_id = models.CharField(max_length=50, blank=True, null=True)
    prefecture = models.ForeignKey('MPrefecture', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('MCity', models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    billing_prefecture_id = models.CharField(max_length=11, blank=True, null=True)
    billing_city_id = models.CharField(max_length=11, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_address2 = models.CharField(max_length=255, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=30, blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)
    billing_department = models.CharField(max_length=255, blank=True, null=True)
    billing_position = models.CharField(max_length=255, blank=True, null=True)
    billing_address_same_flag = models.IntegerField(blank=True, null=True)
    hp_url = models.CharField(max_length=255, blank=True, null=True)
    movie_url = models.CharField(max_length=255, blank=True, null=True)
    rep_name = models.CharField(max_length=255, blank=True, null=True)
    rep_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    rep_dep_name = models.CharField(max_length=255, blank=True, null=True)
    rep_position = models.CharField(max_length=255, blank=True, null=True)
    rep_email = models.CharField(max_length=255, blank=True, null=True)
    rep_phone_number = models.CharField(max_length=255, blank=True, null=True)
    establishment_date = models.CharField(max_length=255, blank=True, null=True)
    employees_number = models.CharField(max_length=255, blank=True, null=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    sales = models.CharField(max_length=255, blank=True, null=True)
    company_caption = models.TextField(blank=True, null=True)
    company_document = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)
    registration_phase = models.IntegerField()
    company_name_release_flag = models.IntegerField(blank=True, null=True)
    pickup_flag = models.IntegerField(blank=True, null=True)
    release_flag = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'
        unique_together = (('media_id', 'media_company_id'),)


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class HrApplicant(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    platform = models.ForeignKey('MPlatform', models.DO_NOTHING, blank=True, null=True)
    apply_date = models.DateField(blank=True, null=True)
    share_to_id = models.IntegerField(blank=True, null=True)
    apply_medium_id = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    first_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    initial_name = models.CharField(max_length=10, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    prefecture_id = models.CharField(max_length=11, blank=True, null=True)
    city_id = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    nearest_station = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)
    resume = models.CharField(max_length=255, blank=True, null=True)
    other_resume = models.CharField(max_length=255, blank=True, null=True)
    portfolio = models.CharField(max_length=255, blank=True, null=True)
    educational_background = models.CharField(max_length=255, blank=True, null=True)
    educational_background_detail = models.CharField(max_length=255, blank=True, null=True)
    graduate_date = models.DateField(blank=True, null=True)
    release_flag = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    last_update_user = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant'


class HrApplicantQuestion(models.Model):
    applicant = models.ForeignKey(HrApplicant, models.DO_NOTHING, primary_key=True)
    motivation = models.TextField()
    objective_short = models.CharField(max_length=255, blank=True, null=True)
    objective_medium = models.CharField(max_length=255, blank=True, null=True)
    objective_long = models.CharField(max_length=255, blank=True, null=True)
    self_introduction_sp = models.CharField(max_length=255, blank=True, null=True)
    self_introduction_wp = models.CharField(max_length=255, blank=True, null=True)
    seeking = models.TextField(blank=True, null=True)
    eyesight = models.TextField(blank=True, null=True)
    join_period = models.CharField(max_length=255, blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    ses_propriety = models.IntegerField()
    skill_language = models.TextField(blank=True, null=True)
    study_style = models.TextField(blank=True, null=True)
    study_time = models.TextField(blank=True, null=True)
    desired_contract_type = models.CharField(max_length=11)
    job_category_id = models.PositiveIntegerField()
    desired_annual_salary = models.PositiveIntegerField(blank=True, null=True)
    desired_work_time = models.PositiveIntegerField(blank=True, null=True)
    desired_work_day = models.PositiveIntegerField(blank=True, null=True)
    desired_etc = models.TextField(blank=True, null=True)
    last_update_user = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant_question'


class HrSelectionResult(models.Model):
    applicant = models.ForeignKey(HrApplicant, models.DO_NOTHING, primary_key=True)
    selection_status_id = models.IntegerField()
    user_company_id = models.IntegerField(blank=True, null=True)
    selection_type_id = models.IntegerField(blank=True, null=True)
    interview_date = models.DateTimeField(blank=True, null=True)
    other_selection = models.TextField(blank=True, null=True)
    assessment = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    first_impression = models.IntegerField(blank=True, null=True)
    comprehension = models.IntegerField(blank=True, null=True)
    earnest = models.IntegerField(blank=True, null=True)
    aggressive = models.IntegerField(blank=True, null=True)
    cooperation = models.IntegerField(blank=True, null=True)
    fixing = models.IntegerField(blank=True, null=True)
    communication = models.IntegerField(blank=True, null=True)
    del_flag = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_selection_result'
        unique_together = (('applicant', 'selection_status_id'),)


class HrWorkerHistory(models.Model):
    applicant = models.ForeignKey(HrApplicant, models.DO_NOTHING, primary_key=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    work_content = models.CharField(max_length=255, blank=True, null=True)
    retirement_reason = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    last_update_user = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_worker_history'


class Inquiry(models.Model):
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    inquiry_item = models.CharField(max_length=128)
    inquiry_message = models.TextField()
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquiry'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LineTmporaryRegistration(models.Model):
    line_id = models.CharField(unique=True, max_length=255)
    regist_id = models.CharField(max_length=255)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'line_tmporary_registration'


class LpInquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    entry_service_id = models.IntegerField(blank=True, null=True)
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    birth_y = models.CharField(max_length=4)
    birth_m = models.CharField(max_length=2)
    birth_d = models.CharField(max_length=2)
    sex = models.CharField(max_length=2)
    tel = models.CharField(max_length=16)
    mail = models.CharField(max_length=255)
    zip = models.CharField(max_length=8)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    skill = models.CharField(max_length=255, blank=True, null=True)
    doc1 = models.CharField(max_length=255, blank=True, null=True)
    doc2 = models.CharField(max_length=255, blank=True, null=True)
    education1 = models.CharField(max_length=8, blank=True, null=True)
    education_y = models.CharField(max_length=4, blank=True, null=True)
    education_name = models.CharField(max_length=255, blank=True, null=True)
    education_txt = models.TextField(blank=True, null=True)
    lang_jp = models.CharField(max_length=8, blank=True, null=True)
    lang_en = models.CharField(max_length=8, blank=True, null=True)
    toeic = models.IntegerField(blank=True, null=True)
    lang_other = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_y_a = models.CharField(max_length=4, blank=True, null=True)
    company_m_a = models.CharField(max_length=2, blank=True, null=True)
    company_y_b = models.CharField(max_length=4, blank=True, null=True)
    company_m_b = models.CharField(max_length=2, blank=True, null=True)
    company_type = models.CharField(max_length=8, blank=True, null=True)
    company_text = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lp_inquiry'


class MAnotherFeature(models.Model):
    another_feature_id = models.CharField(primary_key=True, max_length=11)
    another_feature_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_another_feature'


class MCity(models.Model):
    city_id = models.CharField(primary_key=True, max_length=11)
    prefecture = models.ForeignKey('MPrefecture', models.DO_NOTHING)
    city_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_city'


class MCode(models.Model):
    category = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255)
    display_order = models.IntegerField()
    display_name = models.CharField(max_length=255)
    col_1 = models.CharField(max_length=255, blank=True, null=True)
    col_2 = models.CharField(max_length=255, blank=True, null=True)
    col_3 = models.CharField(max_length=255, blank=True, null=True)
    col_4 = models.CharField(max_length=255, blank=True, null=True)
    col_5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_code'
        unique_together = (('category', 'code'),)


class MJob(models.Model):
    job_id = models.CharField(primary_key=True, max_length=11)
    job_category = models.ForeignKey('MJobCategory', models.DO_NOTHING)
    job_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_job'


class MJobCategory(models.Model):
    job_category_id = models.CharField(primary_key=True, max_length=11)
    job_category_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_job_category'


class MMedia(models.Model):
    media_id = models.CharField(primary_key=True, max_length=50)
    media_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    del_flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'm_media'


class MPlatform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(unique=True, max_length=255)
    ip_adress = models.CharField(max_length=5)
    display_order = models.PositiveIntegerField()
    del_flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'm_platform'


class MPrefecture(models.Model):
    prefecture_id = models.CharField(primary_key=True, max_length=11)
    region = models.ForeignKey('MRegion', models.DO_NOTHING)
    prefecture_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_prefecture'


class MProjectFeature(models.Model):
    project_feature_id = models.CharField(primary_key=True, max_length=11)
    project_feature_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_project_feature'


class MRecordingSite(models.Model):
    recording_site_id = models.AutoField(primary_key=True)
    recording_site_name = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
    display_order = models.IntegerField()
    del_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_recording_site'


class MRegion(models.Model):
    region_id = models.CharField(primary_key=True, max_length=11)
    region_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_region'


class MSkill(models.Model):
    skill_id = models.CharField(primary_key=True, max_length=11)
    skill_category_id = models.CharField(max_length=11, blank=True, null=True)
    skill_name = models.CharField(max_length=255)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_skill'


class MSkillWeight(models.Model):
    skill = models.ForeignKey(MSkill, models.DO_NOTHING, primary_key=True)
    skill_weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'm_skill_weight'


class MStation(models.Model):
    station_id = models.PositiveIntegerField(primary_key=True)
    station_name = models.CharField(max_length=255)
    prefecture = models.ForeignKey(MPrefecture, models.DO_NOTHING)
    city = models.ForeignKey(MCity, models.DO_NOTHING)
    postal_code = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    line_id = models.PositiveIntegerField()
    line_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'm_station'


class MessageDetail(models.Model):
    message_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('MessageRoom', models.DO_NOTHING)
    sender_id = models.PositiveIntegerField()
    sender_type = models.CharField(max_length=10)
    message = models.TextField(blank=True, null=True)
    original_file_name = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    read_flag = models.IntegerField()
    del_flag = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message_detail'


class MessageRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    user_company = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    del_flag = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message_room'
        unique_together = (('company', 'worker', 'user_company'),)


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Offer(models.Model):
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'


class OfferToWorker(models.Model):
    user_company_id = models.PositiveIntegerField()
    worker_id = models.PositiveIntegerField()
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_to_worker'


class ParticipationStatus(models.Model):
    participation_status_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participation_status'


class PreSignup(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    first_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    one_time_token = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_signup'
        unique_together = (('email', 'one_time_token'),)


class PreSignupCompany(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    one_time_token = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_signup_company'
        unique_together = (('email', 'one_time_token'),)


class PreWorkerQuestionnaire(models.Model):
    id = models.PositiveIntegerField(blank=True, primary_key=True)
    email = models.ForeignKey(PreSignup, models.DO_NOTHING, db_column='email', blank=True, null=True)
    ans1 = models.CharField(max_length=11, blank=True, null=True)
    ans2 = models.CharField(max_length=11, blank=True, null=True)
    ans3 = models.CharField(max_length=11, blank=True, null=True)
    capital = models.CharField(max_length=11, blank=True, null=True)
    working_experience = models.CharField(max_length=11, blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_worker_questionnaire'


class PreWorkerSkill(models.Model):
    email = models.ForeignKey(PreSignup, models.DO_NOTHING, db_column='email')
    skill_id = models.CharField(max_length=11)
    experience_id = models.CharField(max_length=11, blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_worker_skill'
        unique_together = (('email', 'skill_id'),)


class PreWorkerSns(models.Model):
    email = models.ForeignKey(PreSignup, models.DO_NOTHING, db_column='email')
    sns_id = models.CharField(max_length=11)
    sns_account = models.CharField(max_length=255, blank=True, null=True)
    follow_user_num = models.IntegerField(blank=True, null=True)
    follower_user_num = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_worker_sns'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name = "company")
    project_company_id = models.PositiveIntegerField(blank=True, null=True)
    media = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name = "media")
    media_company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name = "media_company")
    media_project_id = models.CharField(max_length=50, blank=True, null=True)
    media_url = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.ForeignKey('UserCompany', models.DO_NOTHING, blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    job = models.ForeignKey(MJob, models.DO_NOTHING, blank=True, null=True)
    position = models.CharField(max_length=11, blank=True, null=True)
    prefecture = models.ForeignKey(MPrefecture, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(MCity, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    nearest_station = models.CharField(max_length=255, blank=True, null=True)
    pay_rate_min = models.CharField(max_length=11, blank=True, null=True)
    pay_rate_max = models.CharField(max_length=11, blank=True, null=True)
    project_category = models.CharField(max_length=255, blank=True, null=True)
    monthly_income_min = models.IntegerField(blank=True, null=True)
    monthly_income_max = models.IntegerField(blank=True, null=True)
    monthly_income = models.CharField(max_length=255, blank=True, null=True)
    settlement_time = models.CharField(max_length=255, blank=True, null=True)
    contract_period = models.CharField(max_length=255, blank=True, null=True)
    working_days = models.CharField(max_length=255, blank=True, null=True)
    working_system = models.CharField(max_length=255, blank=True, null=True)
    recruitment_restrictions = models.CharField(max_length=255, blank=True, null=True)
    number_of_interviews = models.IntegerField(blank=True, null=True)
    contract_type = models.CharField(max_length=11, blank=True, null=True)
    project_requirements = models.TextField(blank=True, null=True)
    project_outline = models.TextField(blank=True, null=True)
    salary = models.TextField(blank=True, null=True)
    welfare = models.TextField(blank=True, null=True)
    vacation = models.TextField(blank=True, null=True)
    selection_process = models.TextField(blank=True, null=True)
    desired_personality = models.TextField(blank=True, null=True)
    working_time_from = models.TimeField(blank=True, null=True)
    working_time_to = models.TimeField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    skill_management = models.CharField(max_length=11, blank=True, null=True)
    skill_english = models.CharField(max_length=11, blank=True, null=True)
    recruitment_number = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)
    inexperience_ok = models.IntegerField(blank=True, null=True)
    work_start_date = models.DateField(blank=True, null=True)
    agent_comment = models.TextField(blank=True, null=True)
    posting_end_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    pickup_flag = models.IntegerField(blank=True, null=True)
    release_flag = models.IntegerField(blank=True, null=True)
    recruitment_end_flag = models.IntegerField(blank=True, null=True)
    recruitment_end_date = models.DateField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    project_feature = models.ForeignKey(MAnotherFeature, models.DO_NOTHING)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_feature'
        unique_together = (('project', 'project_feature'),)


class ProjectPreviews(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, primary_key=True)
    previews = models.PositiveIntegerField()
    last_viewed_user_type = models.PositiveIntegerField(blank=True, null=True)
    last_viewed_user_id = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_previews'


class ProjectSkill(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    priority = models.IntegerField()
    skill = models.ForeignKey(MSkill, models.DO_NOTHING)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_skill'
        unique_together = (('project', 'skill'),)


class ProjectWorkingplace(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    prefecture = models.ForeignKey(MPrefecture, models.DO_NOTHING)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_workingplace'
        unique_together = (('project', 'prefecture'),)


class ProposalWorker(models.Model):
    business_talk_status = models.ForeignKey(BusinessTalkStatus, models.DO_NOTHING, primary_key=True)
    worker_id = models.PositiveIntegerField()
    prefecture_id = models.CharField(max_length=11, blank=True, null=True)
    city_id = models.CharField(max_length=11, blank=True, null=True)
    desired_contract_type = models.CharField(max_length=11, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    nearest_station = models.CharField(max_length=255, blank=True, null=True)
    current_monthly_income = models.CharField(max_length=255, blank=True, null=True)
    desired_monthly_income = models.CharField(max_length=255, blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    agent_comment = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal_worker'
        unique_together = (('business_talk_status', 'worker_id'),)


class ProposalWorkerDesiredAnotherFeature(models.Model):
    business_talk_status = models.ForeignKey(BusinessTalkStatus, models.DO_NOTHING, primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    desired_another_feature = models.ForeignKey(MAnotherFeature, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal_worker_desired_another_feature'
        unique_together = (('business_talk_status', 'worker', 'desired_another_feature'),)


class ProposalWorkerDesiredJob(models.Model):
    business_talk_status = models.ForeignKey(BusinessTalkStatus, models.DO_NOTHING, primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    desired_job = models.ForeignKey(MJob, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal_worker_desired_job'
        unique_together = (('business_talk_status', 'worker', 'desired_job'),)


class ProposalWorkerDesiredWorkingplace(models.Model):
    business_talk_status = models.ForeignKey(BusinessTalkStatus, models.DO_NOTHING, primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    prefecture = models.ForeignKey(MPrefecture, models.DO_NOTHING)
    priority = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal_worker_desired_workingplace'
        unique_together = (('business_talk_status', 'worker', 'prefecture'),)


class ProposalWorkerSkill(models.Model):
    business_talk_status = models.ForeignKey(BusinessTalkStatus, models.DO_NOTHING, primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    skill = models.ForeignKey(MSkill, models.DO_NOTHING)
    experience_id = models.CharField(max_length=11, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal_worker_skill'
        unique_together = (('business_talk_status', 'worker', 'skill'),)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user_engineer = models.ForeignKey('UserEngineer', models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_text = models.TextField()
    cancel_flag = models.IntegerField()
    reservation_cancel_text = models.TextField(blank=True, null=True)
    del_flag = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reservation'


class SearchProjectCondition(models.Model):
    user_engineer = models.ForeignKey('UserEngineer', models.DO_NOTHING, primary_key=True)
    category = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'search_project_condition'
        unique_together = (('user_engineer', 'category', 'code'),)


class SearchWorkerCondition(models.Model):
    user_company = models.ForeignKey('UserCompany', models.DO_NOTHING, primary_key=True)
    category = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'search_worker_condition'
        unique_together = (('user_company', 'category', 'code'),)


class SendRecommendProjectMail(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, primary_key=True)
    send_flag = models.IntegerField()
    send_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'send_recommend_project_mail'
        unique_together = (('project', 'create_date'),)


class SendRecommendWorkerMail(models.Model):
    worker = models.ForeignKey('Worker', models.DO_NOTHING, primary_key=True)
    send_flag = models.IntegerField()
    send_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'send_recommend_worker_mail'
        unique_together = (('worker', 'create_date'),)


class SkillNameIdentification(models.Model):
    skill = models.ForeignKey(MSkill, models.DO_NOTHING)
    skill_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_name_identification'


class TPrincipalStations(models.Model):
    station = models.ForeignKey(MStation, models.DO_NOTHING, primary_key=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_principal_stations'


class TProjectSkillPopularity(models.Model):
    skill = models.ForeignKey(MSkill, models.DO_NOTHING, primary_key=True)
    popularity = models.PositiveIntegerField()
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_project_skill_popularity'


class UserCompany(models.Model):
    user_company_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    first_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    catch_phrase = models.CharField(max_length=255, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    final_education = models.CharField(max_length=255, blank=True, null=True)
    educational_background_detail = models.CharField(max_length=255, blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    graduate_date = models.DateField(blank=True, null=True)
    final_employment_name = models.CharField(max_length=50, blank=True, null=True)
    final_employment_department = models.CharField(max_length=50, blank=True, null=True)
    final_employment_content = models.TextField(blank=True, null=True)
    final_employment_start_date = models.DateField(blank=True, null=True)
    final_employment_end_date = models.DateField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)
    one_time_token = models.CharField(max_length=255, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    human_resource_flag = models.IntegerField()
    agent_flag = models.IntegerField()
    admin_flag = models.PositiveIntegerField()
    account_suspended_flag = models.IntegerField(blank=True, null=True)
    authenticated_flag = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company'


class UserCompanyFavorite(models.Model):
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING, primary_key=True)
    target_type = models.PositiveIntegerField()
    target_id = models.PositiveIntegerField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_company_favorite'
        unique_together = (('user_company', 'target_type', 'target_id'),)


class UserCompanyMatchingScoreToWorker(models.Model):
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING, primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)
    matching_score = models.FloatField()
    mail_send_flag = models.IntegerField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_company_matching_score_to_worker'
        unique_together = (('user_company', 'worker'),)


class UserCompanyQualification(models.Model):
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING)
    qualification_name = models.CharField(max_length=100)
    certified_date = models.DateField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company_qualification'


class UserCompanyResponsibleArea(models.Model):
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING)
    prefecture_id = models.CharField(max_length=255)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company_responsible_area'
        unique_together = (('id', 'user_company', 'prefecture_id'),)


class UserCompanySpecialty(models.Model):
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING, primary_key=True)
    specialty = models.ForeignKey(MJob, models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_company_specialty'
        unique_together = (('user_company', 'specialty'), ('user_company', 'specialty'),)


class UserEngineer(models.Model):
    user_engineer_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=50, blank=True, null=True)
    line_id = models.CharField(max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    one_time_token = models.CharField(max_length=255, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    registration_phase = models.IntegerField()
    account_suspended_flag = models.IntegerField(blank=True, null=True)
    authenticated_flag = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_engineer'


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    worker_type = models.IntegerField(blank=True, null=True)
    user_engineer_id = models.IntegerField(blank=True, null=True)
    worker_manager = models.ForeignKey(UserCompany, models.DO_NOTHING, blank=True, null=True)
    belongs_company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    first_name_ruby = models.CharField(max_length=255, blank=True, null=True)
    initial_name = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    company_from = models.CharField(max_length=255, blank=True, null=True)
    prefecture_id = models.CharField(max_length=11, blank=True, null=True)
    city_id = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    desired_contract_type = models.CharField(max_length=11, blank=True, null=True)
    skill_management = models.CharField(max_length=11, blank=True, null=True)
    skill_english = models.CharField(max_length=11, blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)
    resume = models.CharField(max_length=255, blank=True, null=True)
    skill_sheet = models.CharField(max_length=255, blank=True, null=True)
    other_resume = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    final_education = models.IntegerField(blank=True, null=True)
    educational_background_detail = models.CharField(max_length=255, blank=True, null=True)
    graduate_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    nearest_station = models.CharField(max_length=255, blank=True, null=True)
    current_monthly_income = models.CharField(max_length=255, blank=True, null=True)
    desired_monthly_income = models.CharField(max_length=255, blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    agent_comment = models.TextField(blank=True, null=True)
    release_flag = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    last_update_user_id = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker'


class WorkerDesiredAnotherFeature(models.Model):
    worker_id = models.PositiveIntegerField()
    desired_another_feature_id = models.CharField(max_length=11)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_desired_another_feature'
        unique_together = (('worker_id', 'desired_another_feature_id'),)


class WorkerDesiredJob(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    desired_job = models.ForeignKey(MJob, models.DO_NOTHING)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_desired_job'
        unique_together = (('worker', 'desired_job'),)


class WorkerDesiredWorkingplace(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    prefecture = models.ForeignKey(MPrefecture, models.DO_NOTHING)
    priority = models.IntegerField(blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_desired_workingplace'
        unique_together = (('worker', 'prefecture'),)


class WorkerFavorite(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING, primary_key=True)
    target_type = models.PositiveIntegerField()
    target_id = models.PositiveIntegerField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_favorite'
        unique_together = (('worker', 'target_type', 'target_id'),)


class WorkerMatchingScoreToProject(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    matching_score = models.FloatField()
    mail_send_flag = models.IntegerField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_matching_score_to_project'
        unique_together = (('worker', 'project'),)


class WorkerPortfolio(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    portfolio_name = models.CharField(max_length=30, blank=True, null=True)
    portfolio_detail = models.CharField(max_length=255, blank=True, null=True)
    portfolio_file = models.CharField(max_length=255)
    portfolio_thumbnail = models.CharField(max_length=255, blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_portfolio'


class WorkerPreviews(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING, primary_key=True)
    previews = models.PositiveIntegerField()
    last_viewed_user_type = models.PositiveIntegerField(blank=True, null=True)
    last_viewed_user_id = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_previews'


class WorkerQuestionnaire(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING, primary_key=True)
    ans_capital = models.CharField(max_length=11, blank=True, null=True)
    ans_experience = models.CharField(max_length=11, blank=True, null=True)
    ans1 = models.CharField(max_length=11, blank=True, null=True)
    ans2 = models.CharField(max_length=11, blank=True, null=True)
    ans3 = models.CharField(max_length=11, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_questionnaire'


class WorkerReviews(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    user_company = models.ForeignKey(UserCompany, models.DO_NOTHING)
    review_rating = models.PositiveIntegerField()
    review_title = models.CharField(max_length=255, blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    release_flag = models.IntegerField()
    del_flag = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_reviews'
        unique_together = (('worker', 'user_company'),)


class WorkerSkill(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    skill = models.ForeignKey(MSkill, models.DO_NOTHING)
    experience_id = models.CharField(max_length=11, blank=True, null=True)
    del_flag = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_skill'
        unique_together = (('worker', 'skill'),)


class WorkerSns(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    sns_id = models.CharField(max_length=11)
    sns_account = models.CharField(max_length=255, blank=True, null=True)
    follow_user_num = models.PositiveIntegerField(blank=True, null=True)
    follower_user_num = models.PositiveIntegerField(blank=True, null=True)
    published_flag = models.PositiveIntegerField()
    del_flag = models.PositiveIntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'worker_sns'


class WorkerWorkHistory(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING)
    company_name = models.CharField(max_length=50)
    contract_type = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    job = models.ForeignKey(MJob, models.DO_NOTHING, blank=True, null=True)
    monthly_income = models.CharField(max_length=50, blank=True, null=True)
    management_experience = models.IntegerField(blank=True, null=True)
    work_content = models.TextField(blank=True, null=True)
    achievement = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_work_history'
