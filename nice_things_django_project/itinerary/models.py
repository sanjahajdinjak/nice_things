from django.db import models
from django_pandas.managers import DataFrameManager


class Food(models.Model):
    inspection_id = models.PositiveIntegerField(primary_key=True)
    dba_name = models.CharField(max_length=200)
    aka_name = models.CharField(max_length=200)
    license_num = models.PositiveIntegerField()
    facility_type = models.CharField(max_length=200)
    risk = models.CharField(max_length=200, default=None)
    address = models.CharField(max_length=200, default=None)
    city = models.CharField(max_length=200, default=None)
    state = models.CharField(max_length=2, default=None)
    zip_code = models.IntegerField(default=None)
    inspection_date = models.DateTimeField(default=None)
    inspection_type = models.CharField(max_length=200, default=None)
    results = models.CharField(max_length=200, default=None)
    violations = models.TextField(default=None)
    longitude = models.FloatField(default=None)
    latitude = models.FloatField(default=None)
    objects = DataFrameManager()


class Wages(models.Model):
    case_id = models.PositiveIntegerField(primary_key=True)
    trade_nm = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=200)
    street_addr_1_txt = models.CharField(max_length=200)
    cty_nm = models.CharField(max_length=200)
    st_cd = models.CharField(max_length=2)
    zip_code = models.IntegerField(default=None)
    case_violtn_cnt = models.PositiveIntegerField()
    longitude = models.FloatField(default=None)
    latitude = models.FloatField(default=None)
    objects = DataFrameManager()
    '''naic_cd
    naics_code_description

    cmp_assd_cnt
    ee_violtd_cnt
    bw_atp_amt
    ee_atp_cnt
    findings_start_date
    findings_end_date
    flsa_violtn_cnt
    flsa_repeat_violator
    flsa_bw_atp_amt
    flsa_ee_atp_cnt
    flsa_mw_bw_atp_amt
    flsa_ot_bw_atp_amt
    flsa_15a3_bw_atp_amt
    flsa_cmp_assd_amt
    sca_violtn_cnt
    sca_bw_atp_amt
    sca_ee_atp_cnt
    mspa_violtn_cnt
    mspa_bw_atp_amt
    mspa_ee_atp_cnt
    mspa_cmp_assd_amt
    h1b_violtn_cnt
    h1b_bw_atp_amt
    h1b_ee_atp_cnt
    h1b_cmp_assd_amt
    fmla_violtn_cnt
    fmla_bw_atp_amt
    fmla_ee_atp_cnt
    fmla_cmp_assd_amt
    flsa_cl_violtn_cnt
    flsa_cl_minor_cnt
    flsa_cl_cmp_assd_amt
    dbra_cl_violtn_cnt
    dbra_bw_atp_amt
    dbra_ee_atp_cnt
    h2a_violtn_cnt
    h2a_bw_atp_amt
    h2a_ee_atp_cnt
    h2a_cmp_assd_amt
    flsa_smw14_violtn_cnt
    flsa_smw14_bw_amt
    flsa_smw14_ee_atp_cnt
    cwhssa_violtn_cnt
    cwhssa_bw_amt
    cwhssa_ee_cnt
    osha_violtn_cnt
    osha_bw_atp_amt
    osha_ee_atp_cnt
    osha_cmp_assd_amt
    eppa_violtn_cnt
    eppa_bw_atp_amt
    eppa_ee_cnt
    eppa_cmp_assd_amt
    h1a_violtn_cnt
    h1a_bw_atp_amt
    h1a_ee_atp_cnt
    h1a_cmp_assd_amt
    crew_violtn_cnt
    crew_bw_atp_amt
    crew_ee_atp_cnt
    crew_cmp_assd_amt
    ccpa_violtn_cnt
    ccpa_bw_atp_amt
    ccpa_ee_atp_cnt
    flsa_smwpw_violtn_cnt
    flsa_smwpw_bw_atp_amt
    flsa_smwpw_ee_atp_cnt
    flsa_hmwkr_violtn_cnt
    flsa_hmwkr_bw_atp_amt
    flsa_hmwkr_ee_atp_cnt
    flsa_hmwkr_cmp_assd_amt
    ca_violtn_cnt
    ca_bw_atp_amt
    ca_ee_atp_cnt
    pca_violtn_cnt
    pca_bw_atp_amt
    pca_ee_atp_cnt
    flsa_smwap_violtn_cnt
    flsa_smwap_bw_atp_amt
    flsa_smwap_ee_atp_cnt
    flsa_smwft_violtn_cnt
    flsa_smwft_bw_atp_amt
    flsa_smwft_ee_atp_cnt
    flsa_smwl_violtn_cnt
    flsa_smwl_bw_atp_amt
    flsa_smwl_ee_atp_cnt
    flsa_smwmg_violtn_cnt
    flsa_smwmg_bw_atp_amt
    flsa_smwmg_ee_atp_cnt
    flsa_smwsl_violtn_cnt
    flsa_smwsl_bw_atp_amt
    flsa_smwsl_ee_atp_cnt
    eev_violtn_cnt
    h2b_violtn_cnt
    h2b_bw_atp_amt
    h2b_ee_atp_cnt
    sraw_violtn_cnt
    sraw_bw_atp_amt
    sraw_ee_atp_cnt
    ld_dt'''


# class Env_Enforce(models.Model):
#     '''
#     This model is data on environmental records from CDPH.
#     It does not contain information on the individual violations,
#     only that a violation exists. But the URL links to the details.
#     https://data.cityofchicago.org/Environment-Sustainable-Development/CDPH-Environmental-Records-Lookup-Table/a9u4-3dwb/data
#     '''
#     # needs a primary key
#     longitude = models.FloatField(default=None)
#     latitude = models.FloatField(default=None)
#     objects = DataFrameManager()
#     address = models.CharField(max_length=200) # need to concatentate strings for this
#     enviro_enforcement = models.BooleanField() # CDPH Enviro. Enforcement data
#     enviro_enforcement_url = models.URLField() # link to enviro information


class Env_Complaints(models.Model):
    '''
    This model is data on environmental records from CDPH.
    It does not contain information on the individual violations,
    only that a violation exists. But the URL links to the details.
    '''
    # needs a primary key
    longitude = models.FloatField(default=None)
    latitude = models.FloatField(default=None)
    objects = DataFrameManager()
    address = models.CharField(max_length=200) # need to concatentate strings for this
    complaints = models.BooleanField(default = None) # complaints in the CDPH Environmental Complaints data
    complaints_url = models.URLField(default = None) # link to the complaint
    enviro_enforcement = models.BooleanField(default = None)  # CDPH Enviro. Enforcement data
    enviro_enforcement_url = models.URLField(default = None)  # link to enviro information


class Divvy(models.Model):
    station_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    longitude = models.FloatField(default=None)
    latitude = models.FloatField(default=None)
    capacity = models.PositiveIntegerField()
    objects = DataFrameManager()









